import sys
# 입력 속도 개선
input = sys.stdin.read

# 입력 데이터를 한 번에 읽음
data = input().split()

# 첫 번째 줄 N (사용 안 함)
N = int(data[0])
# 두 번째 줄 카드 목록
cards = list(map(int, data[1:N+1]))

# 세 번째 줄 M (사용 안 함)
M = int(data[N+1])
# 네 번째 줄 찾을 숫자 목록
targets = list(map(int, data[N+2:]))

# 1. 상근이 카드들의 개수를 딕셔너리에 저장
counts = {}
for card in cards:
    counts[card] = counts.get(card, 0) + 1

# 2. 찾을 숫자들 각각의 개수를 확인
results = []
for target in targets:
    # 딕셔너리에 없으면 0, 있으면 해당 개수
    results.append(str(counts.get(target, 0)))

# 결과를 공백으로 구분하여 출력
print(" ".join(results))