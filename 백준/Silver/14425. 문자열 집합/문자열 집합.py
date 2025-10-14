import sys
# 입력 속도 개선을 위해 sys.stdin.readline 사용
# 대량의 입력 시 효율적

# 첫째 줄 N(집합 S의 크기)과 M(검사할 문자열의 크기)을 입력받음
try:
    N, M = map(int, sys.stdin.readline().split())
except:
    # EOF 예외 처리
    N, M = 0, 0

# 집합 S를 저장할 set 자료형을 생성
S = set()

# N개의 집합 S의 원소를 입력받아 set에 추가
for _ in range(N):
    S.add(sys.stdin.readline().strip())

# 집합 S에 포함되는 문자열의 개수를 저장할 변수 초기화
count = 0

# M개의 검사할 문자열을 입력받아 집합 S에 포함되는지 확인
for _ in range(M):
    check_str = sys.stdin.readline().strip()
    # 검사할 문자열이 S에 있으면 count 증가
    if check_str in S:
        count += 1

# 결과 출력
print(count)