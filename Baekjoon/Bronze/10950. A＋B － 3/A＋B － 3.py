# sys 모듈 임포트해서 표준 입력시간 단축
import sys

# 사용자에게 테스트 케이스 개수 t 입력 받기
t = int(sys.stdin.readline()) # sys.stdin.readline()는 한 줄을 읽어옴(문자열)

# t만큼 반복해서 테스트 케이스 처리
for _ in range(t): # _는 반복 횟수가 중요하지 않을 때 변수 명으로 씀

    # 사용자에게 a , b 입력 받기
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)

# 입력시간을 단축하기 위해 sys 모듈을 사용했다.
# 입력 값을 받고 그 수 만큼 반복해 주어진 값 대로 더해서 출력하는 간단한 문제







