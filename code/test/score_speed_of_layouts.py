data_matrix_speed = Speed24x24
speed_scores = []
for letters in test_layout_strings:
    score = score_layout(data_matrix_speed, letters,  bigrams, bigram_frequencies, verbose = False) 
    speed_scores.append(score)

speed_scores_sorted, speed_ranks_sorted, Isort_speed = rank_within_epsilon(speed_scores, 
                                                                    epsilon, factor=False, verbose=False)
speed_layouts_sorted = []
speed_layout_strings_sorted = []
for i in Isort_speed:
    speed_layouts_sorted.append(' '.join(test_layout_strings[i]))
    speed_layout_strings_sorted.append(test_layout_strings[i])

count = 0
print('    Layout                                                  Speed score')
for i, isort_speed in enumerate(Isort_speed):
    if speed_ranks_sorted[isort_speed] == 1:
        count += 1
        if isort_speed < 9:
            s = '  '
        else:
            s = ' '
        print('    ({0}){1}{2}    {3}'.format(isort_speed+1, s, 
                                              speed_layouts_sorted[i], 
                                              speed_scores_sorted[i]))
print('    {0} of {1} layouts tied for first place'.format(count, len(test_layout_strings)))