import sys
from typing import List

# 입력 빠르게
input = sys.stdin.readline

# 전역 변수
count: int = 0      # 저장 횟수
k: int = 0          # 목표 횟수 K
result: int = -1    # K번째 저장된 값


def merge(a: List[int], p: int, q: int, r: int) -> None:
    """A[p..q]와 A[q+1..r]을 병합"""
    global count, k, result
    
    tmp: List[int] = [0] * (r - p + 2)
    i, j, t = p, q + 1, 1

    # 작은 값 tmp에 저장
    while i <= q and j <= r:
        if a[i] <= a[j]:
            tmp[t] = a[i]
            i += 1
        else:
            tmp[t] = a[j]
            j += 1
        t += 1

    # 남은 왼쪽 배열 처리
    while i <= q:
        tmp[t] = a[i]
        t += 1
        i += 1

    # 남은 오른쪽 배열 처리
    while j <= r:
        tmp[t] = a[j]
        t += 1
        j += 1

    # 결과를 A[p..r]에 저장 (K번째 저장 확인)
    i, t = p, 1
    while i <= r:
        if count < k:
            a[i] = tmp[t]
            count += 1
            if count == k:
                result = a[i]  # K번째 값 기록
        i += 1
        t += 1


def merge_sort(a: List[int], p: int, r: int) -> None:
    """배열 A[p..r]을 병합 정렬"""
    if p < r:
        q: int = (p + r) // 2
        
        merge_sort(a, p, q)      # 전반부 정렬
        merge_sort(a, q + 1, r)  # 후반부 정렬
        merge(a, p, q, r)        # 병합


def solve() -> None:
    """입력 처리 및 정렬 실행"""
    global k
    
    # N, K 입력
    try:
        data: List[str] = input().split()
        if not data:
            return
        n, k_val = map(int, data)
    except EOFError:
        return
    
    # 배열 A 입력
    try:
        a: List[int] = list(map(int, input().split()))
    except EOFError:
        return

    k = k_val

    # 0부터 N-1 인덱스까지 정렬 시작
    merge_sort(a, 0, n - 1)

    # 결과 출력
    print(result)


if __name__ == "__main__":
    solve()