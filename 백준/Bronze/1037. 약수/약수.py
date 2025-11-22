from typing import List

def find_original_number(divisors: List[int]) -> int:
    # 가장 작은 약수와 가장 큰 약수를 곱하면 N이 됨
    min_divisor: int = min(divisors)
    max_divisor: int = max(divisors)
    
    return min_divisor * max_divisor

# 약수 개수 입력 (사용 안 함)
try:
    input()
except:
    number_of_divisors: int = 0

# 진짜 약수 리스트 입력
try:
    actual_divisors: List[int] = [int(x) for x in input().split()]
except:
    actual_divisors: List[int] = []

# 결과 출력
if actual_divisors:
    result: int = find_original_number(actual_divisors)
    print(result)