import sys
from typing import List

# 입력 속도 개선
# sys.setrecursionlimit(10**6) # 재귀 깊이 제한을 늘릴 필요가 있을 경우 사용

def get_star(n: int, r: int, c: int) -> str:
    """
    N x N 패턴에서 (r, c) 위치에 들어갈 문자를 반환합니다.

    :param n: 현재 패턴의 크기 (N)
    :param r: 현재 패턴 내 행 위치 (0 <= r < n)
    :param c: 현재 패턴 내 열 위치 (0 <= c < n)
    :return: '*' 또는 ' '
    """
    # **기저 조건 (N=1):** 가장 작은 단위에서는 별을 반환
    if n == 1:
        return '*'

    # **현재 단계의 중앙 확인:**
    # 9등분 했을 때 중앙 (1, 1) 영역인지 확인 (r/3, c/3이 모두 1인 경우)
    third: int = n // 3
    if third <= r < third * 2 and third <= c < third * 2:
        return ' ' # 중앙 블록은 공백
    else:
        # **재귀 호출:**
        # 중앙이 아니면 다음 단계(N/3)의 (r%third, c%third) 위치를 확인
        return get_star(third, r % third, c % third)


def solve() -> None:
    """
    문제의 요구사항에 따라 별 패턴을 출력하는 메인 함수
    """
    try:
        # 입력 N을 받음
        n_str: str = sys.stdin.readline()
        if not n_str:
            return
        
        n: int = int(n_str.strip())
    except EOFError:
        return
    except ValueError:
        return

    # 결과 문자열을 담을 리스트 (메모리 사용 최적화)
    result: List[str] = []

    # N x N 모든 좌표를 순회하며 문자를 결정
    for r in range(n):
        line: List[str] = []
        for c in range(n):
            line.append(get_star(n, r, c))
        
        # 한 행이 완성되면 결과 리스트에 추가
        result.append(''.join(line))

    # 모든 행을 한 번에 출력
    sys.stdout.write('\n'.join(result) + '\n')


# 함수 실행
if __name__ == '__main__':
    solve()