import sys
from bisect import bisect_right
from typing import List


def get_subset_sums(weights: List[int]) -> List[int]:
    """물건의 무게 리스트를 받아 가능한 모든 부분합을 반환한다."""
    sums = [0]
    for w in weights:
        current_sums = []
        for s in sums:
            current_sums.append(s + w)
        sums.extend(current_sums)
    return sums


def solve() -> None:
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    c = int(input_data[1])
    weights = list(map(int, input_data[2:]))

    # 1. 물건을 두 그룹으로 나눔
    mid = n // 2
    left_weights = weights[:mid]
    right_weights = weights[mid:]

    # 2. 각 그룹의 모든 가능한 무게 합 생성
    left_sums = get_subset_sums(left_weights)
    right_sums = get_subset_sums(right_weights)

    # 3. 이분 탐색을 위해 한쪽 정렬
    right_sums.sort()

    # 4. 조합 찾기
    answer = 0
    for l_sum in left_sums:
        if l_sum <= c:
            # c - l_sum 이하인 무게가 right_sums에 몇 개 있는지 확인
            target = c - l_sum
            answer += bisect_right(right_sums, target)

    print(answer)


if __name__ == "__main__":
    solve()