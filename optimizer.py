import numpy as np
import itertools
from data import traveltimes, populations

NODES = 6
reaches = np.zeros((NODES, NODES))


def reach(start, target):
    '''
    Calculates reach of a single ambulance for a district
    '''
    pass


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
