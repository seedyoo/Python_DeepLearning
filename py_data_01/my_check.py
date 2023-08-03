# 1부터 100 까지 숫자 중에 짝수만 출력
# 1.
for i in range(2,102,2):
    print(i, end=' ')
    
# 2.
input = list(range(1,101))  
for i in input:
    if i%2 ==0:
        print(i, end=' ')
    
