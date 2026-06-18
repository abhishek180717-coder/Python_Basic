import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#You feed it a mean and standard deviation, and it can answer any probability question

#Normal Distribution - the bell curve
#Normal Distribution with mean 165cm and standard deviation 7cm
mean_h, std_h = 165, 7

#Probability of being taller than 175cm
prob = 1 - norm.cdf(175, mean_h, std_h)
print(f'P(height > 175cm) = {prob:.4f} = {prob*100:.1f}%')

#The 68-95-99.7 Rule
print(f'68% of people: {mean_h-std_h:.0f}cm to {mean_h+std_h:.0f}cm')
print(f'95% of people: {mean_h-2*std_h:.0f}cm to {mean_h+2*std_h:.0f}cm')
print(f'99.7% of people: {mean_h-3*std_h:.0f}cm to {mean_h+3*std_h:.0f}cm')