import sys

def check_big_o_n(a1: int, a0: int, c: int, n0: int) -> int:
    """
    주어진 f(n), c, n0가 O(n) 정의를 만족하는지 확인하는 함수

    Args:
        a1: f(n)의 n 항 계수
        a0: f(n)의 상수 항
        c: 빅오 정의의 상수 c
        n0: 빅오 정의의 상수 n0

    Returns:
        O(n) 정의를 만족하면 1, 아니면 0
    """
    for n in range(n0, 101): # n이 n0부터 100까지의 범위에서만 확인하기
        if a1 * n + a0 > c * n:
            return 0
    return 1

def main():
    try:
        a1, a0 = map(int, sys.stdin.readline().split())
        c = int(sys.stdin.readline())
        n0 = int(sys.stdin.readline())

        result = check_big_o_n(a1, a0, c, n0)
        print(result)
        
    except ValueError:
        print("입력값 올바르지 않음")

if __name__ == "__main__":
    main()