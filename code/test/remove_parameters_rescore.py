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

    print('    Remove parameter {0}:'.format(param_names[iparam]))

    data_matrix_param = create_24x24_flow_matrix(not_home_row, side_top,
                                                 P[0],P[1],P[2],P[3],P[4],P[5],P[6],P[7],P[8],P[9],P[10],
                                                 1,1,1,1,1,1)
    if apply_strength:
        data_matrix_param = Strength24x24 * data_matrix_param

    param_scores = []
    for letters in test_layout_strings:
        score = score_layout(data_matrix_param, letters, bigrams, bigram_frequencies, verbose=False);
        param_scores.append(score)
        #print(letters, score)
            
    param_scores_sorted, param_ranks_sorted, Isort_param = rank_within_epsilon(param_scores, factor24, factor=True, verbose=False)
    param_layouts_sorted = []
    param_layout_strings_sorted = []
    for i in Isort_param:
        param_layouts_sorted.append(' '.join(test_layout_strings[i]))
        param_layout_strings_sorted.append(test_layout_strings[i])

    print('    Layout                                                  Score')
    for i, isort_param in enumerate(Isort_param):
        if param_ranks_sorted[isort_param] == 1:
            if isort_param < 9:
                s = '  '
            else:
                s = ' '
            print('    ({0}){1}{2}    {3}'.format(isort_param+1, s, 
                                                  param_layouts_sorted[i], 
                                                  param_scores_sorted[i]))