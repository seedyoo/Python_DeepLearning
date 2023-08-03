# 1
def print_string():
    print_input = input("문자열을 입력하세요: ")
    print("입력한 문자열:", print_input)

print_string()

# 2
def print_string():
    print_input1 = input("첫번째 수를 입력하세요:")
    print_input2 = input("두번째 수를 입력하세요:")
    print('a = ', print_input1, 'b = ', print_input2)

print_string()

# 3
def repeat_string(input_string, repeat_count):
    repeated_string = input_string * repeat_count
    return repeated_string

if __name__ == "__main__":
    input_string = input("문자열을 입력하세요: ")
    repeat_count = int(input("정수를 입력하세요: "))

    if repeat_count <= 0:
        print("반복 횟수는 양수여야 합니다.")
    else:
        result = repeat_string(input_string, repeat_count)
        print("반복된 문자열:", result)

# 4
def swap_case(input_string):
    swapped_string = ""
    for char in input_string:
        if char.isupper():
            swapped_string += char.lower()
        elif char.islower():
            swapped_string += char.upper()
        else:
            swapped_string += char
    return swapped_string

if __name__ == "__main__":
    input_string = input("영어 알파벳으로 이루어진 문자열을 입력하세요: ")
    result = swap_case(input_string)
    print("대소문자가 변환된 문자열:", result)
    
# 5
if __name__ == "__main__":
    input_special_characters = input("특수문자를 입력하세요: ")
    print("입력한 특수문자:", input_special_characters)
    
