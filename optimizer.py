import itertools
#from data import traveltimes, populations


def overlap(a1, a2, a3=None):
    '''
    Calculates overlap between ambulances
    '''
    if a3 is not None:
        return 0
    pass


def reach(a1):
    '''
    Calculates reach of a single ambulance
    '''
    pass

maxreach = 0
optimal = (0, 1, 2)
for a1, a2, a3 in itertools.combinations(xrange(6), 3):
    reach = (reach(a1) + reach(a2) + reach(a3) -
             overlap(a1, a2) - overlap(a1, a3) - overlap(a2, a3) +
             overlap(a1, a2, a3))
    if reach > maxreach:
        optimal = (a1, a2, a3)
