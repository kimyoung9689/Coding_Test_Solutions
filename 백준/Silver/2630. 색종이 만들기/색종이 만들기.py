import sys
from typing import List


def solve() -> None:
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n: int = int(input_data[0])
    # 2차원 리스트로 종이 정보 저장
    paper: List[List[int]] = []
    for i in range(n):
        row = list(map(int, input_data[1 + i * n : 1 + (i + 1) * n]))
        paper.append(row)

    white_count: int = 0
    blue_count: int = 0

    def check_color(x: int, y: int, size: int) -> None:
        nonlocal white_count, blue_count
        
        first_color = paper[x][y]
        is_same = True
        
        # 현재 영역이 모두 같은 색인지 확인
        for i in range(x, x + size):
            for j in range(y, y + size):
                if paper[i][j] != first_color:
                    is_same = False
                    break
            if not is_same:
                break
        
        if is_same:
            if first_color == 0:
                white_count += 1
            else:
                blue_count += 1
        else:
            # 색이 다르면 4등분하여 재귀 호출
            new_size = size // 2
            check_color(x, y, new_size)  # 1사분면
            check_color(x, y + new_size, new_size)  # 2사분면
            check_color(x + new_size, y, new_size)  # 3사분면
            check_color(x + new_size, y + new_size, new_size)  # 4사분면

    check_color(0, 0, n)
    
    # 결과 출력
    print(white_count)
    print(blue_count)


if __name__ == "__main__":
    solve()