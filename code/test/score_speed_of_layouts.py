data_matrix_speed = Speed24x24

print('epsilon    = {0}'.format(epsilon))

speed_scores = []
for letters in test_layout_strings:
    score = score_layout(data_matrix_speed, letters[0:24], bigrams, bigram_frequencies, verbose = False) 
    speed_scores.append(score)

speed_scores_sorted, speed_ranks_sorted, Isort_speed = rank_within_epsilon(speed_scores, epsilon, factor=False, verbose=False)

print('\nRank:   Layout                                             Speed score           Score\n')
for i, rank in enumerate(speed_ranks_sorted):
    if rank == 1:
        print('    {0}:  {1}    {2}'.format(rank, test_layouts[Isort_speed[i]][0:24], 
                                            speed_scores_sorted[i]))