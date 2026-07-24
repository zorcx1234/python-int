"""
Numerisches Python mit numpy

pip install numpy
"""

import numpy as np

values = [1, 2, 3, 4, 5, 6]  # Python Liste mit ints
x = np.array(values)
x = x.astype(np.int8)
print("DAtentyp von x:", x.dtype)


# klassisch
new_values = []
for value in values:
    new_values.append(value + 2)

# mit numpy (Vektorisierung, SIMD)
x = x + 2
print("Ergebnis:", x)
