import numpy as np
import sympy as sp
from sympy import Function, integrate
import itertools
from data import traveltimes, populations

NODES = 6
reaches = np.zeros((NODES, NODES))

a, x, s, t = sp.symbols('a, x, s, t')


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


class gauss_curve(Function):
    nargs = 2

    @classmethod
    def eval(cls, a, x):
        return 0  # TODO

PROB_CURVE = quad_curve
MAX_TIME = 8

expected_value = integrate(integrate(PROB_CURVE(a, t) * PROB_CURVE(a, t - s),
                                     (t, -a / 2, a / 2)) * s,
                           (s, 0, a))


def reach(start, target):
    '''
    Calculates reach of a single ambulance for a district
    '''
    #taa = traveltimes[start, start]
    tbb = traveltimes[target, target]
    tab = traveltimes[start, target]
    tba = traveltimes[target, start]
    #taam = 2 * taa / (1 + tba / tab)
    tbbp = 2 * tbb / (1 + tab / tba)
    #wa = sp.solve(expected_value - taam)[0]
    wb = sp.solve(expected_value - tbbp)[0]
    bstart = -wb / 2
    bend = MAX_TIME - tab
    if bstart > bend:
        return 0
    return round(integrate(PROB_CURVE(wb, t), (t, bstart, bend)) * populations(target))


def calcreaches():
    for i in xrange(NODES):
        for j in xrange(NODES):
            reaches[i, j] = reach(i, j)


def greedyoptimize(nambulances):
    reached = np.zeros(NODES)
    startnodes = np.empty(nambulances)
    for i in xrange(nambulances):
        maxreach = 0
        bestnode = 0
        for start in xrange(NODES):
            reach = 0
            for target in xrange(NODES):
                reach += min(reaches[start, target], populations[target] - reached[target])
            if reach > maxreach:
                maxreach = reach
                bestnode = start
        startnodes[i] = bestnode
        for target in xrange(NODES):
            reached[target] += min(reaches[start, target], populations[target] - reached[target])
    return (startnodes, reached)


def bruteforce(nambulances):
    maxreach = 0
    for startingnodes in itertools.combinations(xrange(NODES), nambulances):
        totalreach = 0
        for i in xrange(NODES):
            totalreach += min(populations[i], sum([reaches[a, i] for a in startingnodes]))
        if totalreach > maxreach:
            optimal = startingnodes
    return optimal
