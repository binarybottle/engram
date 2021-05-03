data_matrix_strength = Strength24x24
strength_scores = []
for letters in test_layout_strings:
    score = score_layout(data_matrix_strength, letters,  bigrams, bigram_frequencies, verbose = False) 
    strength_scores.append(score)

strength_scores_sorted, strength_ranks_sorted, Isort_strength = rank_within_epsilon(strength_scores, 
                                                                    factor32, factor=True, verbose=False)
strength_layouts_sorted = []
strength_layout_strings_sorted = []
for i in Isort_strength:
    strength_layouts_sorted.append(' '.join(test_layout_strings[i]))
    strength_layout_strings_sorted.append(test_layout_strings[i])

print('    Layout                                                  Strength score')
count = 0
for i, isort_strength in enumerate(Isort_strength):
    if strength_ranks_sorted[isort_strength] == 1:
        count += 1
        if isort_strength < 9:
            s = '  '
        else:
            s = ' '
        print('    ({0}){1}{2}    {3}'.format(isort_strength+1, s, 
                                              strength_layouts_sorted[i], 
                                              strength_scores_sorted[i]))
print('    {0} of {1} layouts tied for first place'.format(count, len(test_layout_strings)))