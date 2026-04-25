import sys
from bisect import bisect_left
from typing import List

def solve() -> None:
    n: int = int(sys.stdin.readline())
    a: List[int] = list(map(int, sys.stdin.readline().split()))

    # LIS의 길이를 구하기 위한 리스트와 각 원소의 위치 기록
    lis: List[int] = []
    # (값, 해당 값의 LIS에서의 인덱스)를 저장
    pos: List[tuple[int, int]] = []

    for val in a:
        if not lis or val > lis[-1]:
            lis.append(val)
            pos.append((val, len(lis) - 1))
        else:
            idx = bisect_left(lis, val)
            lis[idx] = val
            pos.append((val, idx))

    # 결과 출력
    print(len(lis))

    # 역추적을 통해 실제 부분 수열 구하기
    result: List[int] = []
    target_idx = len(lis) - 1
    
    for i in range(n - 1, -1, -1):
        if pos[i][1] == target_idx:
            result.append(pos[i][0])
            target_idx -= 1
            
    print(*(result[::-1]))

if __name__ == "__main__":
    solve()