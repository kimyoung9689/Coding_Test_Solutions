import sys
from typing import List, Tuple

# 입력이 작으므로 (N<=8) 빠르게 읽기 위해 sys.stdin.readline 사용
def solve() -> None:
    """
    백트래킹을 사용하여 'N과 M (1)' 문제의 조건을 만족하는
    길이 M의 수열을 모두 찾아 출력한다.
    """
    try:
        # N, M을 입력받는다.
        # sys.stdin.readline().split()은 ['4', '2']와 같은 문자열 리스트를 반환
        input_data: List[str] = sys.stdin.readline().split()
        if not input_data:
            return
            
        N: int = int(input_data[0])
        M: int = int(input_data[1])
    except EOFError:
        return
    except ValueError:
        return

    # 완성된 수열을 저장할 리스트 (M개의 숫자가 채워짐)
    sequence: List[int] = []
    
    # 방문 여부를 체크하는 리스트 (1부터 N까지 숫자에 대응)
    # 인덱스 0은 사용하지 않고, is_visited[i]는 숫자 i의 사용 여부를 나타냄
    is_visited: List[bool] = [False] * (N + 1)

    def backtrack() -> None:
        """
        수열의 길이가 M이 될 때까지 재귀적으로 숫자를 선택하는 함수.
        """
        # 1. 종료 조건 (수열 완성)
        if len(sequence) == M:
            # 수열을 공백으로 구분하여 출력
            print(" ".join(map(str, sequence)))
            return

        # 2. 다음 숫자 선택
        # 1부터 N까지 숫자를 차례대로 시도한다.
        for i in range(1, N + 1):
            # i가 아직 사용되지 않은 숫자라면
            if not is_visited[i]:
                # i를 사용했다고 표시
                is_visited[i] = True
                
                # 수열에 i를 추가
                sequence.append(i)
                
                # 다음 위치의 숫자를 고르기 위해 재귀 호출 (깊이 탐색)
                backtrack()
                
                # 3. 철수 (백트래킹)
                # 재귀 호출이 끝나면, 방금 추가했던 i를 수열에서 제거
                sequence.pop()
                
                # i의 사용 표시를 다시 False로 되돌려 다른 경우의 수에서 i를 사용할 수 있게 함
                is_visited[i] = False

    # 백트래킹 시작
    backtrack()

# 함수 호출
solve()