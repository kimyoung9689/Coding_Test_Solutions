from collections import deque
import sys

# 입력이 많을 때 속도를 위해 sys.stdin.readline 사용
# N 입력
input = sys.stdin.read
data = input().split()
N = int(data[0])
moves = list(map(int, data[1:]))

# (풍선 번호, 이동 값) 튜플로 deque 생성
# 풍선 번호는 1부터 시작
balloons = deque((i + 1, moves[i]) for i in range(N))

result = []

# 모든 풍선이 터질 때까지 반복
while balloons:
    # 1. 현재 풍선 터뜨리기: 맨 앞 풍선 (번호, 값) 꺼내기
    idx, move = balloons.popleft()
    result.append(idx)
    
    # 2. 남은 풍선이 없으면 종료
    if not balloons:
        break
        
    # 3. 다음 풍선 찾기 (deque 회전)
    # move > 0 (오른쪽 이동): popleft로 1칸 이미 이동했으니 (move - 1)만큼 오른쪽 회전 (음수)
    if move > 0:
        balloons.rotate(-(move - 1))
    # move < 0 (왼쪽 이동): move의 절대값만큼 왼쪽 회전 (양수)
    else:
        balloons.rotate(-move)

# 결과 출력
print(*result)