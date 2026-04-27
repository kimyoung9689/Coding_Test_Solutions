import sys
from typing import List, Tuple

# 재귀 깊이 제한 해제
sys.setrecursionlimit(2000)


def solve() -> None:
    # 입력 처리
    n: int = int(sys.stdin.readline())
    w: int = int(sys.stdin.readline())
    
    # 사건 위치 저장 (0번: 경찰차1 시작, 1번: 경찰차2 시작, 2~W+1번: 실제 사건)
    events: List[Tuple[int, int]] = [(1, 1), (n, n)]
    for _ in range(w):
        events.append(tuple(map(int, sys.stdin.readline().split())))

    # DP 테이블 초기화 (-1은 아직 계산되지 않음을 의미)
    dp: List[List[int]] = [[-1] * (w + 2) for _ in range(w + 2)]
    # 경로 추적을 위한 테이블
    choice: List[List[int]] = [[0] * (w + 2) for _ in range(w + 2)]

    def get_distance(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
        """두 좌표 사이의 맨해튼 거리를 계산한다."""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def find_min_dist(p1_idx: int, p2_idx: int) -> int:
        """DP를 이용해 최소 거리를 구하는 재귀 함수 (Memoization)"""
        current_event: int = max(p1_idx, p2_idx) + 1
        
        # 모든 사건을 다 처리한 경우
        if current_event == w + 2:
            return 0
        
        if dp[p1_idx][p2_idx] != -1:
            return dp[p1_idx][p2_idx]

        # 1번 경찰차가 현재 사건을 처리하는 경우
        dist1: int = (find_min_dist(current_event, p2_idx) + 
                      get_distance(events[p1_idx], events[current_event]))
        
        # 2번 경찰차가 현재 사건을 처리하는 경우
        dist2: int = (find_min_dist(p1_idx, current_event) + 
                      get_distance(events[p2_idx], events[current_event]))

        # 최솟값 선택 및 경로 기록
        if dist1 < dist2:
            dp[p1_idx][p2_idx] = dist1
            choice[p1_idx][p2_idx] = 1
        else:
            dp[p1_idx][p2_idx] = dist2
            choice[p1_idx][p2_idx] = 2
            
        return dp[p1_idx][p2_idx]

    # 최소 거리 출력 (1번 경찰차는 index 0, 2번 경찰차는 index 1에서 시작)
    print(find_min_dist(0, 1))

    # 경로 역추적 및 출력
    curr_p1: int = 0
    curr_p2: int = 1
    for i in range(2, w + 2):
        police_num: int = choice[curr_p1][curr_p2]
        print(police_num)
        if police_num == 1:
            curr_p1 = i
        else:
            curr_p2 = i


if __name__ == "__main__":
    solve()