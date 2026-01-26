import sys

# 1,000,000,007로 나눈 나머지
MOD: int = 1_000_000_007


def multiply(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]]:
    """두 2x2 행렬의 곱셈을 수행한다."""
    result: list[list[int]] = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] %= MOD
    return result


def power(matrix: list[list[int]], n: int) -> list[list[int]]:
    """행렬의 n거듭제곱을 분할 정복으로 계산한다."""
    res: list[list[int]] = [[1, 0], [0, 1]]  # 단위 행렬
    while n > 0:
        if n % 2 == 1:
            res = multiply(res, matrix)
        matrix = multiply(matrix, matrix)
        n //= 2
    return res


def solve() -> None:
    """메인 실행 함수"""
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    n: int = int(line)
    
    if n == 0:
        print(0)
        return
    if n == 1:
        print(1)
        return

    # 피보나치 기본 행렬
    base_matrix: list[list[int]] = [[1, 1], [1, 0]]
    
    # 행렬의 n-1 거듭제곱 계산
    final_matrix: list[list[int]] = power(base_matrix, n)
    
    # F_n은 결과 행렬의 [0][1] 또는 [1][0] 위치의 값
    print(final_matrix[0][1])


if __name__ == "__main__":
    solve()