# Load inter-key timings table. Save Time32x32 and Time24x24 arrays in data/ files.

load_original_interkey_timings_table = False
if load_original_interkey_timings_table:

    interkey_table = "data/interkey-timings.xlsx"
    wb = xlrd.open_workbook(interkey_table) 
    interkey_sheet = wb.sheet_by_index(0)

    # Convert interkey stroke times table to array:
    Time32x32_original = np.zeros((32,32))
    for i in range(1,33):
        for j in range(1,33):
            if interkey_sheet.cell_value(i,j):
                Time32x32_original[i-1,j-1] = interkey_sheet.cell_value(i,j)

    # Fill empty (symmetric) portion of the array:
    for i in range(1,33):
        for j in range(1,33):
            if interkey_sheet.cell_value(i,j):
                Time32x32_original[j-1,i-1] = interkey_sheet.cell_value(i,j)

    # Extract pairwise entries for the 32 vertical range keys:
    #        Left:            Right:
    #    1  2  3  4 25   28 13 14 15 16 31 
    #    5  6  7  8 26   29 17 18 19 20 32
    #    9 10 11 12 27   30 21 22 23 24
    # A. Iseri, M. Eksioglu / International Journal of Industrial Ergonomics 48 (2015) 127e138
    #        Left:            Right:
    #    1  4  7 10 13   16 19 22 25 28 30 32 
    #    2  5  8 11 14   17 20 23 26 29 31
    #    3  6  9 12 15   18 21 24 27
    table_32_positions = [1,4,7,10, 2,5,8,11, 3,6,9,12,  
                          19,22,25,28, 20,23,26,29, 21,24,27,31,
                          13,14,15, 16,17,18, 30,32]
    Time32x32 = np.zeros((32, 32))
    u = 0
    for i in table_32_positions:
        u += 1
        v = 0
        for j in table_32_positions:
            v += 1
            Time32x32[u-1,v-1] = Time32x32_original[i-1,j-1]
    
    # Extract pairwise entries for the 24 vertical range keys:
    table_24_positions = [1,4,7,10, 2,5,8,11, 3,6,9,12,  19,22,25,28, 20,23,26,29, 21,24,27,31]
    Time24x24 = np.zeros((24, 24))
    u = 0
    for i in table_24_positions:
        u += 1
        v = 0
        for j in table_24_positions:
            v += 1
            Time24x24[u-1,v-1] = Time32x32[i-1,j-1]
    
    # Print:
    for times in Time32x32:
        times = [np.str(np.int(x)) for x in times]
        print('[{0}],'.format(','.join(times)))
    print()
    for times in Time24x24:
        times = [np.str(np.int(x)) for x in times]
        print('[{0}],'.format(','.join(times)))