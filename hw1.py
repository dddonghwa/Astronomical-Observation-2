import numpy as np
from astropy.stats import sigma_clipped_stats
from matplotlib import pyplot as plt

#%%
# problem 1
np.random.seed(123)
data = np.random.random(10)
## (1)
avg = np.average(data)
med = np.median(data)
std = np.std(data)
print (f"average = {avg:.3f}, median = {med:.3f}, standard deviation = {std:.3f}")

## (2)
avg, med, std = sigma_clipped_stats(data, sigma=1, iters=1)
print (f"average = {avg:.3f}, median = {med:.3f}, standard deviation = {std:.3f}")

## (3) 
eps = 10**(-10)
for i in range(6):
    avg, med, std = sigma_clipped_stats(data, sigma=1, iters=i)
    avg0, med0, std0 = sigma_clipped_stats(data, sigma=1, iters=i+1)
    if abs(avg-avg0) < eps and abs(med-med0) < eps and abs(std-std0) < eps :
        print(f"average = {avg:.3f}, median = {med:.3f}, standard deviation = {std:.3f}")
        print(f"At N_iter {i}, these three values stop to change.")
        break

#%%
# problem 2
np.random.seed(123)
data = np.random.random((10, 20))
data[:, [3, 10]] += 10

for i in [0, 3]:
    avg, med, std = sigma_clipped_stats(data, sigma=1, iters=i, axis=0)
    plt.plot(med, label=f"Niter = {i}", ls=':', marker='.')
plt.title("Median combine")
plt.grid(ls=':')
plt.legend()
