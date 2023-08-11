'''
#1번
def solution(a, b, c):
    answer = 0

    if a == b == c:
        answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    elif a == b or b == c or a == c:
        answer = (a + b + c) * (a**2 + b**2 + c**2)
    else:
        answer = a + b + c

    return answer

# 사용자로부터 a, b, c 값을 입력받아 solution 함수를 호출하고 결과를 출력합니다.
a = int(input("a를 입력하세요: "))
b = int(input("b를 입력하세요: "))
c = int(input("c를 입력하세요: "))

result = solution(a, b, c)
print("결과:", result)
'''
'''
#2번
def diamond(rows):
    if rows % 2 == 0:
        rows += 1  

    for i in range(1, rows + 1):
        space = abs((rows // 2 + 1) - i)
        star = rows - 2 * space
        
        print(" " * space + "*" * star)

num_rows = int(input("행 개수 : "))
diamond(num_rows)
'''
'''
# 3번
import pandas as pd
import glob

# CSV 파일들을 검색
file_patterns = ["a.csv", "b.csv", "c.csv"] 

# 딕셔너리 정의
result_counts = {
    "GS25": 0,
    "CU": 0,
    "세븐일레븐": 0
}

# 모든 CSV 파일 검색 및 작업
for file_path in glob.glob(file_patterns):
    # CSV 파일을 읽어 데이터프레임으로 변환
    df = pd.read_csv(file_path)
    
    # B열 추출
    data_in_b = df['B']

    # 개수 세기
    for item in data_in_b:
        if item in result_counts:
            result_counts[item] += 1

# 결과 출력
for category, count in result_counts.items():
    print(f"{category}의 개수:", count)
'''
'''
# 4번
def calculator():
    while True:
        print("p: 덧셈, m: 뺄셈, c: 곱셈, d: 나눗셈, 0: 나가기")
        choice = input("선택 (p/m/c/d/0): ")
        
        if choice == "0":
            print("계산기를 종료합니다.")
            break
        
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))
        
        if choice == "p":
            result = num1 + num2
            operation = "덧셈"
        elif choice == "m":
            result = num1 - num2
            operation = "뺄셈"
        elif choice == "c":
            result = num1 * num2
            operation = "곱셈"
        elif choice == "d":
            if num2 != 0:
                result = num1 / num2
                operation = "나눗셈"
            else:
                print("0으로 나눌 수 없습니다.")
                continue
        else:
            print("잘못된 선택입니다. 다시 선택하세요.")
            continue
        
        print(f"{num1} {operation} {num2} = {result}\n")

# 계산기 실행
calculator()
'''
'''
# 5번
import random
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Gulim'

def calculate_distance(point):
    return (point[0] - 5)**2 + (point[1] - 5)**2

def generate_random_coordinates(num_coordinates):
    coordinates = set()

    while len(coordinates) < num_coordinates:
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        coordinates.add((x, y))

    return coordinates

num_coordinates = 20
random_coordinates = generate_random_coordinates(num_coordinates)
sorted_coordinates = sorted(random_coordinates, key=calculate_distance)

x_coords, y_coords = zip(*sorted_coordinates)  # 좌표를 x, y 리스트로 분리

plt.scatter(x_coords, y_coords, color='blue', label='랜덤 좌표')
plt.scatter(5, 5, color='red', label='중심 좌표 (5, 5)', marker='X')

plt.xlabel('X 축')
plt.ylabel('Y 축')
plt.title('랜덤 좌표')
plt.legend()
plt.grid()

plt.show()

'''
