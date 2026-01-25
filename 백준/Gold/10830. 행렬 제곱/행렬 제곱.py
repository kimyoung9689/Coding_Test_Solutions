import sys
from typing import List

# 타입 힌트를 위한 별칭
Matrix = List[List[int]]

def multiply(matrix_a: Matrix, matrix_b: Matrix, size: int) -> Matrix:
    """두 행렬을 곱하고 1,000으로 나눈 나머지를 반환해."""
    result: Matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            temp: int = 0
            for k in range(size):
                temp += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = temp % 1000
    return result


def power(matrix: Matrix, exp: int, size: int) -> Matrix:
    """분할 정복을 이용해 행렬의 거듭제곱을 계산해."""
    if exp == 1:
        # 초기 원소가 1000일 경우를 대비해 나머지 연산 수행
        return [[cell % 1000 for cell in row] for row in matrix]
    
    half: Matrix = power(matrix, exp // 2, size)
    square: Matrix = multiply(half, half, size)
    
    if exp % 2 == 0:
        return square
    else:
        return multiply(square, matrix, size)


def solve() -> None:
    """입력을 받고 결과를 출력하는 메인 함수야."""
    input_data: List[str] = sys.stdin.read().split()
    if not input_data:
        return
        
    n: int = int(input_data[0])
    b: int = int(input_data[1])
    
    matrix: Matrix = []
    for i in range(n):
        row: List[int] = list(map(int, input_data[2 + i*n : 2 + (i+1)*n]))
        matrix.append(row)
    
    result_matrix: Matrix = power(matrix, b, n)
    
    for row in result_matrix:
        print(*(row))


if __name__ == "__main__":
    solve()