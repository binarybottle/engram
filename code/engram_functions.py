# %load code/engram_functions.py
# Import dependencies
import xlrd
import numpy as np
from sympy.utilities.iterables import multiset_permutations
import matplotlib
import matplotlib.pyplot as plt    
import seaborn as sns


def permute_optimize_keys(fixed_letters, fixed_letter_indices, open_letter_indices, 
                          all_letters, keys, data_matrix, bigrams, bigram_frequencies, 
                          min_score=0, verbose=False):
    """
    Find all permutations of letters, optimize layout, and generate output.
    """
    matrix_selected = select_keys(data_matrix, keys, verbose=False) 
    
    unassigned_letters = []
    for all_letter in all_letters:
        if all_letter not in fixed_letters:
            unassigned_letters.append(all_letter)
            if len(unassigned_letters) == len(open_letter_indices):
                break

    letter_permutations = permute_letters(unassigned_letters, verbose)
    if verbose:
        print("{0} permutations".format(len(letter_permutations)))
    top_permutation, top_score = optimize_layout(np.array([]), matrix_selected, bigrams, bigram_frequencies, letter_permutations, open_letter_indices, fixed_letters, fixed_letter_indices, min_score, verbose)
    
    return top_permutation, top_score


def permute_optimize(letters, all_letters, all_keys, data_matrix, bigrams, bigram_frequencies, min_score=0, verbose=False):
    """
    Find all permutations of letters, optimize layout, and generate output.
    """
    matrix_selected = select_keys(data_matrix, all_keys, verbose=False)
    open_positions = []
    fixed_positions = [] 
    open_letters = []
    fixed_letters = []
    assigned_letters = []
    for iletter, letter in enumerate(letters):
        if letter.strip() == "":
            open_positions.append(iletter)
            for all_letter in all_letters:
                if all_letter not in letters and all_letter not in assigned_letters:
                    open_letters.append(all_letter)
                    assigned_letters.append(all_letter)
                    break
        else:
            fixed_positions.append(iletter)
            fixed_letters.append(letter)

    letter_permutations = permute_letters(open_letters, verbose)
    if verbose:
        print("{0} permutations".format(len(letter_permutations)))
    top_permutation, top_score = optimize_layout(letters, matrix_selected, bigrams, bigram_frequencies, letter_permutations, open_positions, fixed_letters, fixed_positions, min_score, verbose)
        
    return top_permutation, top_score


def select_keys(data_matrix, keys, verbose=False):
    """
    Select keys to quantify pairwise relationships.
    """
    # Extract pairwise entries for the keys:
    nkeys = len(keys)
    Select = np.zeros((nkeys, nkeys))
    u = 0
    for i in keys:
        u += 1
        v = 0
        for j in keys:
            v += 1
            Select[u-1,v-1] = data_matrix[i-1,j-1]

    # Normalize matrix with min-max scaling to a range with max 1:
    newMin = np.min(Select) / np.max(Select)
    newMax = 1.0
    Select = newMin + (Select - np.min(Select)) * (newMax - newMin) / (np.max(Select) - np.min(Select))
    
    if verbose:
        # Heatmap of array
        heatmap(data=Select, title="Matrix heatmap", xlabel="Key 1", ylabel="Key 2", print_output=False); plt.show()
    
    return Select


def permute_letters(letters, verbose=False):
    """
    Find all permutations of a given set of letters (max: 8-10 letters).
    """
    letter_permutations = []
    for p in multiset_permutations(letters):
        letter_permutations.append(p)
    letter_permutations = np.array(letter_permutations)
    
    return letter_permutations


