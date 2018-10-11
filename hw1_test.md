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

