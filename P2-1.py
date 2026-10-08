import numpy as np
from scipy import constants as const

k = 10
T1 = 25 + 273.15
T2 = 47+ 273.15
R = const.R

Ea = -R * np.log(k) / (1/T2 - 1/T1)
print("活性化エネルギー:", Ea, "J/mol")