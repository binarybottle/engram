layout_strings = []
scores = []
for layout in top_layouts:
    layout_string = ' '.join(layout)
    score = score_layout(Factors24x24, layout, bigrams, bigram_frequencies, verbose=False)
    #print('    {0}    {1}'.format(layout_string, score))
    layout_strings.append(layout_string)
    scores.append(score)

# Establish which layouts are within a small difference of the top-scoring layout 
#    - half of the smallest difference between two flow penalties, ignoring strength: (0.9^9 - 0.9^10)/2
#    - divided by the number of key pairs: 24^2
delta_flow = (0.9**8 - 0.9**9)
factor = ((24**2 - 1) + (1-delta_flow)) / (24**2)
print('    The smallest difference between two flow penalties: (0.9^8 - 0.9^9) = {0}'.format(delta_flow))
print('    ...divided by the number of key pairs (24^2) = {0}'.format(factor))
scores_sorted, ranks_sorted, Isort = rank_within_epsilon(scores, factor, factor=True, verbose=False)
layouts_sorted = []
layout_strings_sorted = []
for i in Isort:
    layouts_sorted.append(top_layouts[i])
    layout_strings_sorted.append(layout_strings[i])
print('\nRank:   Layout                                             Score\n')
for i, rank in enumerate(ranks_sorted):
    print('    {0}:  {1}    {2}'.format(rank, layout_strings_sorted[i], scores_sorted[i]))

print('\nLayouts tied for first place, with letter frequencies:\n')
print('Rank:   Layout                                             Score\n')
first_ranks = []
first_layouts = []
first_layout_strings = []
first_scores = []
for i, rank in enumerate(ranks_sorted):
    if rank == 1:
        first_ranks.append(rank)
        first_layouts.append(layout_strings_sorted[i])
        first_layout_strings.append(layouts_sorted[i])
        first_scores.append(scores_sorted[i])    
Isort2 = np.argsort([-x for x in first_scores])
first_ranks_sorted = []
first_layouts_sorted = []
first_layout_strings_sorted = []
first_scores_sorted = []
for i in Isort2:
    first_ranks_sorted.append(first_ranks[i])
    first_layouts_sorted.append(first_layouts[i])
    first_layout_strings_sorted.append(first_layout_strings[i])
    first_scores_sorted.append(first_scores[i])
for i, first_layout in enumerate(first_layouts):
    print('    {0}:  {1}    {2}'.format(first_ranks_sorted[i], 
                                        first_layout,  # first_layout_strings_sorted[i], 
                                        first_scores_sorted[i]))
# Print layouts:
for i, layout_string in enumerate(first_layout_strings_sorted):
    layout = first_layouts_sorted[i]
    print('')
    print_layout24(layout_string)
    print('')
    print_layout24_instances(layout_string, letters24, instances24, bigrams, bigram_frequencies)
    print('')