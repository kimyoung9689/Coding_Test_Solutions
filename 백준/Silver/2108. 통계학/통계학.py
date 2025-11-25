import sys
# 입력 속도를 빠르게 하기 위해 사용
input = sys.stdin.readline

def solve():
    """산술평균, 중앙값, 최빈값, 범위를 계산하여 출력한다."""
    try:
        n = int(input())
    except:
        return

    # 입력된 N개의 수를 리스트에 저장
    numbers = [int(input()) for _ in range(n)]

    # 1. 산술평균: 합계를 N으로 나누고 반올림하여 정수로 출력
    avg = sum(numbers) / n
    # 소수점 첫째 자리에서 반올림 (예: -0.333... -> 0)
    print(int(round(avg)))

    # 2. 중앙값: 리스트를 정렬한 후 가운데 값
    numbers.sort()
    print(numbers[n // 2])

    # 3. 최빈값: 카운팅 배열을 이용해 빈도 계산 (-4000 ~ 4000)
    # 인덱스 0이 -4000, 8000이 4000에 해당
    counts = [0] * 8001
    for num in numbers:
        counts[num + 4000] += 1

    # 최대 빈도수를 찾음
    max_freq = max(counts)
    modes = []

    # 최빈값을 가지는 수들을 오름차순으로 modes에 추가
    for i, count in enumerate(counts):
        if count == max_freq:
            modes.append(i - 4000)
            # 최빈값이 여러 개일 때 두 번째로 작은 값까지만 찾으면 됨
            if len(modes) == 2:
                break

    # 출력: 최빈값이 여러 개면 두 번째로 작은 값, 아니면 첫 번째 값
    if len(modes) > 1:
        print(modes[1])
    else:
        print(modes[0])

    # 4. 범위: 최댓값 - 최솟값
    # 이미 정렬된 리스트의 가장 큰 값(마지막)과 가장 작은 값(처음) 사용
    print(numbers[-1] - numbers[0])

if __name__ == "__main__":
    solve()