# Penalizing factors for 24 keys  (1 = no penalty; set to less than 1 to penalize):

# Dexterity
side_above_3away = 0.9     # index and little finger type two keys, one or more rows apart (same hand)
side_above_2away = 0.81    # index finger types key a row or two above ring finger key, or
                           # little finger types key a row or two above middle finger key (same hand)
side_above_1away = 0.729   # index finger types key a row or two above middle finger key, or
                           # little finger types key a row or two above ring finger key (same hand)
middle_above_ring = 0.9    # middle finger types key a row or two above ring finger key (same hand)
ring_above_middle = 0.729  # ring finger types key a row or two above middle finger key (same hand)
lateral = 0.9              # lateral movement of (index or little) finger outside of 8 vertical columns

# Direction
outward = 0.9              # outward roll of fingers from the index to little finger (same hand)

# Distance
skip_row_3away = 0.9       # index and little fingers type two keys that skip over home row (same hand)
                           # (e.g., one on bottom row, the other on top row)
skip_row_2away = 0.729     # little and middle or index and ring fingers type two keys that skip over home row (same hand)
skip_row_1away = 0.59049   # little and ring or middle and index fingers type two keys that skip over home row (same hand)

# Repetition
skip_row_0away = 0.6561    # same finger types two keys that skip over home row
same_finger = 0.59049      # use same finger again for a different key


# Unused or redundant parameters
same_hand = 1.0            # (addressed by splitting up the most frequent letters across left/right sides above)
not_home_row = 1.0         # at least one key not on home row
side_top = 1.0             # index or little finger types top corner key
shorter_above = 1.0        # (taken care of by side_above_[1,2,3]away parameters)
adjacent_offset = 1.0      # (taken care of by side_above_1away, middle_above_ring, ring_above_middle parameters)
inside_top = 1.0           # index finger types top corner key (taken care of by side_above_1away parameter)
index_above = 1.0          # index finger types top corner key (unless other bigram key is in the top row for the same hand)
                           # (taken care of by side_above_[1,2,3]away parameters)


