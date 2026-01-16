import sys
from typing import List


def check_and_compress(x: int, y: int, n: int, video: List[str]) -> str:
    """
    주어진 영역이 모두 같은 숫자인지 확인하고 압축을 수행하는 함수
    """
    initial_color: str = video[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            # 영역 내 다른 숫자가 발견되면 4분할 재귀 호출
            if video[i][j] != initial_color:
                half: int = n // 2
                res: str = "("
                res += check_and_compress(x, y, half, video)  # 왼쪽 위
                res += check_and_compress(x, y + half, half, video)  # 오른쪽 위
                res += check_and_compress(x + half, y, half, video)  # 왼쪽 아래
                res += check_and_compress(x + half, y + half, half, video)  # 오른쪽 아래
                res += ")"
                return res

    # 모든 영역이 같은 숫자라면 해당 숫자 반환
    return initial_color


def solve() -> None:
    """
    입력을 받고 쿼드트리 압축 결과를 출력하는 메인 함수
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])
    video_data: List[str] = input_data[1:]

    result: str = check_and_compress(0, 0, n, video_data)
    print(result)


if __name__ == "__main__":
    solve()