def score_layout(data_matrix, letters, bigrams, bigram_frequencies, verbose=False):
    """
    Compute the score for a given letter-key layout (NOTE normalization step).
    """
    # Create a matrix of bigram frequencies:
    nletters = len(letters)
    F2 = np.zeros((nletters, nletters))

    # Find the bigram frequency for each ordered pair of letters in the permutation:
    for i1 in range(nletters):
        for i2 in range(nletters):
            bigram = letters[i1] + letters[i2]
            i2gram = np.where(bigrams == bigram)
            if np.size(i2gram) > 0:
                F2[i1, i2] = bigram_frequencies[i2gram][0]

    # Normalize matrices with min-max scaling to a range with max 1:
    newMax = 1
    minF2 = np.min(F2)
    maxF2 = np.max(F2)
    newMin2 = minF2 / maxF2
    F2 = newMin + (F2 - minF2) * (newMax - newMin2) / (maxF2 - minF2)

    # Compute the score for this permutation:
    score  = np.average(data_matrix * F2) 
    if verbose:
        print("Score for letter permutation {0}: {1}".format(letters, score))

    return score


def tally_bigrams(input_text, bigrams, normalize=True, verbose=False):
    """
    Compute the score for a given letter-key layout (NOTE normalization step).
    """   
    # Find the bigram frequency for each ordered pair of letters in the input text
    #input_text = [str.upper(str(x)) for x in input_text]
    input_text = [str.upper(x) for x in input_text]
    nchars = len(input_text)
    F = np.zeros(len(bigrams))

    for ichar in range(0, nchars-1):
        bigram = input_text[ichar] + input_text[ichar + 1]
        i2gram = np.where(bigrams == bigram)
        if np.size(i2gram) > 0:
            F[i2gram] += 1

    # Normalize matrix with min-max scaling to a range with max 1:
    if normalize:
        newMax = 1
        newMin = np.min(F) / np.max(F)
        F = newMin + (F - np.min(F)) * (newMax - newMin) / (np.max(F) - np.min(F))

    bigram_frequencies_for_input = F

    if verbose:
        print("Bigram frequencies for input: {0}".format(bigram_frequencies_for_input))

    return bigram_frequencies_for_input


def tally_layout_samefinger_bigrams(layout, bigrams, bigram_frequencies, nkeys=32, verbose=False):
    """
    Tally the number of same-finger bigrams within (a list of 24 letters representing) a layout:
    ['P','Y','O','U','C','I','E','A','G','K','J','X','M','D','L','B','R','T','N','S','H','V','W','F']
    """  
    if nkeys == 32:
        #        Left:            Right:
        #    1  2  3  4 25   28 13 14 15 16 31 
        #    5  6  7  8 26   29 17 18 19 20 32
        #    9 10 11 12 27   30 21 22 23 24
        same_finger_keys = [[1,5],[5,9],[1,9], [2,6],[6,10],[2,10], 
                            [3,7],[7,11],[3,11], [4,8],[8,12],[4,12],
                            [25,26],[26,27],[25,27], [28,29],[29,30],[28,30], [31,32],
                            [4,25],[4,26],[4,27], [8,25],[8,26],[8,27], [12,25],[12,26],[12,27],
                            [13,28],[13,29],[13,30], [17,28],[17,29],[17,30], [21,28],[21,29],[21,30],
                            [31,16],[31,20],[31,24], [32,16],[32,20],[32,24],
                            [13,17],[17,21],[13,21], [14,18],[18,22],[14,22], 
                            [15,19],[19,23],[15,23], [16,20],[20,24],[16,24]] 
    elif nkeys == 24:
        #    1  2  3  4         13 14 15 16  
        #    5  6  7  8         17 18 19 20 
        #    9 10 11 12         21 22 23 24
        same_finger_keys = [[1,5],[5,9],[1,9], [2,6],[6,10],[2,10], 
                            [3,7],[7,11],[3,11], [4,8],[8,12],[4,12],
                            [13,17],[17,21],[13,21], [14,18],[18,22],[14,22], 
                            [15,19],[19,23],[15,23], [16,20],[20,24],[16,24]] 

    layout = [str.upper(x) for x in layout]
    max_frequency = 1.00273E+11

    samefinger_bigrams = []
    samefinger_bigram_counts = []
    for bigram_keys in same_finger_keys:
        bigram1 = layout[bigram_keys[0]-1] + layout[bigram_keys[1]-1]
        bigram2 = layout[bigram_keys[1]-1] + layout[bigram_keys[0]-1]
        i2gram1 = np.where(bigrams == bigram1)
        i2gram2 = np.where(bigrams == bigram2)
        if np.size(i2gram1) > 0:
            samefinger_bigrams.append(bigram1)
            samefinger_bigram_counts.append(max_frequency * bigram_frequencies[i2gram1] / np.max(bigram_frequencies))
        if np.size(i2gram2) > 0:
            samefinger_bigrams.append(bigram2)
            samefinger_bigram_counts.append(max_frequency * bigram_frequencies[i2gram2] / np.max(bigram_frequencies))

    samefinger_bigrams_total = np.sum(samefinger_bigram_counts)

    if verbose:
        print("    Total same-finger bigram frequencies: {0:15.0f}".format(samefinger_bigrams_total))

    return samefinger_bigrams, samefinger_bigram_counts, samefinger_bigrams_total 


