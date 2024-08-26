# genetic-cache-booster
Investigating boosting genetic algorithm using cache

## Problem statement
A genetic algorithm needs to evaluate metrics related to chromosome it tries to optimize.
The time the algorithm computes these metrics can have a big impact on its performance and/or its ability to solve the problem.

Is using cache a good solution to improve a genetic algorithm performance?


### Variable design
The problem is dependent of the genetic algorithm context.

#### Computation time
The time computing the metric takes to the algorithm can be:
- deterministic: fixed to a certain value
- stochastic: randomly chosen in a given distribution each time

#### Collision probability
The probability the genetic algorithm encounters the same chromosome as before leading to the possibility to leverage the cache.
