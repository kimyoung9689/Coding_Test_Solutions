import math
import sys

# 표준 입력에서 창문 및 사람의 수 N을 읽음
n = int(sys.stdin.readline())

# N 이하의 제곱수의 개수를 구함. 이것이 마지막에 열린 창문의 개수임.
# 약수의 개수가 홀수인 수(제곱수)는 창문 상태가 홀수 번 바뀌어 열려 있음.
result = int(math.sqrt(n))  # N의 양의 제곱근의 정수 부분

print(result)