def tally_layout_bigram_rolls(layout, bigrams, bigram_frequencies, nkeys=32, verbose=False):
    """
    Tally the number of bigrams that engage little-to-index finger inward rolls
    for (a list of 24 or 32 letters representing) a layout,
    within the four columns of one hand, or any column across two hands.
    layout = ['P','Y','O','U','C','I','E','A','G','K','J','X','L','D','B','V','N','T','R','S','H','M','W','F']
    bigram_rolls, bigram_roll_counts, bigram_rolls_total = tally_layout_bigram_rolls(layout, bigrams, bigram_frequencies, nkeys=24, verbose=True)
    """   
    if nkeys == 32:
        #        Left:            Right:
        #    1  2  3  4 25   28 13 14 15 16 31 
        #    5  6  7  8 26   29 17 18 19 20 32
        #    9 10 11 12 27   30 21 22 23 24

        roll_keys = [[1,2],[2,3],[3,4], [5,6],[6,7],[7,8], [9,10],[10,11],[11,12],
                    [16,15],[15,14],[14,13], [20,19],[19,18],[18,17], [24,23],[23,22],[22,21],
                    [1,3],[2,4],[1,4], [5,7],[6,8],[5,8], [9,11],[10,12],[9,12],
                    [16,14],[15,13],[16,13], [20,18],[19,17],[20,17], [24,22],[23,21],[24,21],
                    [1,6],[1,7],[1,8],[2,7],[2,8],[3,8], 
                    [5,2],[5,3],[5,4],[6,3],[6,4],[7,4],
                    [5,10],[5,11],[5,12],[6,11],[6,12],[7,12], 
                    [9,6],[9,7],[9,8],[10,7],[10,8],[11,8],
                    [16,19],[16,18],[16,17],[15,18],[15,17],[14,17], 
                    [20,15],[20,14],[20,13],[19,14],[19,13],[18,13],
                    [20,23],[20,22],[20,21],[19,22],[19,21],[18,21], 
                    [24,19],[24,18],[24,17],[23,18],[23,17],[22,17],
                    [1,10],[1,11],[1,12],[2,11],[2,12],[3,12],
                    [9,2],[9,3],[9,4],[10,3],[10,4],[11,4],
                    [16,23],[16,22],[16,21],[15,22],[15,21],[14,21],
                    [24,15],[24,14],[24,13],[23,14],[23,13],[22,13]]
        for i in [1,2,3,4,5,6,7,8,9,10,11,12, 25,26,27]:
            for j in [13,14,15,16,17,18,19,20,21,22,23,24, 28,29,30,31,32]:
                roll_keys.append([i,j])
        for i in [13,14,15,16,17,18,19,20,21,22,23,24, 28,29,30,31,32]:
            for j in [1,2,3,4,5,6,7,8,9,10,11,12, 25,26,27]:
                roll_keys.append([i,j])

    elif nkeys == 24:
        #    1  2  3  4         13 14 15 16  
        #    5  6  7  8         17 18 19 20 
        #    9 10 11 12         21 22 23 24
        roll_keys = [[1,2],[2,3],[3,4], [5,6],[6,7],[7,8], [9,10],[10,11],[11,12],
                    [16,15],[15,14],[14,13], [20,19],[19,18],[18,17], [24,23],[23,22],[22,21],
                    [1,3],[2,4],[1,4], [5,7],[6,8],[5,8], [9,11],[10,12],[9,12],
                    [16,14],[15,13],[16,13], [20,18],[19,17],[20,17], [24,22],[23,21],[24,21],
                    [1,6],[1,7],[1,8],[2,7],[2,8],[3,8], [5,2],[5,3],[5,4],[6,3],[6,4],[7,4],
                    [5,10],[5,11],[5,12],[6,11],[6,12],[7,12], [9,6],[9,7],[9,8],[10,7],[10,8],[11,8],
                    [16,19],[16,18],[16,17],[15,18],[15,17],[14,17], [20,15],[20,14],[20,13],[19,14],[19,13],[18,13],
                    [20,23],[20,22],[20,21],[19,22],[19,21],[18,21], [24,19],[24,18],[24,17],[23,18],[23,17],[22,17],
                    [1,10],[1,11],[1,12],[2,11],[2,12],[3,12], [9,2],[9,3],[9,4],[10,3],[10,4],[11,4],
                    [16,23],[16,22],[16,21],[15,22],[15,21],[14,21], [24,15],[24,14],[24,13],[23,14],[23,13],[22,13]]
        for i in range(0,12):
            for j in range(12,24):
                roll_keys.append([i,j])
        for i in range(12,24):
            for j in range(0,12):
                roll_keys.append([i,j])

    layout = [str.upper(x) for x in layout]
    max_frequency = 1.00273E+11

    bigram_rolls = []
    bigram_roll_counts = []
    for bigram_keys in roll_keys:
        bigram1 = layout[bigram_keys[0]-1] + layout[bigram_keys[1]-1]
        bigram2 = layout[bigram_keys[1]-1] + layout[bigram_keys[0]-1]
        i2gram1 = np.where(bigrams == bigram1)
        i2gram2 = np.where(bigrams == bigram2)
        if np.size(i2gram1) > 0:
            bigram_rolls.append(bigram1)
            bigram_roll_counts.append(max_frequency * bigram_frequencies[i2gram1] / np.max(bigram_frequencies))
        if np.size(i2gram2) > 0:
            bigram_rolls.append(bigram2)
            bigram_roll_counts.append(max_frequency * bigram_frequencies[i2gram2] / np.max(bigram_frequencies))

    bigram_rolls_total = np.sum(bigram_roll_counts)

    if verbose:
        print("    Total bigram inward roll frequencies: {0:15.0f}".format(bigram_rolls_total))

    return bigram_rolls, bigram_roll_counts, bigram_rolls_total 


