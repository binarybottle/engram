# Left/right symmetric version of the Time32x32 matrix
# (The original version was constructed with data from right-handed people.)
# A. Iseri, M. Eksioglu / International Journal of Industrial Ergonomics 48 (2015) 127e138

#        Left:            Right:
#    1  2  3  4 25   28 13 14 15 16 31 
#    5  6  7  8 26   29 17 18 19 20 32
#    9 10 11 12 27   30 21 22 23 24

I = [ 1, 2, 3, 4,25,   5, 6, 7, 8,26,   9,10,11,12,27,  16,15,14,13,28,  20,19,18,17,29,  24,23,22,21,30]
J = [16,15,14,13,28,  20,19,18,17,29,  24,23,22,21,30,   1, 2, 3, 4,25,   5, 6, 7, 8,26,   9,10,11,12,27]

TimeSymmetric32x32 = np.ones((32,32))
for i1, I1 in enumerate(I):
    for i2, I2 in enumerate(I):
        J1 = J[i1] - 1
        J2 = J[i2] - 1
        avgvalue = (Time32x32[I1-1,I2-1] + Time32x32[J1,J2]) / 2 
        #print(Time32x32[I1-1,I2-1], Time32x32[J1,J2], avgvalue)
        TimeSymmetric32x32[I1-1,I2-1] = avgvalue
        TimeSymmetric32x32[J1,J2] = avgvalue

# Normalize matrix with min-max scaling to a range with maximum = 1:
newMin = np.min(Time32x32) / np.max(Time32x32)
newMax = 1.0
Time32x32 = newMin + (Time32x32 - np.min(Time32x32)) * (newMax - newMin) / (np.max(Time32x32) - np.min(Time32x32))

# Convert relative interkey stroke times to relative speeds by subtracting from 1:
Speed32x32 = 1 - Time32x32 + np.min(Time32x32)

# Normalize matrix with min-max scaling to a range with maximum = 1:
newMin = np.min(TimeSymmetric32x32) / np.max(TimeSymmetric32x32)
newMax = 1.0
TimeSymmetric32x32 = newMin + (TimeSymmetric32x32 - np.min(TimeSymmetric32x32)) * (newMax - newMin) / (np.max(TimeSymmetric32x32) - np.min(TimeSymmetric32x32))

# Convert relative interkey stroke times to relative speeds by subtracting from 1:
SpeedSymmetric32x32 = 1 - TimeSymmetric32x32 + np.min(TimeSymmetric32x32)

# Print:
#print_matrix_info(matrix_data=Speed32x32, matrix_label="Speed32x32", nkeys=32, nlines=50)
#heatmap(data=Speed32x32, title="Speed32x32", xlabel="Key 1", ylabel="Key 2", print_output=print_output)