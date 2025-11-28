import sys
from typing import List

# 입력 n을 받는다.
# n은 20보다 작거나 같은 자연수 또는 0이다.
def solve() -> None:
    """
    n번째 피보나치 수를 계산하고 출력한다.
    """
    try:
        # sys.stdin.readline()을 사용하여 입력을 받는다.
        # 입력은 한 줄이고 n 하나만 주어진다.
        n_str = sys.stdin.readline().strip()
        if not n_str:
            # 입력이 없으면 종료한다.
            return
        n: int = int(n_str)
    except Exception:
        # 입력 변환 중 오류가 발생하면 종료한다.
        return

    # n이 0 또는 1일 경우를 처리한다.
    if n <= 1:
        # F_0 = 0, F_1 = 1
        print(n)
        return

    # 피보나치 수열을 저장할 리스트를 초기화한다.
    # fib[i]는 i번째 피보나치 수를 저장한다.
    # 초깃값은 F_0=0, F_1=1
    fib: List[int] = [0, 1]

    # 2번째 수부터 n번째 수까지 계산한다.
    # F_i = F_{i-1} + F_{i-2}
    for i in range(2, n + 1):
        # 바로 앞 두 수의 합을 새로운 피보나치 수로 추가한다.
        next_fib: int = fib[i - 1] + fib[i - 2]
        fib.append(next_fib)

    # n번째 피보나치 수를 출력한다.
    # 리스트의 인덱스는 0부터 시작하므로 fib[n]이 n번째 수이다.
    print(fib[n])

if __name__ == "__main__":
    solve()