def optimize_layout(starting_letters, data_matrix, bigrams, bigram_frequencies, letter_permutations, open_positions, fixed_letters, fixed_positions=[], min_score=0, verbose=False):
    """
    Compute scores for all letter-key layouts.
    """
    iter = 0
    top_score = min_score
    use_score_function = False

    nletters = len(open_positions) + len(fixed_positions)
    F2 = np.zeros((nletters, nletters))

    # Loop through the permutations of the selected letters:
    for p in letter_permutations:
        letters = np.array(['W' for x in range(nletters)])  # KEEP to initialize!
        for imove, open_position in enumerate(open_positions):
            letters[open_position] = p[imove]
        for ifixed, fixed_position in enumerate(fixed_positions):
            letters[fixed_position] = fixed_letters[ifixed]

        # Compute the score for this permutation:
        if use_score_function:
            score = score_layout(data_matrix, letters, bigrams, bigram_frequencies, verbose=False)
        else:
            # Find the bigram frequency for each ordered pair of letters in the permutation:
            for i1 in range(nletters):
                for i2 in range(nletters):
                    bigram = letters[i1] + letters[i2]
                    i2gram = np.where(bigrams == bigram)
                    if np.size(i2gram) > 0:
                        F2[i1, i2] = bigram_frequencies[i2gram][0]

            # Normalize matrices with min-max scaling to a range with max 1:
            newMax = 1
            minF2 = np.min(F2)
            maxF2 = np.max(F2)
            newMin2 = minF2 / maxF2
            F = newMin + (F2 - minF2) * (newMax - newMin2) / (maxF2 - minF2)

            # Compute the score for this permutation:
            score  = np.average(data_matrix * F) 

        if score > top_score:
            top_score = score
            top_permutation = letters
            
    if verbose:
        if top_score == min_score:
            print("top_score = min_score")
            top_permutation = starting_letters
        print("{0:0.8f}".format(top_score))
        print(*top_permutation)
        
    return top_permutation, top_score


