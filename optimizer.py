import numpy as np
import itertools
from data import traveltimes, populations


def reach(start, target):
    '''
    Calculates reach of a single ambulance for a district
    '''
    pass

reaches = np.zeros((6, 6))
for i in xrange(6):
    for j in xrange(6):
        reaches[i, j] = reach(i, j)

maxreach = 0
optimal = (0, 1, 2)
for a1, a2, a3 in itertools.combinations(xrange(6), 3):
    totalreach = 0
    for i in xrange(6):
        totalreach += min(populations[i], sum([reaches[a, i] for a in (a1, a2, a3)]))
    if totalreach > maxreach:
        optimal = (a1, a2, a3)
