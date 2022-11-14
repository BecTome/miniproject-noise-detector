def first_idx_rec(seq, arr, m, n):
    # Base Cases
    if m == 0:
        return n
    if n == 0:
        return False
 
    # If last characters of two
    # strings are matching
    if seq[m-1] == arr[n-1]:
        return first_idx_rec(seq, arr, m-1, n-1)
 
    # If last characters are not matching
    return first_idx_rec(seq, arr, m, n-1)

import numpy as np
import sys

N_SAMPLE = 20_000
N_SUBSAMPLE = 200

sys.setrecursionlimit(10000000)

np.random.seed(0)
X1 = sorted(np.random.randn(N_SAMPLE) * 10 + 10)
X2 = sorted(np.random.choice(X1, N_SUBSAMPLE))

import time
tic = time.perf_counter()
first_idx_rec(X2, X1, len(X2), len(X1))
toc = time.perf_counter()

print(toc - tic)