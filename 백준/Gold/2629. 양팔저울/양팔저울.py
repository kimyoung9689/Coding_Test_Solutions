import sys
from typing import List, Set


def solve() -> None:
    # 입력 받기
    num_weights: int = int(sys.stdin.readline())
    weights: List[int] = list(map(int, sys.stdin.readline().split()))
    num_marbles: int = int(sys.stdin.readline())
    marbles: List[int] = list(map(int, sys.stdin.readline().split()))

    # 측정 가능한 무게를 저장할 집합 (DP)
    # 초기값은 0 (아무것도 안 올린 상태)
    possible_weights: Set[int] = {0}

    for weight in weights:
        temp_set: Set[int] = set()
        for w in possible_weights:
            # 1. 저울의 반대편에 추가하는 경우
            temp_set.add(w + weight)
            # 2. 저울의 같은 편에 추가하는 경우 (차이 계산)
            temp_set.add(abs(w - weight))
            # 3. 추가하지 않는 경우 (이미 possible_weights에 있음)
            temp_set.add(w)
        possible_weights = temp_set

    # 결과 출력
    results: List[str] = []
    for marble in marbles:
        if marble in possible_weights:
            results.append("Y")
        else:
            results.append("N")

    print(" ".join(results))


if __name__ == "__main__":
    solve()