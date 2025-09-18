import sys


def find_smallest_constructor(target_n: int) -> int:
    """
    주어진 자연수 N의 가장 작은 생성자를 찾는 코드

    Args:
        target_n: 생성자를 찾을 목표 자연수 N (1 <= N <= 1,000,000)

    Returns:
        가장 작은 생성자 M, 또는 생성자가 없을 경우 0
    """
    # 1부터 N까지 모든 자연수를 확인
    for m in range(1, target_n + 1):
        # 분해합 계산
        # 정수를 문자열로 변환해 각 자리수에 접근한 후, 합을 구함
        decomposition_sum = m + sum(int(digit) for digit in str(m))

        # 분해합이 N과 같은지 확인
        if decomposition_sum == target_n:
            # 가장 작은 생성자를 찾았으므로 바로 반환
            return m

    # 반복문을 다 돌아도 생성자를 못 찾은 경우
    return 0


if __name__ == "__main__":
    try:
        n_str = sys.stdin.readline().strip()
        if not n_str:
            sys.exit(0)
        n: int = int(n_str)
        result = find_smallest_constructor(n)
        print(result)
    except (ValueError, IndexError):
        # 입력 오류 발생 시 0을 출력하거나, 필요에 따라 오류 처리를 할 수 있음
        print(0)