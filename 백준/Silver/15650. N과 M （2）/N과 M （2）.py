import sys
from typing import List

# 입력 함수를 sys.stdin.readline으로 설정해 입력 속도를 높인다.
# 입력 값이 정해져 있으므로 (1 <= M <= N <= 8) 성능에 큰 차이는 없지만
# 습관적으로 사용하는 것이 좋다.
input = sys.stdin.readline

def solve_n_m_2() -> None:
    # N과 M을 입력받아 정수로 변환한다.
    n, m = map(int, input().split())
    
    # 현재 만들어지고 있는 수열을 저장할 리스트
    sequence: List[int] = []

    def backtrack(start: int) -> None:
        # **종료 조건**: 수열의 길이가 M이 되면 (M개의 숫자를 모두 고르면)
        if len(sequence) == m:
            # 수열을 공백으로 구분해서 출력한다.
            print(*sequence)
            return

        # **재귀 호출**: start부터 N까지의 숫자를 탐색한다.
        # start는 이전에 고른 숫자보다 **크거나 같은** 수부터 탐색을 시작해야 한다.
        # 이전에 고른 숫자보다 **큰** 수부터 탐색해야 '오름차순' 조건을 만족하고 
        # '중복 없이' 고르는 효과를 낸다.
        for i in range(start, n + 1):
            # i를 현재 수열에 추가한다.
            sequence.append(i)
            
            # 다음 숫자는 현재 고른 i 다음인 i + 1부터 탐색하도록 재귀 호출한다.
            # 이 부분이 **오름차순**과 **중복 없음** 조건을 만족시킨다.
            # 만약 i가 아닌 start를 넘기면 (N과 M (1)처럼) 오름차순을 보장할 수 없다.
            # 따라서 **i + 1**을 넘겨야 한다.
            backtrack(i + 1)
            
            # 재귀 호출이 끝나면 (다음 경우의 수를 탐색하기 위해)
            # 수열에 추가했던 i를 제거하고 돌아간다 (백트래킹).
            sequence.pop()

    # 1부터 N까지의 숫자 중에서 시작해야 하므로 start=1로 호출한다.
    backtrack(1)

if __name__ == '__main__':
    solve_n_m_2()