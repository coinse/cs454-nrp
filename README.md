# CS454 Assignment 1: Local Search for Next Relaese Problem

The aim of this assignment is to understand and implement basic local search algorithms: greedy heuristic, variants of hill climbing (first ascent, steepest ascent, and random ascent), as well as simulated annealing. 

## Next Release Problem

Suppose you have $N$ candidate features for the next version of your software product, $F = \{f_1, \ldots, f_N\}$. Each feature $f_i$ has both cost $cost(f_i)$ and value $value(f_i)$. Given budget $B$, Next Release Problem is to find the subset of $F$, $F_R$, such that maximizes $\sum_{f_i\in F_R}{value(f_i)}$ while subject to $\sum_{f_i\in F_R}{cost(f_i)} \leq B$.

## Skeleton Code

The repository contains `nrp.py`, which provides a few utility functions as well as the class `Solution` that you can use to write solvers. 