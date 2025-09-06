import sys

def solve():
    """
    MenOfPassion 알고리즘의 수행 횟수와 최고차항의 차수를 계산하는 함수
    """
    try:
        n = int(sys.stdin.readline())
    except (IOError, ValueError):
        return

    # 코드1의 수행 횟수는 n * n
    count = n * n

    # 최고차항의 차수는 2
    degree = 2

    print(count)
    print(degree)

if __name__ == "__main__":
    solve()