# Noisy Data Detector

The model/workflow takes two 1D sequences X1 and X2 as input. Here, `X1` will be a
continuous sequence. Note that `X2` will be a subset of `X1` with some noise and difference in sampling rate.

The goal is to build a model (any approach) that can tell the starting position of sequence `X2` in
sequence `X1`. The specifics are as follows.

1. Build a single solution that is better than the brute-force search. Here brute-force implies a simple point-by-point linear search. Coding more than one solution is not going to add any extra points. The coded solution does not have to be computationally optimal, neither does it need to be close to
optimal – just keep it better than the brute-force.

2. Think of possible approaches that could have presented the solution in a faster way. You
do not need to code these. Rather keep them documented with yourself to discuss
during the presentation.