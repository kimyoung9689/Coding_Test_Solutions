import sys
from typing import List


def solve() -> None:
    # 입력 속도를 높이기 위해 sys.stdin.read 사용
    input_data: List[str] = sys.stdin.read().split()
    
    if not input_data:
        return

    n: int = int(input_data[0])
    s: int = int(input_data[1])
    # 수열 추출 (PEP 484 타입 힌트 적용)
    numbers: List[int] = [int(x) for x in input_data[2:]]

    start: int = 0
    end: int = 0
    current_sum: int = 0
    min_length: float = float('inf')

    # 투 포인터 알고리즘 진행
    while True:
        if current_sum >= s:
            # 합이 S 이상이면 길이를 갱신하고 start를 오른쪽으로 이동
            min_length = min(min_length, end - start)
            current_sum -= numbers[start]
            start += 1
        elif end == n:
            # 더 이상 더할 숫자가 없으면 종료
            break
        else:
            # 합이 S 미만이면 end를 오른쪽으로 이동하며 숫자를 더함
            current_sum += numbers[end]
            end += 1

    # 결과 출력 (합을 만드는 것이 불가능하면 0 출력)
    if min_length == float('inf'):
        print(0)
    else:
        print(int(min_length))


if __name__ == "__main__":
    solve()