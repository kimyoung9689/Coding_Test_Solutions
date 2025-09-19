import sys
from typing import List

def solve_linear_equations(a: int, b: int, c: int, d: int, e: int, f: int) -> List[int]:
    """
    두 개의 미지수를 가진 연립방정식 풀기

    Args:
        a: 첫 번째 방정식의 x 계수
        b: 첫 번째 방정식의 y 계수
        c: 첫 번째 방정식의 상수항
        d: 두 번째 방정식의 x 계수
        e: 두 번째 방정식의 y 계수
        f: 두 번째 방정식의 상수항

    Returns:
        방정식의 해인 [x, y] 값의 리스트
    """
    # x 또는 y를 소거하기 위해 한 변수를 정리
    # 여기서는 y를 소거하기 위해 첫 번째 식에 d를, 두 번째 식에 a를 곱한다.
    denominator = a * e - b * d

    # 분모가 0이 아니라는 기준으로 계산 (문제에서 유일한 해가 보장)
    x = (c * e - b * f) / denominator
    y = (a * f - c * d) / denominator

    return [int(x), int(y)]

def main():
    """
    주요 프로그램 실행 함수
    """
    try:
        a, b, c, d, e, f = map(int, sys.stdin.readline().split())
        result = solve_linear_equations(a, b, c, d, e, f)
        print(*result)
    except (IOError, ValueError) as e:
        print(f"입력 처리중 오류가 발생: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()