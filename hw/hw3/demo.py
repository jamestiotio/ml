#!/usr/bin/env python3
# Demonstration of floating-point arithmetic underflow
# James Raphael Tiovalen / 1004555

import secrets
import math
import sys

N = 1000

print("Generating probability values for likelihood...\n")

probability_multiply_result = secrets.SystemRandom().uniform(0, 1)

for _ in range(N):
    next_probability = secrets.SystemRandom().uniform(0, 1)
    # while next_probability == 0:
    #     next_probability = secrets.SystemRandom().uniform(0, 1)
    print(next_probability)
    probability_multiply_result *= next_probability

print(f"\nFinal probability multiplication result: {probability_multiply_result}\n")

# This should fail (assuming no exactly zero probability was obtained), but it actually passes (which is wrong)!!!
assert probability_multiply_result == 0

print("Generating logarithmic values for log-likelihood...\n")

# We technically could use sys.maxsize as the upper limit, but we use math.exp(1) instead to make it as a "fair" comparison with the previous method
logarithm_sum_result = math.log(secrets.SystemRandom().uniform(1, math.exp(1)))

for _ in range(N):
    next_logarithm = math.log(secrets.SystemRandom().uniform(1, math.exp(1)))
    print(next_logarithm)
    logarithm_sum_result += next_logarithm

logarithm_sum_result /= N

print(f"\nFinal logarithmic summation/addition result: {logarithm_sum_result}\n")

# This passes, as it should!!!
assert logarithm_sum_result != 0
