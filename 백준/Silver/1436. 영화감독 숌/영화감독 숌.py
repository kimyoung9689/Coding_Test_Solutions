import sys

def solve() -> None:
    """
    N번째로 작은 종말의 수를 찾는 함수
    """
    try:
        n = int(sys.stdin.readline())
    except (ValueError, IndexError):
        print("유효한 숫자를 입력하기")
        return

    count = 0
    number = 665  # 666부터 시작하기 위해 665로 초기화

    while True:
        number += 1
        if "666" in str(number):
            count += 1
        
        if count == n:
            print(number)
            break

if __name__ == "__main__":
    solve()