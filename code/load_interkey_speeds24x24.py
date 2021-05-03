# Left/right symmetric version of the Time24x24 matrix
# (The original version was constructed with data from right-handed people.)
# A. Iseri, M. Eksioglu / International Journal of Industrial Ergonomics 48 (2015) 127e138

#        Left:            Right:
#     1  2  3  4       13 14 15 16 
#     5  6  7  8       17 18 19 20
#     9 10 11 12       21 22 23 24

I = [ 1, 2, 3, 4,   5, 6, 7, 8,   9,10,11,12,  16,15,14,13,  20,19,18,17,  24,23,22,21]
J = [16,15,14,13,  20,19,18,17,  24,23,22,21,   1, 2, 3, 4,   5, 6, 7, 8,   9,10,11,12]

TimeSymmetric24x24 = np.ones((24,24))
for i1, I1 in enumerate(I):
    for i2, I2 in enumerate(I):
        J1 = J[i1] - 1
        J2 = J[i2] - 1
        avgvalue = (Time24x24[I1-1,I2-1] + Time24x24[J1,J2]) / 2 
        #print(Time24x24[I1-1,I2-1], Time24x24[J1,J2], avgvalue)
        TimeSymmetric24x24[I1-1,I2-1] = avgvalue
        TimeSymmetric24x24[J1,J2] = avgvalue

# Normalize matrix with min-max scaling to a range with maximum = 1:
newMin = np.min(Time24x24) / np.max(Time24x24)
newMax = 1.0
Time24x24 = newMin + (Time24x24 - np.min(Time24x24)) * (newMax - newMin) / (np.max(Time24x24) - np.min(Time24x24))

# Convert relative interkey stroke times to relative speeds by subtracting from 1:
Speed24x24 = 1 - Time24x24 + np.min(Time24x24)

# Normalize matrix with min-max scaling to a range with maximum = 1:
newMin = np.min(TimeSymmetric24x24) / np.max(TimeSymmetric24x24)
newMax = 1.0
TimeSymmetric24x24 = newMin + (TimeSymmetric24x24 - np.min(TimeSymmetric24x24)) * (newMax - newMin) / (np.max(TimeSymmetric24x24) - np.min(TimeSymmetric24x24))

# Convert relative interkey stroke times to relative speeds by subtracting from 1:
SpeedSymmetric24x24 = 1 - TimeSymmetric24x24 + np.min(TimeSymmetric24x24)

# Print:
#print_matrix_info(matrix_data=Speed24x24, matrix_label="Speed24x24", nkeys=24, nlines=50)
#heatmap(data=Speed24x24, title="Speed24x24", xlabel="Key 1", ylabel="Key 2", print_output=print_output)