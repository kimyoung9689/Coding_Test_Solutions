import sys

# 숫자의 개수 n 입력 받기
n = int(sys.stdin.readline().strip())

# n개의 숫자 입력 받기
numbers = list(map(int,sys.stdin.readline().split()))

# 가장 작은 값,큰 값 찾기
min_value = min(numbers)
max_value = max(numbers)

# 출력하기
print(min_value, max_value)