"""
Module imports demonstration.
Shows various ways to import modules in Python:
- Importing entire modules
- Importing specific functions from modules
- Aliasing modules
- Importing custom packages
"""

import math

# Importing and using entire module
print(math.sqrt(16))
print(math.pi)

# Importing specific functions from module
from math import sqrt, pi

print(sqrt(64))
print(pi)

# Importing numpy module with alias
import numpy as np

print(np.array([1, 2, 3, 4, 5]))

# Importing custom made package
from package import maths

print(maths.addition(3, 4))
print(maths.substraction(4, 3))
