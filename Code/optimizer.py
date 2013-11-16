import numpy as np
import sympy as sp
from sympy import Function, integrate
import itertools
from data import traveltimes, populations

NODES = 6  # number of nodes to care about
MAX_TIME = 8  # maximum allotted time to cover a destination
zz_coverage = np.zeros((NODES, NODES))

a, x, s, t = sp.symbols('a, x, s, t')


# Probability/population distribution curves.
class quad_curve(Function):
    nargs = 2

    @classmethod
    def eval(cls, a, x):
        return -(12.0 / 11 / a) * x ** 2 / a ** 2 + (12.0 / 11 / a)


class const_curve(Function):
    nargs = 2

    @classmethod
    def eval(cls, a, x):
        return 1 / a

PROB_CURVE = const_curve  # selected model for population distribution

expected_value = integrate(integrate(PROB_CURVE(a, t) * PROB_CURVE(a, t - s),
                                     (t, -a / 2, a / 2)) * s, (s, 0, a))
# integral that should equal t_bbp


def calc_cover(start, target):
    '''
    Calculates coverage of a single ambulance for a zone.
    '''
    t_bb = traveltimes[target, target]
    t_ab = traveltimes[start, target]
    t_ba = traveltimes[target, start]
    t_bbp = 2 * t_bb / (1 + t_ab / t_ba)
    b = sp.solve(expected_value - t_bbp)[0]
    b_start = -b / 2
    b_end = min(b / 2, MAX_TIME - t_ab)
    if b_start > b_end:
        return 0
    return int(integrate(PROB_CURVE(b, t), (t, b_start, b_end)) *
               populations[target] + 0.5)


for i in xrange(NODES):
    for j in xrange(NODES):
        zz_coverage[i, j] = calc_cover(i, j)


def greedyoptimize(nambulances):
    '''
    Optimize ambulance placement using a greedy algorithm.
    Selects additional ambulances locations based on how
    many additional people it would cover.
    '''
    covered = np.zeros(NODES)
    startnodes = []
    for i in xrange(nambulances):
        maxcoverage = 0
        bestnode = 0
        for start in xrange(NODES):
            if start in startnodes:
                continue  # don't duplicate zones
            coverage = 0
            for target in xrange(NODES):
                # additional coverage will increase the coverage to,
                # at most the population of the zone
                coverage += min(zz_coverage[start, target],
                                populations[target] - covered[target])
            if coverage > maxcoverage:
                maxcoverage = coverage
                bestnode = start
        startnodes.append(bestnode)
        for target in xrange(NODES):
            covered[target] += min(zz_coverage[bestnode, target],
                                   populations[target] - covered[target])
    return ([i + 1 for i in startnodes], covered)  # change 0 to 1-indexing


def bruteforce(nambulances):
    '''
    Takes all possible combinations of nambulances from NODES,
    and arranges them so that there is maximum coverage among zones.
    '''
    maxcoverage = np.zeros(NODES)
    for startingnodes in itertools.combinations(xrange(NODES),
                                                nambulances):
        covered = np.zeros(NODES)
        for target in xrange(NODES):
            for start in startingnodes:
                covered[target] += min(zz_coverage[start, target],
                                       populations[target] - covered[target])
        if np.sum(covered) > np.sum(maxcoverage):
            optimal = startingnodes
            maxcoverage = covered
    return ([i + 1 for i in optimal], maxcoverage)  # change 0 to 1-indexing
