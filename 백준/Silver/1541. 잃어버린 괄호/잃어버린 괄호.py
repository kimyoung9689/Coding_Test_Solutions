import sys


def solve() -> None:
    """
    백준 1541: 잃어버린 괄호
    - 기준으로 식을 나누어 최솟값을 계산한다.
    """
    # 입력을 읽어와서 '-' 단위로 쪼갠다.
    input_data: str = sys.stdin.readline().strip()
    parts: list[str] = input_data.split('-')

    # 첫 번째 파트의 숫자들을 합산한다.
    initial_sum: int = sum(int(n) for n in parts[0].split('+'))

    # 이후 파트들은 각각의 합을 구한 뒤 뺀다.
    result: int = initial_sum
    for part in parts[1:]:
        result -= sum(int(n) for n in part.split('+'))

    print(result)


if __name__ == "__main__":
    solve()