import sys

# 표준 입력을 더 빠르게 받기 위함
input = sys.stdin.read

# 입력 전체를 읽고 줄바꿈을 기준으로 나눔
data = input().split()

# 가로수 개수 N
n = int(data[0])

# 가로수 위치 리스트
trees = [int(data[i+1]) for i in range(n)]

# 유클리드 호제법으로 최대공약수(GCD)를 구하는 함수
# PEP 8 (소문자, 언더바), PEP 484 (타입 힌트) 준수
def gcd(a: int, b: int) -> int:
    # b가 0이 될 때까지 반복
    while b:
        # a에 b를, b에 (a % b)를 할당
        a, b = b, a % b
    # 최종적인 a가 최대공약수
    return a

# 인접한 가로수 사이의 간격들을 저장할 리스트
gaps = []

# 가로수 위치는 이미 정렬되어 있으므로, 인접한 위치의 차를 구함
for i in range(1, n):
    gaps.append(trees[i] - trees[i-1])

# 모든 간격들의 최대공약수를 찾음 (최소 2개의 간격이 있어야 함)
# 첫 번째 간격을 초기 최대공약수(g)로 설정
g = gaps[0]

# 나머지 간격들과의 최대공약수를 순차적으로 구함
for i in range(1, len(gaps)):
    # 현재 최대공약수 g와 다음 간격 gaps[i]의 최대공약수를 다시 g에 저장
    g = gcd(g, gaps[i])

# 새로 심어야 하는 가로수의 최소 개수
new_trees = 0

# 각 간격마다 새로 심어야 하는 나무의 수를 계산
for gap in gaps:
    # (원래 간격 / 최대공약수 간격) - 1 이 해당 구간에 새로 심을 나무 수
    # 예를 들어 간격이 6, 최대공약수가 3이면 (6/3) - 1 = 1 그루 필요
    new_trees += (gap // g) - 1

# 결과 출력
print(new_trees)