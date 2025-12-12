from itertools import combinations
from typing import List

# N: 총 인원수 (짝수)
N: int
# S: 능력치 행렬
S: List[List[int]]

def solve() -> int:
    """
    스타트 팀과 링크 팀의 능력치 차이의 최솟값을 계산한다.
    N명 중 N/2명을 뽑는 모든 조합을 확인하는 완전 탐색 문제이다.
    """
    global N, S
    
    # N을 입력받는다.
    try:
        N = int(input())
    except EOFError:
        return 0

    # 능력치 행렬 S를 입력받는다.
    S = []
    for _ in range(N):
        S.append(list(map(int, input().split())))

    # 최종 결과: 능력치 차이의 최솟값. 최대 가능한 능력치 합(20 * 100 * 20/2 * (20/2 - 1) / 2 = 9500)보다 큰 값으로 초기화.
    min_diff = float('inf')
    
    # 총 N명(0부터 N-1까지) 중 N/2명을 뽑는 모든 조합(스타트 팀)을 만든다.
    # combinations(iterable, r): iterable에서 원소 r개를 고르는 조합을 반환.
    all_members = list(range(N))
    
    # N/2명을 뽑는 모든 조합(스타트 팀)을 순회한다.
    for start_team_indices in combinations(all_members, N // 2):
        # 스타트 팀에 포함되지 않은 나머지 사람들은 링크 팀이 된다.
        # set.difference를 사용하여 스타트 팀에 없는 사람들을 찾는다.
        link_team_indices = list(set(all_members).difference(set(start_team_indices)))
        
        # 스타트 팀과 링크 팀의 능력치를 계산한다.
        start_score: int = 0
        link_score: int = 0
        
        # 각 팀의 모든 가능한 두 사람 쌍에 대해 능력치를 합산한다.
        # 팀의 능력치는 팀원 쌍 (i, j)에 대해 S[i][j] + S[j][i]의 합이다.
        for i, j in combinations(start_team_indices, 2):
            start_score += S[i][j] + S[j][i]
            
        for i, j in combinations(link_team_indices, 2):
            link_score += S[i][j] + S[j][i]

        # 두 팀 능력치 차이의 절댓값을 구한다.
        diff = abs(start_score - link_score)
        
        # 최솟값을 갱신한다.
        min_diff = min(min_diff, diff)

        # 만약 차이가 0이라면 더 이상 탐색할 필요가 없다 (최솟값 0).
        if min_diff == 0:
            break
            
    # 최종 최솟값을 반환한다.
    return min_diff

# 함수를 호출하고 결과를 출력한다.
if __name__ == "__main__":
    print(solve())