import sys
from typing import Callable # 타입 힌트 추가

# 입력 값 N을 받아옴 (0 <= N <= 12)
try:
    N: int = int(sys.stdin.readline())
except EOFError:
    N = 0

# 팩토리얼을 계산하는 재귀 함수 정의
def factorial(n: int) -> int:
    """N!을 계산하는 재귀 함수."""
    # 0!은 1이라는 기본 조건
    if n <= 1:
        return 1
    # N! = N * (N-1)! 공식 적용
    return n * factorial(n - 1)

# 계산 결과 출력
print(factorial(N))