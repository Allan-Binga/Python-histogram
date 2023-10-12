import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(500, 5)

plt.hist2d(data[:,0], data[:,1], bins=20)

plt.colorbar()

plt.show()