import sys


def solve() -> None:
    """
    이분 탐색을 이용해 K번째 수를 찾는 함수
    """
    # 입력 받기
    try:
        line1 = sys.stdin.readline()
        line2 = sys.stdin.readline()
        
        if not line1 or not line2:
            return
            
        n: int = int(line1.strip())
        k: int = int(line2.strip())
    except ValueError:
        return

    # 이분 탐색 범위 설정
    start: int = 1
    end: int = k
    answer: int = 0

    while start <= end:
        mid: int = (start + end) // 2
        
        # mid보다 작거나 같은 숫자의 개수 세기
        count: int = 0
        for i in range(1, n + 1):
            # i행에서 mid보다 작거나 같은 수의 개수는 mid // i
            # 단, 한 행의 최대 개수는 n개임
            count += min(mid // i, n)
        
        if count >= k:
            # 개수가 k보다 크거나 같으면 일단 정답 후보로 저장하고 더 작은 쪽 탐색
            answer = mid
            end = mid - 1
        else:
            # 개수가 부족하면 더 큰 쪽 탐색
            start = mid + 1

    print(answer)


if __name__ == "__main__":
    solve()