def exchange_letters(letters, fixed_letter_indices, all_letters, all_keys, data_matrix, 
                     bigrams, bigram_frequencies, verbose=True):
    """
    Exchange letters, 8 keys at a time (8! = 40,320) selected twice in 14 different ways:

    Indices:
         0  1  2  3     12 13 14 15
         4  5  6  7     16 17 18 19
         8  9 10 11     20 21 22 23 

    1. Top rows
         0  1  2  3     12 13 14 15
    2. Bottom rows
         8  9 10 11     20 21 22 23 
    3. Top and bottom rows on the right side
                        12 13 14 15
                        20 21 22 23 
    4. Top and bottom rows on the left side 
         0  1  2  3
         8  9 10 11 
    5. Top right and bottom left rows
                        12 13 14 15
         8  9 10 11 
    6. Top left and bottom right rows 
         0  1  2  3
                        20 21 22 23 
    7. Center of the top and bottom rows on both sides
            1  2          13 14
            9 10          21 22
    8. The eight corners
         0        3    12       15
         8       11    20       23 
    9. Left half of the top and bottom rows on both sides 
         0  1          12 13
         8  9          20 21
    10. Right half of the top and bottom rows on both sides
               2  3          14 15
              10 11          22 23 
    11. Left half of non-home rows on the left and right half of the same rows on the right 
         0  1                14 15
         8  9                22 23 
    12. Right half of non-home rows on the left and left half of the same rows on the right
               2  3    12 13
              10 11    20 21 
    13. Top center and lower sides
            1  2           13 14
         8       11     20       23 
    14. Top sides and lower center
         0        3     12       15
            9 10           21 22   
    15. Repeat 1-14
         
    """
    top_score = score_layout(data_matrix, letters, bigrams, bigram_frequencies, verbose=False)
    print('Initial score: {0}'.format(top_score)) 
    print(*letters) 
    top_permutation = letters

    lists_of_open_indices = [
        [0,1,2,3,12,13,14,15],
        [8,9,10,11,20,21,22,23],
        [12,13,14,15,20,21,22,23],
        [0,1,2,3,8,9,10,11],
        [12,13,14,15,8,9,10,11],
        [0,1,2,3,20,21,22,23],
        [1,2,13,14,9,10,21,22],
        [0,3,12,15,8,11,20,23],
        [0,1,12,13,8,9,20,21],
        [2,3,14,15,10,11,22,23],
        [0,1,14,15,8,9,22,23],
        [2,3,12,13,10,11,20,21],
        [1,2,8,11,13,14,20,23],
        [0,3,9,10,12,15,21,22]  
    ]
    lists_of_print_statements = [
        '1. Top rows',
        '2. Bottom rows',
        '3. Top and bottom rows on the right side',
        '4. Top and bottom rows on the left side',
        '5. Top right and bottom left rows',
        '6. Top left and bottom right rows',
        '7. Center of the top and bottom rows on both sides',
        '8. The eight corners',
        '9. Left half of the top and bottom rows on both sides',
        '10. Right half of the top and bottom rows on both sides',
        '11. Left half of non-home rows on the left and right half of the same rows on the right',
        '12. Right half of non-home rows on the left and left half of the same rows on the right',
        '13. Top center and lower sides',
        '14. Top sides and lower center'
    ]
                         
    for istep in [1,2]:
        if istep == 1:
            s = "Set 1: 14 letter exchanges: "
        elif istep == 2:
            s = "Set 2: 14 letter exchanges: "

        for ilist, open_indices in enumerate(lists_of_open_indices):
            print_statement = lists_of_print_statements[ilist]     

            if verbose:
                print('{0} {1}'.format(s, print_statement))
                             
            for open_index in open_indices:
                if open_index not in fixed_letter_indices:
                    top_permutation[open_index] = ''
            
            top_permutation, top_score = permute_optimize(top_permutation, letters24, keys24, data_matrix, 
                                                          bigrams, bigram_frequencies, min_score=top_score, 
                                                          verbose=True)                    
    if verbose:
        print('')
        print('    -------- DONE --------') 
        print('')

    return top_permutation, top_score
                             

