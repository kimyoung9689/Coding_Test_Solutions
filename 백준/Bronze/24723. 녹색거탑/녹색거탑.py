import sys

# 입력 속도를 높이기 위해 sys.stdin.readline 사용
# N층 녹색거탑을 내려오는 경우의 수는 2의 N제곱
def solve():
    # 입력으로 높이 N을 받는다.
    try:
        # N은 1 이상 5 이하의 정수
        n = int(sys.stdin.readline())
    except:
        # 입력이 없거나 잘못된 경우 처리
        return

    # 경우의 수는 2^N.
    # ** 연산자는 거듭제곱을 의미
    result = 2 ** n
    print(result)

if __name__ == "__main__":
    solve()