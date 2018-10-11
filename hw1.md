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
(1) numpy 함수를 통해 평균과 중앙값, 표준편차를 구할 수 있다.
~~~
avg = np.average(data)
med = np.median(data)
std = np.std(data)
print (f"average = {avg:.3f}, median = {med:.3f}, standard deviation = {std:.3f}")
~~~
(2) sigma_clipped_stats 함수를 이용하여 1-sigma clipped(1 iteration)된 평균과 중앙값, 표준편차를 구할 수 있다.
~~~
avg, med, std = sigma_clipped_stats(data, sigma=1, iters=1)
print (f"average = {avg:.3f}, median = {med:.3f}, standard deviation = {std:.3f}")
~~~
(3) eps를 매우 작은 값으로 설정하고 iteration n과 n+1일 때의 평균과 중앙값, 표준편차의 차가 eps보다 작다면 iteration 횟수 n을 출력하도록 한다.  
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

problem # 02
----------------
problem # 01과 동일하게 np.random.random 함수를 통해 data를 불러 온다.
~~~
np.random.seed(123)
data = np.random.random((10, 20))
data[:, [3, 10]] += 10
~~~
iteration 횟수를 i (array)로 설정하고 sigma_clipped_stats를 실행한다.
~~~
for i in [0, 3]:
    avg, med, std = sigma_clipped_stats(data, sigma=1, iters=i, axis=0)
    plt.plot(med, label=f"Niter = {i}", ls=':', marker='.')
plt.title("Median combine")
plt.grid(ls=':')
plt.legend()
~~~