def rank_within_epsilon(numbers, epsilon, factor=False, verbose=True):
    """
    numbers = np.array([10,9,8,7,6])
    epsilon = 1
    rank_within_epsilon(numbers, epsilon, factor=False, verbose=True) 
    >>> array([1., 1., 2., 2., 3.])
    numbers = np.array([0.798900824, 0.79899900824, 0.79900824])
    epsilon = 0.9**8 - 0.9**9
    factor24 = ((24**2 - 1) + (1-epsilon)) / (24**2) # 0.999925266109375
    rank_within_epsilon(numbers, factor24, factor=True, verbose=True) 
    >>> array([2., 1., 1.])
    """
    numbers = np.array(numbers)
    Isort = np.argsort(-numbers)
    numbers_sorted = numbers[Isort]
    count = 1
    ranks = np.zeros(np.size(numbers))
    for i, num in enumerate(numbers_sorted):
        if ranks[i] == 0:
            if factor:
                lower_bound = num * epsilon
            else:
                lower_bound = num - epsilon
            bounded_nums1 = num >= numbers_sorted
            bounded_nums2 = numbers_sorted >= lower_bound
            bounded_nums = bounded_nums1 * bounded_nums2
            count += 1
            for ibounded, bounded_num in enumerate(bounded_nums):
                if bounded_num == True:
                    ranks[ibounded] = count

    uranks = np.unique(ranks)
    nranks = np.size(uranks)
    new_ranks = ranks.copy()
    new_count = 0
    for rank in uranks:
        new_count += 1
        same_ranks = ranks == rank
        for isame, same_rank in enumerate(same_ranks):
            if same_rank == True:
                new_ranks[isame] = new_count

    #ranks_sorted = new_ranks[Isort]
    ranks_sorted = [np.int(x) for x in new_ranks]
    
    if verbose:
        for i, num in enumerate(numbers_sorted):
            print("    ({0})    {1}".format(np.int(ranks_sorted[i]), num))
        
    return numbers_sorted, ranks_sorted, Isort


def print_matrix_info(matrix_data, matrix_label, nkeys, nlines=10):
    """
    Print matrix output.
    """
    print("{0} min = {1}, max = {2}".format(matrix_label, np.min(matrix_data), np.max(matrix_data)))
    matrix_flat = matrix_data.flatten()
    argsort = np.argsort(matrix_flat)
    print("{0} key number pairs with minimum values:".format(matrix_label))
    for x in argsort[0:nlines]:
        if x % nkeys == 0:
            min_row = np.int(np.ceil(x / nkeys)) + 1
            min_col = 1
        else:
            min_row = np.int(np.ceil(x / nkeys))
            min_col = x - nkeys * (min_row-1) + 1                
        print("        {0} -> {1}        ({2})".format(min_row, min_col, matrix_flat[x]))
    print("{0} key number pairs with maximum values:".format(matrix_label))
    max_sort = argsort[-nlines::]
    for x in max_sort[::-1]:
        if x % nkeys == 0:
            max_row = np.int(np.ceil(x / nkeys)) + 1
            max_col = 1
        else:
            max_row = np.int(np.ceil(x / nkeys))
            max_col = x - nkeys * (max_row-1) + 1                
        print("        {0} -> {1}        ({2})".format(max_row, max_col, matrix_flat[x]))


