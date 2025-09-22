import sys

def solve() -> None:
    """
    N킬로그램을 배달하기 위한 최소 봉지 개수를 구하는 함수
    """

    n = int(sys.stdin.readline().strip())

    # 5kg 봉지를 가장 많이 쓰는 경우
    for five_kg_count in range(n // 5, -1, -1):
        remaining_kg = n - (five_kg_count * 5)

        # 남은 무게가 3kg 봉지로 딱 떨어지는지 확인
        if remaining_kg % 3 == 0:
            three_kg_count = remaining_kg // 3
            print(five_kg_count + three_kg_count)
            return

    # 5kg 봉지를 줄여가며 시도 안되면 -1 출력
    print(-1)

if __name__ == "__main__":
    solve()