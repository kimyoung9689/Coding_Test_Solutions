import sys

def solve():
    """
    정수 N을 소인수분해하는 함수
    """
    n = int(sys.stdin.readline())

    # N이 1인 경우 아무것도 출력하지 않고 종료
    if n == 1:
        return

    # 2부터 N의 제곱근까지 나누어 보며 소인수 찾기
    i = 2
    while i * i <= n:
        while n % i == 0:
            print(i)
            n //= i
        i += 1

    # 위 반복문이 끝난 후, N이 1보다 크면 남은 N은 소수
    if n > 1:
        print(n)

solve()