def heatmap(data, title="", xlabel="", ylabel="", x_axis_labels=[], y_axis_labels=[], print_output=True):
    """
    Plot heatmap of matrix.
    """
    # use heatmap function, set the color as viridis and
    # make each cell seperate using linewidth parameter
    plt.figure()
    sns_plot = sns.heatmap(data, xticklabels=x_axis_labels, yticklabels=y_axis_labels, linewidths=1, 
                           cmap="viridis", square=True, vmin=np.min(data), vmax=np.max(data))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    sns_plot.set_xticklabels(x_axis_labels)  #, rotation=75) 
    sns_plot.set_yticklabels(y_axis_labels) 
    if print_output:
        sns_plot.figure.savefig("{0}_heatmap.png".format(title))
        
    
def histmap(data, title="", print_output=True):
    """
    Plot histogram.
    """
    sns.distplot(data)
    plt.title(title)
    if print_output:
        sns_plot.figure.savefig("{0}_histogram.png".format(title))
        
        
def print_layout24(layout):
    """
    Print layout.
    """   
    print('    {0}  {1}'.format(' '.join(layout[0:4]),
                                ' '.join(layout[12:16])))
    print('    {0}  {1}'.format(' '.join(layout[4:8]),
                                ' '.join(layout[16:20])))
    print('    {0}  {1}'.format(' '.join(layout[8:12]),
                                ' '.join(layout[20:24])))


def print_layout24_instances(layout, letters24, instances24, bigrams, bigram_frequencies):
    """
    Print billions of instances per letter (not Z or Q) in layout form.
    layout = ['P','Y','O','U','C','I','E','A','G','K','J','X','M','D','L','B','R','T','N','S','H','V','W','F']
    print_layout24_instances(layout, letters24, instances24, bigrams, bigram_frequencies)
    """
    layout_instances = []
    layout_instances_strings = []
    for letter in layout:
        index = letters24.index(letter)
        layout_instances.append(instances24[index])
        layout_instances_strings.append('{0:3.0f}'.format(instances24[index]/1000000000))
 
    print('    {0}  {1}'.format(' '.join(layout_instances_strings[0:4]),
                                ' '.join(layout_instances_strings[12:16])))
    print('    {0}  {1}'.format(' '.join(layout_instances_strings[4:8]),
                                ' '.join(layout_instances_strings[16:20])))
    print('    {0}  {1}'.format(' '.join(layout_instances_strings[8:12]),
                                ' '.join(layout_instances_strings[20:24])))
    left_sum = np.sum(layout_instances[0:12])/1000000000000
    right_sum = np.sum(layout_instances[12:24])/1000000000000
    pL = ''
    pR = ''
    if left_sum > right_sum:
        pL = ' ({0:3.2f}%)'.format(100 * (left_sum - right_sum) / right_sum)
    elif right_sum > left_sum:
        pR = ' ({0:3.2f}%)'.format(100 * (right_sum - left_sum) / left_sum)
    
    print('\n    left: {0:3.3f}T{1}  right: {2:3.3f}T{3}'.format(left_sum, pL, 
                                                                 right_sum, pR))
    
    tally_layout_samefinger_bigrams(layout, bigrams, bigram_frequencies, nkeys=24, verbose=True)
    tally_layout_bigram_rolls(layout, bigrams, bigram_frequencies, nkeys=24, verbose=True)
   

def print_bigram_frequency(input_pair, bigrams, bigram_frequencies):
    """
    >>> print_bigram_frequency(['t','h'], bigrams, bigram_frequencies)
    """
    # Find the bigram frequency
    max_frequency = 1.00273E+11
    input_text = [str.upper(str(x)) for x in input_pair]
    nchars = len(input_text)
    for ichar in range(0, nchars-1):
        bigram1 = input_text[ichar] + input_text[ichar + 1]
        bigram2 = input_text[ichar + 1] + input_text[ichar]
        i2gram1 = np.where(bigrams == bigram1)
        i2gram2 = np.where(bigrams == bigram2)
        if np.size(i2gram1) > 0:
            freq1 = max_frequency/1e9 * bigram_frequencies[i2gram1[0][0]]
            print("{0}: {1:3.2f}B".format(bigram1, freq1))
        if np.size(i2gram2) > 0:
            freq2 = max_frequency/1e9 * bigram_frequencies[i2gram2[0][0]]
            print("{0}: {1:3.2f}B".format(bigram2, freq2))