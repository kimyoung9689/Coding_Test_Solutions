import sys
from typing import List


def multiply_matrices() -> None:
    """
    두 행렬을 입력받아 곱셈 결과를 출력하는 함수
    """
    # 행렬 A 입력
    n, m = map(int, sys.stdin.readline().split())
    matrix_a: List[List[int]] = [
        list(map(int, sys.stdin.readline().split())) for _ in range(n)
    ]

    # 행렬 B 입력
    m_check, k = map(int, sys.stdin.readline().split())
    matrix_b: List[List[int]] = [
        list(map(int, sys.stdin.readline().split())) for _ in range(m_check)
    ]

    # 결과 행렬 초기화 (N x K 크기)
    result: List[List[int]] = [[0] * k for _ in range(n)]

    # 행렬 곱셈 수행: C[i][j] = sum(A[i][l] * B[l][j])
    for i in range(n):
        for j in range(k):
            for l in range(m):
                result[i][j] += matrix_a[i][l] * matrix_b[l][j]

    # 결과 출력
    for row in result:
        print(*(row))


if __name__ == "__main__":
    multiply_matrices()