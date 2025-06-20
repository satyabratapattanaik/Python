# numpy definition

import numpy as np

climate_data = np.array([84, 63, 38])
weight = np.array([0.3, 0.2, 0.5])

apple_yield = np.dot(climate_data, weight)
print(apple_yield)