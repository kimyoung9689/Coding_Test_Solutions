import sys

def solve():
    """
    MenOfPassion 알고리즘의 수행 횟수와 최고차항의 차수를 계산
    """
    try:
        n = int(sys.stdin.readline())
    except (IOError, ValueError) as e:
        print(f"입력 오류: {e}", file=sys.stderr)
        return

    # 코드1의 수행 횟수는 n * n * n
    # n의 범위(1 <= n <= 500,000)를 고려하여 n^3을 계산
    # n이 500,000일 때 n^3은 1.25 * 10^17, 이는 int형으로 처리 가능
    execution_count = n * n * n

    # 최고차항의 차수는 3
    degree = 3

    print(execution_count)
    print(degree)

if __name__ == '__main__':
    solve()