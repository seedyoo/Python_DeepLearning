# x점들과 직선의 거리 -> 최소
# w점들과 직선의 거리 -> 최소
import numpy as np

x = [[2,3], [4,5]]  # 0번째, 1번째
nx = np.array(x)
print(nx)

a1 = 1
b1 = 2
c1 = 1
nx[:,0] *= a1
print(nx)