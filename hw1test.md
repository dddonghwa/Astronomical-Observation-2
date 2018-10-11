Homework 01
=================

우선 풀이에 필요한 library(numpy, astropy.stats, matplotlib) 속 함수를 불러온다. 
~~~
import numpy as np
from astropy.stats import sigma_clipped_stats
from matplotlib import pyplot as plt
~~~
problem # 01
-----------------
np.random.random 함수를 통해 (0,1) 사이의 값을 가지는 임의의 data (10개)를 불러 온다.
여기서 random seed()는 불러온 데이터를 저장할 공간을 말한다.
~~~
np.random.seed(123)
data = np.random.random(10)
~~~
#(1) 
~~~
avg = np.average(data)
med = np.median(data)
std = np.std(data)
print (f"average = {avg:.3f}, median = {med:.3f}, standard deviation = {std:.3f}")
~~~
# (2)
~~~
avg, med, std = sigma_clipped_stats(data, sigma=1, iters=1)
print (f"average = {avg:.3f}, median = {med:.3f}, standard deviation = {std:.3f}")
~~~
# (3)
~~~ 
eps = 10**(-10)
for i in range(6):
    avg, med, std = sigma_clipped_stats(data, sigma=1, iters=i)
    avg0, med0, std0 = sigma_clipped_stats(data, sigma=1, iters=i+1)
    if abs(avg-avg0) < eps and abs(med-med0) < eps and abs(std-std0) < eps :
        print(f"average = {avg:.3f}, median = {med:.3f}, standard deviation = {std:.3f}")
        print(f"At N_iter {i}, these three values stop to change.")
        break
~~~
결과는 다음과 같다.
![Alt text](/Users/Owner/Desktop/천관실2/result1.png)