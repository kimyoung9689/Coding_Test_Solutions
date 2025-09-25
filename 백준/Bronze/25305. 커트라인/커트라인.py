import sys

def solve() -> None:
    """
    커트라인 계산하는 함수
    """
    # 응시자 수 N과 상을 받는 사람 수 k 입력
    try:
        n, k = map(int, sys.stdin.readline().split())
        scores = list(map(int, sys.stdin.readline().split()))
    except ValueError:
        return

    # 점수 내림차순으로 정렬
    scores.sort(reverse=True)

    # k번째 점수 출력
    if 1 <= k <= len(scores):
        print(scores[k-1])
    else:
        # k가 유효 범위에 없을 경우 에러 처리
        print("유효하지 않은 k 값입니다.")

if __name__ == "__main__":
    solve()