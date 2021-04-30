params0 = [side_above_3away, side_above_2away, side_above_1away, middle_above_ring, ring_above_middle, 
           outward, skip_row_3away, skip_row_2away, skip_row_1away, skip_row_0away, same_finger]
param_names = ['side_above_3away', 'side_above_2away', 'side_above_1away', 
               'middle_above_ring', 'ring_above_middle', 'outward', 'skip_row_3away', 
               'skip_row_2away', 'skip_row_1away', 'skip_row_0away', 'same_finger']
params_lists = []
for i in range(len(params0)):
    params_list = params0.copy()
    params_list[i] = 1.0
    params_lists.append(params_list)

for iparam, P in enumerate(params_lists):

    print('\nRemove parameter {0}:'.format(param_names[iparam]))

    data_matrix_param = create_24x24_flow_matrix(not_home_row, side_top,
                                                 P[0],P[1],P[2],P[3],P[4],P[5],P[6],P[7],P[8],P[9],P[10],
                                                 1,1,1,1,1,1)
    if apply_strength:
        data_matrix_param = Strength24x24 * data_matrix_param

    param_scores = []
    for letters in test_layout_strings:
        score = score_layout(data_matrix_param, letters, bigrams, bigram_frequencies, verbose=False);
        param_scores.append(score)
            
    param_scores_sorted, param_ranks_sorted, Isort_param = rank_within_epsilon(param_scores, factor, factor=True, verbose=False)
    param_layouts_sorted = []
    param_layout_strings_sorted = []
    for i in Isort_param:
        param_layouts_sorted.append(test_layouts[i])
        param_layout_strings_sorted.append(test_layout_strings[i])

    print('Rank:   Layout                                             Score\n')
    for i, rank in enumerate(param_ranks_sorted):
        if rank == 1:
            if rank_variations:
                print('    {0}:  {1}    {2}'.format(rank, layouts_first_place[i], param_scores_sorted[i]))
            else:
                print('    {0}:  {1}    {2}'.format(rank, layout_strings_sorted[i], param_scores_sorted[i]))