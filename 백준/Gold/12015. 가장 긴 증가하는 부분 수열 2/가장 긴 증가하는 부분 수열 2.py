import sys
from bisect import bisect_left
from typing import List

def solve() -> None:
    # 입력 속도를 위해 sys.stdin.read 사용
    input_data: List[str] = sys.stdin.read().split()
    if not input_data:
        return
    
    n: int = int(input_data[0])
    # n이 1,000,000이므로 리스트 컴프리헨션으로 정수 변환
    a: List[int] = [int(x) for x in input_data[1:]]

    # LIS(가장 긴 증가하는 부분 수열)를 유지할 리스트
    lis: List[int] = []

    for num in a:
        # 이진 탐색으로 num이 들어갈 위치를 찾음 (O(log N))
        pos: int = bisect_left(lis, num)
        
        # 만약 num이 lis의 모든 요소보다 크다면 맨 뒤에 추가
        if pos == len(lis):
            lis.append(num)
        # 그렇지 않다면 해당 위치의 값을 num으로 교체 (더 작은 값으로 유지)
        else:
            lis[pos] = num

    # 최종적인 lis 리스트의 길이가 정답
    print(len(lis))

if __name__ == "__main__":
    solve()