import sys  # 시스템 모듈 사용, 입력 빠르게 받기 위함

def solve() -> None:
    """N!을 계산하고 출력하는 함수"""
    try:
        # sys.stdin.readline()으로 한 줄의 입력을 문자열로 읽고 정수로 변환
        # N은 0 <= N <= 20
        n: int = int(sys.stdin.readline())
    except EOFError:
        # 입력이 없는 경우 처리
        return

    # 팩토리얼 결과를 저장할 변수.
    # 0!은 1이므로 초기값을 1로 설정
    result: int = 1

    # 1부터 N까지 반복하며 result에 곱함
    # range(1, n + 1)은 1, 2, ..., n을 만듦
    for i in range(1, n + 1):
        result *= i  # result = result * i

    # 계산된 N! 값을 출력
    print(result)

if __name__ == "__main__":
    solve()