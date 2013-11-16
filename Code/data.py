import numpy as np

'''
avg. travel times from sector to sector.
traveltimes[i, j] is travel time from sector i to sector j.
0-indexed, so watch out!
'''
traveltimes = np.array([[1, 8, 12, 14, 10, 16],
                        [8, 1, 6, 18, 16, 16],
                        [12, 18, 1.5, 12, 6, 4],
                        [16, 14, 4, 1, 16, 12],
                        [18, 16, 10, 4, 2, 2],
                        [16, 18, 4, 12, 2, 2]])

'''
Populations of each sector.
0-indexed, watch out!
'''
populations = np.array((5e4, 8e4, 3e4, 5.5e4, 3.5e4, 2e4))
