import sys

# 테스트 케이스 개수 입력 받기
T = int(sys.stdin.readline())

# T번 반복
for _ in range(T):
  C = int(sys.stdin.readline()) # 거스름돈 C 입력 받기

  # 쿼터 개수 계산
  quarters = C // 25
  C %= 25

  # 다임 개수 계산
  dimes = C // 10
  C %= 10

  # 니켈 개수 계산
  nickels = C // 5
  C %= 5

  # 페니 개수 계산
  pennies = C // 1

  # 공백 구분해서 출력
  print(quarters, dimes, nickels, pennies)