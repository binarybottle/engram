data_matrix_strength = Strength24x24
strength_scores = []
for letters in test_layout_strings:
    score = score_layout(data_matrix_strength, letters,  bigrams, bigram_frequencies, verbose = False) 
    strength_scores.append(score)

strength_scores_sorted, strength_ranks_sorted, Isort_strength = rank_within_epsilon(strength_scores, 
                                                                    factor, factor=True, verbose=False)
print('\nRank:   Layout                                             Strength score        Score\n')
for i, rank in enumerate(strength_ranks_sorted):
    if rank == 1:
        print('    {0}:  {1}    {2}'.format(rank, test_layouts[Isort_strength[i]], 
                                            strength_scores_sorted[i]))