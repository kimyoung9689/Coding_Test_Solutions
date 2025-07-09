import sys # 모듈 임포트

# 
for line in sys.stdin:
  a, b = map(int, line.split()) # a와b 입력 받기
  print(a + b) # 출력




# 처음에 문제를 잘못 이해했다. 
# 문제에선 테스트 케이스 개수를 미리 입력 받는 것
# 때문에 코드를 for line in sys.stdin: 로 고쳤다.


# input() : 한 줄씩 읽어오고 줄바꿈 문자를 자동제거 해준다. + 입력이 더 없으면 에러남

# sys.stdin.readline(): 한 줄씩 읽어오고 줄바꿈 문자를 제거하지 않고 가져옴
#                       그래서 strip() 같은걸로 제거 할 때 있다.(대신 입력속도가 빠름)

# or line in sys.stdin: sys.stdin 객체를 반복 가능한(iterable) 객체로 사용하는 것
#                       입력이 몇 줄이 들어올지 모를때, 끝날 때까지 자동으로 계속 읽음
#                       줄바꿈 문자를 포함해 읽어와서 line.split()처럼 이어 쓰는 경우 많음

# 결론
# or line in sys.stdin:은 입력의 양이 정해져 있지 않고, 
# 입력이 끝날 때까지 모든 줄을 읽어서 처리해야 할 때 아주 유용한 방법
# 백준 같은 알고리즘 문제 풀이에서 많이 쓰이는 패턴이다.