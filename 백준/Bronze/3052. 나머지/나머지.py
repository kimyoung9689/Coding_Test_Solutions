import sys

# 나머지 저장할 빈 set 생성
result = set()

# 숫자 10개 받기
for _ in range(10):
  num = int(sys.stdin.readline().strip()) # 사용자에게 정수로 입력 값 받기
  result.add(num % 42)                    # 42로 나눈 나머지 set에 추가

# set에 들어있는 나머지 개수 출력
print(len(result))
