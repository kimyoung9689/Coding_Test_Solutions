import sys
from typing import List

def solve() -> None:
    # 입력을 빠르게 받기 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n: int = int(input_data[0])
    # 2차원 리스트로 종이 정보 저장
    board: List[List[int]] = []
    for i in range(n):
        row = list(map(int, input_data[1 + i * n : 1 + (i + 1) * n]))
        board.append(row)

    # 결과 저장용 변수 (-1, 0, 1 순서)
    counts: List[int] = [0, 0, 0]

    def check_and_split(r: int, c: int, size: int) -> None:
        """
        종이가 모두 같은 숫자인지 확인하고, 아니면 9개로 분할함.
        r, c: 시작 좌표, size: 종이 한 변의 길이
        """
        first_val: int = board[r][c]
        
        # 1. 모든 칸이 같은 숫자인지 확인
        is_same: bool = True
        for i in range(r, r + size):
            for j in range(c, c + size):
                if board[i][j] != first_val:
                    is_same = False
                    break
            if not is_same:
                break
        
        # 2. 같은 숫자라면 해당 숫자 카운트 증가
        if is_same:
            counts[first_val + 1] += 1
        else:
            # 3. 다른 숫자가 섞여있다면 9개로 쪼개기 (size // 3)
            next_size: int = size // 3
            for i in range(3):
                for j in range(3):
                    check_and_split(r + i * next_size, c + j * next_size, next_size)

    # 재귀 시작
    check_and_split(0, 0, n)

    # 결과 출력
    for count in counts:
        print(count)

if __name__ == "__main__":
    solve()