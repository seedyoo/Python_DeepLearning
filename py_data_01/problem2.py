# 2차원 R행(5) C열(5) 로 이루어진 리스트 배열을 선언하고 
# 1~25까지 값을 대입한 후 저장된 값을 출력하시오

# 행과 열 입력 받기
rows = int(input("행 수는? "))
cols = int(input("열 수는? "))

# 2차원 리스트 생성
array = [[0] * cols for _ in range(rows)]

# 값 대입
value = 1
for i in range(rows):
    for j in range(cols):
        array[i][j] = value
        value += 1

# 값 출력
for row in array:
    for element in row:
        print(element, end=' ')
    print()