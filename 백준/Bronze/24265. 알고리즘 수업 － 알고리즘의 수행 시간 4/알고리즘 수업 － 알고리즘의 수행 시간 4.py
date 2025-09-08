"""
MenOfPassion 알고리즘의 수행 시간을 계산하는 코드
"""
import sys

def men_of_passion_runtime(n: int) -> tuple[int, int]:
    """
    MenOfPassion 알고리즘의 수행 횟수와 최고차항의 차수를 계산하는 함수.

    Args:
        n (int): 입력의 크기.

    Returns:
        tuple[int, int]: 코드1의 수행 횟수와 최고차항의 차수.
    """
    # 코드1의 수행 횟수는 n(n-1)/2. 조합의 수와 같음.
    count = n * (n - 1) // 2

    # 최고차항은 n^2. 차수는 2.
    degree = 2

    return count, degree

if __name__ == "__main__":
    try:
        n = int(sys.stdin.readline())
        execution_count, polynomial_degree = men_of_passion_runtime(n)
        print(execution_count)
        print(polynomial_degree)
    except (ValueError, IndexError):
        print("입력이 올바르지 않아. 정수 n을 입력해야 함.")