def create_24x24_flow_matrix(not_home_row, side_top, side_above_3away, side_above_2away, side_above_1away, 
                             middle_above_ring, ring_above_middle, outward, skip_row_3away, 
                             skip_row_2away, skip_row_1away, skip_row_0away, same_finger, lateral, 
                             same_hand, shorter_above, adjacent_offset, inside_top, index_above):

    all_24_keys = [1,2,3,4, 5,6,7,8, 9,10,11,12, 13,14,15,16, 17,18,19,20, 21,22,23,24]

    # Create a matrix and multiply by flow factors that promote easy interkey transitions:
    T = np.ones((24, 24))

    # 7.  Promote alternating between hands over uncomfortable transitions with the same hand.
    if same_hand < 1.0:
    #    1  2  3  4   13 14 15 16  
    #    5  6  7  8   17 18 19 20 
    #    9 10 11 12   21 22 23 24
        for i in range(0,12):
            for j in range(0,12):
                T[i,j] *= same_hand
        for i in range(12,24):
            for j in range(12,24):
                T[i,j] *= same_hand

    # 8.  Promote little-to-index-finger roll-ins over index-to-little-finger outwards.
    #    1  2  3  4   13 14 15 16  
    #    5  6  7  8   17 18 19 20 
    #    9 10 11 12   21 22 23 24
    if outward < 1.0:

        # same-row roll-outs:
        roll_ins = [[1,2],[2,3],[3,4], [5,6],[6,7],[7,8], [9,10],[10,11],[11,12],
                    [16,15],[15,14],[14,13], [20,19],[19,18],[18,17], [24,23],[23,22],[22,21]]
        for x in roll_ins:
            T[x[1]-1, x[0]-1] *= outward

        # same-row roll-outs, skipping keys:
        roll_ins_skip_keys = [[1,3],[2,4],[1,4], [5,7],[6,8],[5,8], [9,11],[10,12],[9,12],
                              [16,14],[15,13],[16,13], [20,18],[19,17],[20,17], [24,22],[23,21],[24,21]]
        for x in roll_ins_skip_keys:
            T[x[1]-1, x[0]-1] *= outward

        # adjacent-row roll-outs:
        roll_ins_adj_rows = [[1,6],[1,7],[1,8],[2,7],[2,8],[3,8], [5,2],[5,3],[5,4],[6,3],[6,4],[7,4],
                             [5,10],[5,11],[5,12],[6,11],[6,12],[7,12], [9,6],[9,7],[9,8],[10,7],[10,8],[11,8],
                             [16,19],[16,18],[16,17],[15,18],[15,17],[14,17], [20,15],[20,14],[20,13],[19,14],[19,13],[18,13],
                             [20,23],[20,22],[20,21],[19,22],[19,21],[18,21], [24,19],[24,18],[24,17],[23,18],[23,17],[22,17]]
        for x in roll_ins_adj_rows:
            T[x[1]-1, x[0]-1] *= outward

        # upper<->lower row roll-outs:
        roll_ins_skip_home = [[1,10],[1,11],[1,12],[2,11],[2,12],[3,12], [9,2],[9,3],[9,4],[10,3],[10,4],[11,4],
                              [16,23],[16,22],[16,21],[15,22],[15,21],[14,21], [24,15],[24,14],[24,13],[23,14],[23,13],[22,13]]
        for x in roll_ins_skip_home:
            T[x[1]-1, x[0]-1] *= outward

    # 9.  Avoid stretching shorter fingers up and longer fingers down.
    #    1  2  3  4   13 14 15 16  
    #    5  6  7  8   17 18 19 20 
    #    9 10 11 12   21 22 23 24
    if index_above < 1.0:
        for x in [4]:
            for y in [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]:
                T[x-1, y-1] *= index_above
                T[y-1, x-1] *= index_above
        for x in [13]:
            for y in [1,2,3,4,5,6,7,8,9,10,11,12,13,17,18,19,20,21,22,23,24]:
                T[x-1, y-1] *= index_above
                T[y-1, x-1] *= index_above
    if inside_top < 1.0:
        for x in [4,13]:
            for j in range(0,24):
                T[x-1, j] *= inside_top
                T[j, x-1] *= inside_top
    if side_top < 1.0:
        for x in [1,4,13,16]:
            for j in range(0,24):
                T[x-1, j] *= side_top
                T[j, x-1] *= side_top
    if side_above_1away < 1.0:
        for x in [1]:
            for y in [6,10]:
                T[x-1, y-1] *= side_above_1away
                T[y-1, x-1] *= side_above_1away
        for x in [5]:
            for y in [10]:
                T[x-1, y-1] *= side_above_1away
                T[y-1, x-1] *= side_above_1away
        for x in [4]:
            for y in [7,11]:
                T[x-1, y-1] *= side_above_1away
                T[y-1, x-1] *= side_above_1away
        for x in [8]:
            for y in [11]:
                T[x-1, y-1] *= side_above_1away
                T[y-1, x-1] *= side_above_1away
        for x in [13]:
            for y in [18,22]:
                T[x-1, y-1] *= side_above_1away
                T[y-1, x-1] *= side_above_1away
        for x in [17]:
            for y in [22]:
                T[x-1, y-1] *= side_above_1away
                T[y-1, x-1] *= side_above_1away
        for x in [16]:
            for y in [19,23]:
                T[x-1, y-1] *= side_above_1away
                T[y-1, x-1] *= side_above_1away
        for x in [20]:
            for y in [23]:
                T[x-1, y-1] *= side_above_1away
                T[y-1, x-1] *= side_above_1away
    if side_above_2away < 1.0:
        for x in [1]:
            for y in [7,11]:
                T[x-1, y-1] *= side_above_2away
                T[y-1, x-1] *= side_above_2away
        for x in [5]:
            for y in [11]:
                T[x-1, y-1] *= side_above_2away
                T[y-1, x-1] *= side_above_2away
        for x in [4]:
            for y in [6,10]:
                T[x-1, y-1] *= side_above_2away
                T[y-1, x-1] *= side_above_2away
        for x in [8]:
            for y in [10]:
                T[x-1, y-1] *= side_above_2away
                T[y-1, x-1] *= side_above_2away
        for x in [13]:
            for y in [19,23]:
                T[x-1, y-1] *= side_above_2away
                T[y-1, x-1] *= side_above_2away
        for x in [17]:
            for y in [23]:
                T[x-1, y-1] *= side_above_2away
                T[y-1, x-1] *= side_above_2away
        for x in [16]:
            for y in [18,22]:
                T[x-1, y-1] *= side_above_2away
                T[y-1, x-1] *= side_above_2away
        for x in [20]:
            for y in [22]:
                T[x-1, y-1] *= side_above_2away
                T[y-1, x-1] *= side_above_2away
    if side_above_3away < 1.0:
        for x in [1]:
            for y in [8,12]:
                T[x-1, y-1] *= side_above_3away
                T[y-1, x-1] *= side_above_3away
        for x in [5]:
            for y in [12]:
                T[x-1, y-1] *= side_above_3away
                T[y-1, x-1] *= side_above_3away
        for x in [4]:
            for y in [5,9]:
                T[x-1, y-1] *= side_above_3away
                T[y-1, x-1] *= side_above_3away
        for x in [8]:
            for y in [9]:
                T[x-1, y-1] *= side_above_3away
                T[y-1, x-1] *= side_above_3away
        for x in [13]:
            for y in [20,24]:
                T[x-1, y-1] *= side_above_3away
                T[y-1, x-1] *= side_above_3away
        for x in [17]:
            for y in [24]:
                T[x-1, y-1] *= side_above_3away
                T[y-1, x-1] *= side_above_3away
        for x in [16]:
            for y in [17,21]:
                T[x-1, y-1] *= side_above_3away
                T[y-1, x-1] *= side_above_3away
        for x in [20]:
            for y in [21]:
                T[x-1, y-1] *= side_above_3away
                T[y-1, x-1] *= side_above_3away
    if shorter_above < 1.0:
        for x in [1]:
            for y in [6,7,8,10,11,12]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [2]:
            for y in [7,11]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [4]:
            for y in [6,7,10,11]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above

        for x in [5]:
            for y in [10,11,12]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [6]:
            for y in [11]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [8]:
            for y in [10,11]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above

        for x in [16]:
            for y in [17,18,19,21,22,23]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [15]:
            for y in [18,22]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [13]:
            for y in [18,19,22,23]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above

        for x in [20]:
            for y in [21,22,23]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [19]:
            for y in [22]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [17]:
            for y in [22,23]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above

    if ring_above_middle < 1.0:
        ring_above_middles =  [[2,7],[6,11],[2,11],
                            [15,18],[19,22],[15,22]]
        for x in ring_above_middles:
            T[x[0]-1, x[1]-1] *= ring_above_middle
            T[x[1]-1, x[0]-1] *= ring_above_middle

    if middle_above_ring < 1.0:
        middle_above_rings =  [[6,3],[10,7],[10,3],
                            [19,14],[23,18],[23,14]]
        for x in middle_above_rings:
            T[x[0]-1, x[1]-1] *= middle_above_ring
            T[x[1]-1, x[0]-1] *= middle_above_ring

    # 10. Avoid using the same finger.
    #    1  2  3  4   13 14 15 16  
    #    5  6  7  8   17 18 19 20 
    #    9 10 11 12   21 22 23 24
    if same_finger < 1.0:
        same_fingers = [[1,5],[5,9],[1,9], [2,6],[6,10],[2,10], [3,7],[7,11],[3,11], [4,8],[8,12],[4,12],
                        [13,17],[17,21],[13,21], [14,18],[18,22],[14,22], [15,19],[19,23],[15,23], [16,20],[20,24],[16,24]] 
        for x in same_fingers:
            T[x[0]-1, x[1]-1] *= same_finger
            T[x[1]-1, x[0]-1] *= same_finger

    # 11. Avoid the upper and lower rows.
    #    1  2  3  4   13 14 15 16  
    #    5  6  7  8   17 18 19 20 
    #    9 10 11 12   21 22 23 24
    if not_home_row < 1.0:
        not_home_row_keys = [1,2,3,4, 9,10,11,12, 13,14,15,16, 21,22,23,24]
        for x in not_home_row_keys:
            for j in range(0,23):
                T[x-1, j] *= not_home_row
                T[j, x-1] *= not_home_row

    # 12. Avoid skipping over the home row.
    #    1  2  3  4   13 14 15 16  
    #    5  6  7  8   17 18 19 20 
    #    9 10 11 12   21 22 23 24
    if skip_row_0away < 1.0:
        skip_top = [1, 2, 3, 4, 13,14,15,16] 
        skip_bot = [9,10,11,12, 21,22,23,24] 
        for ix, x in enumerate(skip_top):
            y = skip_bot[ix]
            T[x-1, y-1] *= skip_row_0away
            T[y-1, x-1] *= skip_row_0away
    if skip_row_1away < 1.0:
        skip_top = [1, 2, 2, 3, 3, 4, 13,14,14,15,15,16] 
        skip_bot = [10,9,11,10,12,11, 22,21,23,22,24,23] 
        for ix, x in enumerate(skip_top):
            y = skip_bot[ix]
            T[x-1, y-1] *= skip_row_1away
            T[y-1, x-1] *= skip_row_1away
    if skip_row_2away < 1.0:
        skip_top = [1,  2,3, 4, 13,14,15,16] 
        skip_bot = [11,12,9,10, 23,24,21,22] 
        for ix, x in enumerate(skip_top):
            y = skip_bot[ix]
            T[x-1, y-1] *= skip_row_2away
            T[y-1, x-1] *= skip_row_2away
    if skip_row_3away < 1.0:
        skip_top = [1, 4, 13,16] 
        skip_bot = [12,9, 24,21] 
        for ix, x in enumerate(skip_top):
            y = skip_bot[ix]
            T[x-1, y-1] *= skip_row_3away
            T[y-1, x-1] *= skip_row_3away

    Flow24x24 = T

    # Normalize matrix with min-max scaling to a range with maximum = 1:
    newMin = np.min(Flow24x24) / np.max(Flow24x24)
    newMax = 1.0
    Flow24x24 = newMin + (Flow24x24 - np.min(Flow24x24)) * (newMax - newMin) / (np.max(Flow24x24) - np.min(Flow24x24))

    return Flow24x24

