import numpy as np
import scipy.constants as const
p0 = 1 * const.atm
T0 = 100 + 273.15
H = 8000
vapHm = 44000
z = 8849

p = p0 * np.exp(-z / H)

t = np.log(p/p0) * const.R / vapHm
T = 1 / (1/T0 - t) 
print("エベレスト頂点での沸点は", T ,"K")