# CS454 Assignment 2: Local Search for Next Release Problem

The aim of this assignment is to understand and implement basic genetic algorithm, as well as the multi-objective evolutionary algorithm. 
## Next Release Problem

Suppose you have $N$ candidate features for the next version of your software product, $F = \{f_1, \ldots, f_N\}$. Each feature $f_i$ has both cost $cost(f_i)$ and value $value(f_i)$. Given budget $B$, Next Release Problem is to find the subset of $F$, $F_R$, such that maximizes $\sum_{f_i\in F_R}{value(f_i)}$ while subject to $\sum_{f_i\in F_R}{cost(f_i)} \leq B$.

## Skeleton Code

The repository contains `nrp.py`, which provides a few utility functions as well as the following types to structure your solers around:

- `Feature = TypedDict("Feature", {"cost":int, "value":int})`: a structure that stores cost and value of an individual feature
- `FeatureSet = TypedDict("FeatureSet", {"id":int, "feature":Feature})`: a collection of individual features
- `class Solution`: a representation of a candidate solution that you can use to write your solvers with

It also contains `gen_features(n)` function, which will create a random Next Release Problem instance. Refer to the implementation to understand the instances, but please use the `nrp_100.csv` that is included in the repository for evaluation. It contains 100 features with random costs and values.

A solver is a function (based on a specific algorithm) in the form of `solver(features:FeatureSet, budget:int)`. As an output, return the solution found in the type of `class Solution`. 

The skeleton can be used as follows:

```
budget = 5000
features = read_data("nrp_100.csv")
sol = steepest_hc(features, budget) # steepest hill climbing
print(sol)
```

## Subtask 1: Greedy Heuristic Solver

Implement two types of greedy solvers. The first one is pure greedy, i.e., it will add the feature with the highest value as long as the total cost does not go beyond thd budget. Implement this in `greedy.py`. The second one is additional greedy, i.e., it will add the features with the highest value per cost ratio as long as the total cost does not go beyond the budget. Implement this in `additional_greedy.py`.

## Subtask 2: Genetic Algorithm

Implement a single objective genetic algorithm for the NRP problem. The objective is to maximize the sum of values of the chosen items, while staying below the given budget constraint. Name your solver as `single_ga.py`

## Subtask 3: Multi-Objective Evolutionary Algorithm

Implement the final solver, which is multi-objective. Your goal is to maximize the sum of the cost of chosen items, while minimizing the cost of the chosen items. Try to tune the parameters so that your solver performs well against the others you have implemented. This should be in `multi_ga.py`.

## Report

Write, and commit a simple report detailing your implementations, and include it as a PDF file in the repository. In particular, try to discuss the following point:

- Between greedy, single-objective GA, and multi-objective GA, what differences did you find among the final solution? Why?