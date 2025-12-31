import sys
from typing import List


def solve() -> None:
    # 입력 속도를 위해 sys.stdin.readline 사용
    input_data: List[str] = sys.stdin.read().split()
    
    if not input_data:
        return

    n: int = int(input_data[0])
    k: int = int(input_data[1])
    # 온도 리스트 추출 (PEP 484 타입 힌트 적용)
    temperatures: List[int] = list(map(int, input_data[2:]))

    # 초기 윈도우(첫 K일간의 합) 계산
    current_sum: int = sum(temperatures[:k])
    max_sum: int = current_sum

    # 슬라이딩 윈도우 진행
    for i in range(k, n):
        # 다음 날짜 더하고 가장 오래된 날짜 빼기
        current_sum += temperatures[i] - temperatures[i - k]
        if current_sum > max_sum:
            max_sum = current_sum

    print(max_sum)


if __name__ == "__main__":
    solve()