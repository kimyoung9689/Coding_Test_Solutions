# sys 모듈 불러오기
import sys

# n값 입력 받기
n = int(sys.stdin.readline().rstrip())

# 1부터 n까지 반복하기
for i in range(1, n + 1):
    print('*'* i) # i만큼 별을 곱해서 출력


# for문을 이용해서 하나 하나 값을 받아올 때 마다 별을 늘리면 되는 간단한 문제
