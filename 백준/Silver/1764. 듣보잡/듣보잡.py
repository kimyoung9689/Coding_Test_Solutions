import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# N: 듣도 못한 사람 수, M: 보도 못한 사람 수
N, M = map(int, input().split())

# 듣도 못한 사람 명단을 저장할 집합 생성
# 집합(set)은 중복을 허용하지 않고 탐색 속도가 빠름
never_heard = set()

# N개의 듣도 못한 사람 이름을 집합에 추가
for _ in range(N):
    # 이름은 양 끝 공백 제거 후 저장
    never_heard.add(input().strip())

# 듣보잡 명단을 저장할 리스트
never_seen_heard = []

# M개의 보도 못한 사람 이름을 확인
for _ in range(M):
    name = input().strip()
    # 현재 이름이 '듣도 못한 사람' 명단(집합)에 있는지 확인
    if name in never_heard:
        # 있다면 '듣보잡' 명단에 추가
        never_seen_heard.append(name)

# 1. 듣보잡의 수를 출력
print(len(never_seen_heard))

# 2. 명단을 사전순으로 정렬 후 출력
# 문제 조건에 따라 사전순 정렬
never_seen_heard.sort()

# 정렬된 명단을 한 줄씩 출력
for name in never_seen_heard:
    print(name)