Flow24x24 = create_24x24_flow_matrix(not_home_row, side_top, 
    side_above_3away, side_above_2away, side_above_1away, middle_above_ring, ring_above_middle, outward, 
    skip_row_3away, skip_row_2away, skip_row_1away, skip_row_0away, same_finger, lateral, same_hand, 
    shorter_above, adjacent_offset, inside_top, index_above)

# Print:
print_matrix_info(matrix_data=Flow24x24, matrix_label="Flow24x24", nkeys=24, nlines=30)
heatmap(data=Flow24x24, title="Flow24x24", xlabel="Key 1", ylabel="Key 2", print_output=print_output)


def create_32x32_flow_matrix(not_home_row, side_top, side_above_3away, side_above_2away, side_above_1away, 
                             middle_above_ring, ring_above_middle, outward, skip_row_3away, 
                             skip_row_2away, skip_row_1away, skip_row_0away, same_finger, lateral, 
                             same_hand, shorter_above, adjacent_offset, inside_top, index_above):

    all_32_keys = [1,2,3,4, 5,6,7,8, 9,10,11,12, 13,14,15,16, 17,18,19,20, 21,22,23,24, 
                   25,26,27, 28,29,30, 31,32]

    # Create a matrix and multiply by flow factors that promote easy interkey transitions:
    T = np.ones((32, 32))

    if lateral < 1.0:
        for x in all_32_keys:
            for y in [25,26,27, 28,29,30, 31,32]:
                T[x-1, y-1] *= lateral
                T[y-1, x-1] *= lateral    

    # 7.  Promote alternating between hands over uncomfortable transitions with the same hand.
    if same_hand < 1.0:
        for i in [1,2,3,4,5,6,7,8,9,10,11,12, 25,26,27]:
            for j in [1,2,3,4,5,6,7,8,9,10,11,12, 25,26,27]:
                T[i-1,j-1] *= same_hand
        for i in [13,14,15,16,17,18,19,20,21,22,23,24, 28,29,30,31,32]:
            for j in [13,14,15,16,17,18,19,20,21,22,23,24, 28,29,30,31,32]:
                T[i-1,j-1] *= same_hand

    # 8.  Promote little-to-index-finger roll-ins over index-to-little-finger outsward rolls.
    # Penalize (index, little) finger lateral movements:
    #  1  2  3  4 25   28 13 14 15 16 31 
    #  5  6  7  8 26   29 17 18 19 20 32
    #  9 10 11 12 27   30 21 22 23 24
    if outward < 1.0:

        # same-row roll-outs:
        roll_ins = [[1,2],[2,3],[3,4], [5,6],[6,7],[7,8], [9,10],[10,11],[11,12],
                    [16,15],[15,14],[14,13], [20,19],[19,18],[18,17], [24,23],[23,22],[22,21]]
        for x in roll_ins:
            T[x[1]-1, x[0]-1] *= outward

        # same-row roll-outs, skipping keys:
        roll_ins_skip_keys = [[1,3],[2,4],[1,4], [5,7],[6,8],[5,8], [9,11],[10,12],[9,12],
                              [16,14],[15,13],[16,13], [20,18],[19,17],[20,17], [24,22],[23,21],[24,21]]
                              #[1,25],[2,25],[3,25],
                              #[5,26],[6,26],[7,26],
                              #[9,27],[10,27],[11,27],
                              #[16,28],[15,28],[14,28],
                              #[20,29],[19,29],[18,29],
                              #[24,30],[23,30],[22,30],
                              #[31,15],[31,14],[31,13],[31,28],
                              #[32,19],[32,18],[32,17],[32,29]]
        for x in roll_ins_skip_keys:
            T[x[1]-1, x[0]-1] *= outward

        # adjacent-row roll-outs:
        #  1  2  3  4 25   28 13 14 15 16 31 
        #  5  6  7  8 26   29 17 18 19 20 32
        #  9 10 11 12 27   30 21 22 23 24
        roll_ins_adj_rows = [[1,6],[1,7],[1,8],[2,7],[2,8],[3,8], 
                             [5,2],[5,3],[5,4],[6,3],[6,4],[7,4],
                             [5,10],[5,11],[5,12],[6,11],[6,12],[7,12], 
                             [9,6],[9,7],[9,8],[10,7],[10,8],[11,8],
                             [16,19],[16,18],[16,17],[15,18],[15,17],[14,17], 
                             [20,15],[20,14],[20,13],[19,14],[19,13],[18,13],
                             [20,23],[20,22],[20,21],[19,22],[19,21],[18,21], 
                             [24,19],[24,18],[24,17],[23,18],[23,17],[22,17]]
                             #[5,25],[6,25],[7,25],[8,25],
                             #[5,27],[6,27],[7,27],[8,27],
                             #[1,26],[2,26],[3,26],[4,26],
                             #[9,26],[10,26],[11,26],[12,26],
                             #[16,29],[15,29],[14,29],[13,29],
                             #[24,29],[23,29],[22,29],[21,29],
                             #[20,28],[19,28],[18,28],[17,28],
                             #[20,30],[19,30],[18,30],[17,30],
                             #[31,20],[31,19],[31,18],[31,17],[31,29],
                             #[32,16],[32,15],[32,14],[32,13],[32,28],
                             #[32,24],[32,23],[32,22],[32,21],[32,30]]
        for x in roll_ins_adj_rows:
            T[x[1]-1, x[0]-1] *= outward

        # upper<->lower row roll-outs:
        roll_ins_skip_home = [[1,10],[1,11],[1,12],[2,11],[2,12],[3,12],
                              [9,2],[9,3],[9,4],[10,3],[10,4],[11,4],
                              [16,23],[16,22],[16,21],[15,22],[15,21],[14,21],
                              [24,15],[24,14],[24,13],[23,14],[23,13],[22,13]]
                              #[16,30],[15,30],[14,30],[13,30],
                              #[9,25],[10,25],[11,25],[12,25],
                              #[24,28],[23,28],[22,28],[21,28],
                              #[1,27],[2,27],[3,27],[4,27], 
                              #[31,24],[31,23],[31,22],[31,21],[31,30]]
        for x in roll_ins_skip_home:
            T[x[1]-1, x[0]-1] *= outward

    # 9.  Avoid stretching shorter fingers up and longer fingers down.
    #  1  2  3  4 25   28 13 14 15 16 31 
    #  5  6  7  8 26   29 17 18 19 20 32
    #  9 10 11 12 27   30 21 22 23 24
    if index_above < 1.0:
        for x in [4]:
            for y in [4,5,6,7,8,26,9,10,11,12,27,28,13,14,15,16,31,29,17,18,19,20,32,30,21,22,23,24]:
                T[x-1, y-1] *= index_above
                T[y-1, x-1] *= index_above
        for x in [25]:
            for y in [25,5,6,7,8,26,9,10,11,12,27,28,13,14,15,16,31,29,17,18,19,20,32,30,21,22,23,24]:
                T[x-1, y-1] *= index_above
                T[y-1, x-1] *= index_above
        for x in [13]:
            for y in [1,2,3,4,25,5,6,7,8,26,9,10,11,12,27,13,29,17,18,19,20,32,30,21,22,23,24]:
                T[x-1, y-1] *= index_above
                T[y-1, x-1] *= index_above
        for x in [28]:
            for y in [1,2,3,4,25,5,6,7,8,26,9,10,11,12,27,28,29,17,18,19,20,32,30,21,22,23,24]:
                T[x-1, y-1] *= index_above
                T[y-1, x-1] *= index_above
    if inside_top < 1.0:
        for x in [4,25,28,13]:
            for j in range(0,32):
                T[x-1, j] *= inside_top
                T[j, x-1] *= inside_top
    if side_top < 1.0:
        for x in [1,4,25,28,13,16,31]:
            for j in range(0,32):
                T[x-1, j] *= side_top
                T[j, x-1] *= side_top
    if side_above_1away < 1.0:
        for x in [1]:
            for y in [6,10]:
                T[x-1, y-1] *= side_above_1away
                T[y-1, x-1] *= side_above_1away
        for x in [5]:
            for y in [10]:
                T[x-1, y-1] *= side_above_1away
                T[y-1, x-1] *= side_above_1away
        for x in [4,25]:
            for y in [7,11]:
                T[x-1, y-1] *= side_above_1away
                T[y-1, x-1] *= side_above_1away
        for x in [8,26]:
            for y in [11]:
                T[x-1, y-1] *= side_above_1away
                T[y-1, x-1] *= side_above_1away
        for x in [13,28]:
            for y in [18,22]:
                T[x-1, y-1] *= side_above_1away
                T[y-1, x-1] *= side_above_1away
        for x in [17,29]:
            for y in [22]:
                T[x-1, y-1] *= side_above_1away
                T[y-1, x-1] *= side_above_1away
        for x in [16,31]:
            for y in [19,23]:
                T[x-1, y-1] *= side_above_1away
                T[y-1, x-1] *= side_above_1away
        for x in [20,32]:
            for y in [23]:
                T[x-1, y-1] *= side_above_1away
                T[y-1, x-1] *= side_above_1away
    if side_above_2away < 1.0:
        for x in [1]:
            for y in [7,11]:
                T[x-1, y-1] *= side_above_2away
                T[y-1, x-1] *= side_above_2away
        for x in [5]:
            for y in [11]:
                T[x-1, y-1] *= side_above_2away
                T[y-1, x-1] *= side_above_2away
        for x in [4,25]:
            for y in [6,10]:
                T[x-1, y-1] *= side_above_2away
                T[y-1, x-1] *= side_above_2away
        for x in [8,26]:
            for y in [10]:
                T[x-1, y-1] *= side_above_2away
                T[y-1, x-1] *= side_above_2away
        for x in [13,28]:
            for y in [19,23]:
                T[x-1, y-1] *= side_above_2away
                T[y-1, x-1] *= side_above_2away
        for x in [17,29]:
            for y in [23]:
                T[x-1, y-1] *= side_above_2away
                T[y-1, x-1] *= side_above_2away
        for x in [16,31]:
            for y in [18,22]:
                T[x-1, y-1] *= side_above_2away
                T[y-1, x-1] *= side_above_2away
        for x in [20,32]:
            for y in [22]:
                T[x-1, y-1] *= side_above_2away
                T[y-1, x-1] *= side_above_2away
    if side_above_3away < 1.0:
        for x in [1]:
            for y in [8,12,26,27]:
                T[x-1, y-1] *= side_above_3away
                T[y-1, x-1] *= side_above_3away
        for x in [5]:
            for y in [12,27]:
                T[x-1, y-1] *= side_above_3away
                T[y-1, x-1] *= side_above_3away
        for x in [4,25]:
            for y in [5,9]:
                T[x-1, y-1] *= side_above_3away
                T[y-1, x-1] *= side_above_3away
        for x in [8,26]:
            for y in [9]:
                T[x-1, y-1] *= side_above_3away
                T[y-1, x-1] *= side_above_3away
        for x in [13,28]:
            for y in [20,24,32]:
                T[x-1, y-1] *= side_above_3away
                T[y-1, x-1] *= side_above_3away
        for x in [17,29]:
            for y in [24]:
                T[x-1, y-1] *= side_above_3away
                T[y-1, x-1] *= side_above_3away
        for x in [16,31]:
            for y in [17,21,29,30]:
                T[x-1, y-1] *= side_above_3away
                T[y-1, x-1] *= side_above_3away
        for x in [20,32]:
            for y in [21,30]:
                T[x-1, y-1] *= side_above_3away
                T[y-1, x-1] *= side_above_3away


    #  1  2  3  4 25   28 13 14 15 16 31 
    #  5  6  7  8 26   29 17 18 19 20 32
    #  9 10 11 12 27   30 21 22 23 24
    if shorter_above < 1.0:
        for x in [1]:
            for y in [6,7,8,26,10,11,12,27]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [2]:
            for y in [7,11]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [4]:
            for y in [6,7,10,11]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [25]:
            for y in [6,7,10,11]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above

        for x in [5]:
            for y in [10,11,12,27]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [6]:
            for y in [11]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [8]:
            for y in [10,11]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [26]:
            for y in [10,11]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above

        for x in [16]:
            for y in [29,17,18,19,30,21,22,23]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [31]:
            for y in [29,17,18,19,30,21,22,23]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [15]:
            for y in [18,22]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [13]:
            for y in [18,19,22,23]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [28]:
            for y in [18,19,22,23]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above

        for x in [20]:
            for y in [30,21,22,23]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [32]:
            for y in [30,21,22,23]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [19]:
            for y in [22]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [17]:
            for y in [22,23]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above
        for x in [29]:
            for y in [22,23]:
                T[x-1, y-1] *= shorter_above
                T[y-1, x-1] *= shorter_above

    if ring_above_middle < 1.0:
        ring_above_middles =  [[2,7],[6,11],[2,11],
                            [15,18],[19,22],[15,22]]
        for x in ring_above_middles:
            T[x[0]-1, x[1]-1] *= ring_above_middle
            T[x[1]-1, x[0]-1] *= ring_above_middle

    if middle_above_ring < 1.0:
        middle_above_rings =  [[6,3],[10,7],[10,3],
                            [19,14],[23,18],[23,14]]
        for x in middle_above_rings:
            T[x[0]-1, x[1]-1] *= middle_above_ring
            T[x[1]-1, x[0]-1] *= middle_above_ring

    # 10. Avoid using the same finger.
    #  1  2  3  4 25   28 13 14 15 16 31 
    #  5  6  7  8 26   29 17 18 19 20 32
    #  9 10 11 12 27   30 21 22 23 24
    if same_finger < 1.0:
        same_fingers = [[1,5],[5,9],[1,9], [2,6],[6,10],[2,10], 
                        [3,7],[7,11],[3,11], [4,8],[8,12],[4,12],
                        [25,26],[26,27],[25,27], [28,29],[29,30],[28,30], [31,32],
                        [4,25],[4,26],[4,27], [8,25],[8,26],[8,27], [12,25],[12,26],[12,27],
                        [13,28],[13,29],[13,30], [17,28],[17,29],[17,30], [21,28],[21,29],[21,30],
                        [31,16],[31,20],[31,24], [32,16],[32,20],[32,24],
                        [13,17],[17,21],[13,21], [14,18],[18,22],[14,22], 
                        [15,19],[19,23],[15,23], [16,20],[20,24],[16,24]] 
        for x in same_fingers:
            T[x[0]-1, x[1]-1] *= same_finger
            T[x[1]-1, x[0]-1] *= same_finger

    # 11. Avoid the upper and lower rows.
    if not_home_row < 1.0:
        not_home_row_keys = [1,2,3,4,25, 9,10,11,12,27, 28,13,14,15,16,31, 30,21,22,23,24]
        for x in not_home_row_keys:
            for j in range(0,32):
                T[x-1, j] *= not_home_row
                T[j, x-1] *= not_home_row
                
    # 12. Avoid skipping over the home row.
    #  1  2  3  4 25   28 13 14 15 16 31 
    #  5  6  7  8 26   29 17 18 19 20 32
    #  9 10 11 12 27   30 21 22 23 24
    if skip_row_0away < 1.0:
        skip_top = [1, 2, 3, 4, 4,25,25, 28,28,13,13,14,15,16,31] 
        skip_bot = [9,10,11,12,27,12,27, 30,21,30,21,22,23,24,24] 
        for ix, x in enumerate(skip_top):
            y = skip_bot[ix]
            T[x-1, y-1] *= skip_row_0away
            T[y-1, x-1] *= skip_row_0away
    if skip_row_1away < 1.0:
        skip_top = [1, 2, 2, 3, 3, 4, 4,25, 28,13,13,14,14,15,15,16,31] 
        skip_bot = [10,9,11,10,12,11,27,11, 22,30,22,21,23,22,24,23,23] 
        for ix, x in enumerate(skip_top):
            y = skip_bot[ix]
            T[x-1, y-1] *= skip_row_1away
            T[y-1, x-1] *= skip_row_1away
    if skip_row_2away < 1.0:
        skip_top = [1,  2,3, 4,25, 28,13,14,15,16,31] 
        skip_bot = [11,12,9,10,10, 23,23,24,21,22,22] 
        for ix, x in enumerate(skip_top):
            y = skip_bot[ix]
            T[x-1, y-1] *= skip_row_2away
            T[y-1, x-1] *= skip_row_2away
    if skip_row_3away < 1.0:
        skip_top = [1, 4,25, 28,13,16,16,31,31] 
        skip_bot = [12,9, 9, 24,24,21,30,21,30] 
        for ix, x in enumerate(skip_top):
            y = skip_bot[ix]
            T[x-1, y-1] *= skip_row_3away
            T[y-1, x-1] *= skip_row_3away
                
    Flow32x32 = T

    # Normalize matrix with min-max scaling to a range with maximum = 1:
    newMin = np.min(Flow32x32) / np.max(Flow32x32)
    newMax = 1.0
    Flow32x32 = newMin + (Flow32x32 - np.min(Flow32x32)) * (newMax - newMin) / (np.max(Flow32x32) - np.min(Flow32x32))

    return Flow32x32

Flow32x32 = create_32x32_flow_matrix(not_home_row, side_top, 
    side_above_3away, side_above_2away, side_above_1away, middle_above_ring, ring_above_middle, outward, 
    skip_row_3away, skip_row_2away, skip_row_1away, skip_row_0away, same_finger, lateral, same_hand, 
    shorter_above, adjacent_offset, inside_top, index_above)

# Print:
print_matrix_info(matrix_data=Flow32x32, matrix_label="Flow32x32", nkeys=32, nlines=30)
heatmap(data=Flow32x32, title="Flow32x32", xlabel="Key 1", ylabel="Key 2", print_output=print_output)
