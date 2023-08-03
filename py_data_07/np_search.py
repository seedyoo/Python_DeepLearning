import numpy as np

py_data = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for c in range(3):
    print(py_data[0][c])
    
np_data = np.array(py_data)
print(np_data[0,: ])    # 1qjsgoddml ahems epdlxj
# 2번째 열의 모든 행데이터
print(np_data[ :,1])