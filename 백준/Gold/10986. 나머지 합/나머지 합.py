import sys
from typing import List

def solve() -> None:
    # 입력 속도 향상
    input = sys.stdin.read().split()
    if not input:
        return
    
    n: int = int(input[0])
    m: int = int(input[1])
    numbers: List[int] = list(map(int, input[2:]))

    prefix_sum: int = 0
    # 나머지가 같은 누적 합의 개수를 저장할 배열
    remainder_count: List[int] = [0] * m
    result: int = 0

    for i in range(n):
        prefix_sum += numbers[i]
        remainder: int = prefix_sum % m
        
        # 나머지가 0인 경우는 그 자체로 조건을 만족하므로 정답에 추가
        if remainder == 0:
            result += 1
        
        # 나머지 개수 카운트
        remainder_count[remainder] += 1

    # 나머지가 같은 지점들 중에서 2개를 고르는 조합 계산 (nC2)
    for count in remainder_count:
        if count > 1:
            result += (count * (count - 1)) // 2

    print(result)

if __name__ == "__main__":
    solve()