# %load code/engram_variables.py
# Print .png figures and .txt text files
print_output = False # True

# Apply strength data
apply_strength = True
min_strength_factor = 0.9

letters24 = ['E','T','A','O','I','N','S','R','H','L','D','C','U','M','F','P','G','W','Y','B','V','K','X','J']
keys24 = [1,2,3,4, 5,6,7,8, 9,10,11,12, 13,14,15,16, 17,18,19,20, 21,22,23,24]
instances24 = [4.45155E+11,3.30535E+11,2.86527E+11,2.72277E+11,2.69732E+11,2.57771E+11,
               2.32083E+11,2.23768E+11,1.80075E+11,1.44999E+11,1.36018E+11,1.19156E+11,
               97273082907,89506734085,85635440629,76112599849,66615316232,59712390260,
               59331661972,52905544693,37532682260,19261229433,8369138754,5657910830]                        


# Establish which layouts are within a small difference of the top-scoring layout 
# (the smallest difference between two penalties, 0.9^8 - 0.9^9, in one of 24^2 key pairs):
delta = 0.9**8 - 0.9**9
factor24 = ((24**2 - 1) + (1-delta)) / (24**2)
factor32 = ((32**2 - 1) + (1-delta)) / (32**2)

# Establish which layouts are within a small difference of each other when using the speed matrix. 
# We define an epsilon equal to 13.158 ms for a single bigram (of the 32^2 possible bigrams), 
# where 13.158 ms is one tenth of 131.58 ms, the fastest measured digraph tapping speed (30,000/228 = 131.58 ms) 
# recorded in the study: "Estimation of digraph costs for keyboard layout optimization", 
# A Iseri, Ma Eksioglu, International Journal of Industrial Ergonomics, 48, 127-138, 2015.
#data_matrix_speed = Speed32x32
#time_range = 243  # milliseconds
#norm_range = np.max(data_matrix_speed) - np.min(data_matrix_speed)  # 0.6535662299854439
#ms_norm = norm_range / time_range  # 0.0026895729629030614
#epsilon = 131.58/10 * ms_norm / (32**2)
epsilon    = 0.00003549615849447514