from typing import List, Set, Tuple, Optional

# 스도쿠 보드 타입 정의 (9x9 정수 리스트)
Board = List[List[int]]


def solve_sudoku_fast(
    board: Board,
    zeros: List[Tuple[int, int]],
    idx: int,
    rows: List[Set[int]],
    cols: List[Set[int]],
    boxes: List[Set[int]]
) -> bool:
    """
    최적화된 백트래킹으로 스도쿠를 채운다.
    idx: 현재 처리할 빈 칸 (zeros 리스트의 인덱스)
    rows, cols, boxes: 각 행/열/박스에 사용된 숫자를 저장하는 Set 리스트
    """
    if idx == len(zeros):
        # 모든 빈 칸을 다 채웠다.
        return True

    # 현재 처리할 빈 칸 위치
    row, col = zeros[idx]

    # 현재 위치의 3x3 박스 인덱스 (0부터 8까지)
    box_idx: int = (row // 3) * 3 + (col // 3)

    # 1부터 9까지 숫자를 시도한다.
    for num in range(1, 10):
        # 유효성 검사: num이 행, 열, 박스 셋에 없는지 확인 (O(1) 시간)
        if num not in rows[row] and num not in cols[col] and num not in boxes[box_idx]:

            # 1. 보드에 숫자를 채운다.
            board[row][col] = num

            # 2. Set에 숫자를 추가한다.
            rows[row].add(num)
            cols[col].add(num)
            boxes[box_idx].add(num)

            # 3. 다음 빈 칸으로 이동 (idx + 1)하여 재귀 호출
            if solve_sudoku_fast(board, zeros, idx + 1, rows, cols, boxes):
                return True

            # 4. 실패 시 백트래킹: 보드를 되돌리고 Set에서 숫자를 제거한다.
            board[row][col] = 0
            rows[row].remove(num)
            cols[col].remove(num)
            boxes[box_idx].remove(num)

    return False  # 1-9까지 모두 시도했지만 실패


def print_board(board: Board) -> None:
    """
    스도쿠 보드를 문제 형식에 맞춰 출력한다.
    """
    for row in board:
        print(" ".join(map(str, row)))


def main() -> None:
    """
    입력을 받고 스도쿠를 푼 후 결과를 출력하는 메인 함수
    """
    board: Board = []
    zeros: List[Tuple[int, int]] = []
    
    # Set 자료 구조 초기화
    # 각 인덱스(0~8)가 행/열/박스를 나타내며, Set에 사용된 숫자를 저장한다.
    rows: List[Set[int]] = [set() for _ in range(9)]
    cols: List[Set[int]] = [set() for _ in range(9)]
    boxes: List[Set[int]] = [set() for _ in range(9)]

    # 입력 처리 및 초기 Set 채우기
    for r in range(9):
        line: List[int] = list(map(int, input().split()))
        for c in range(9):
            num: int = line[c]
            if num != 0:
                # 이미 채워진 숫자를 Set에 기록
                box_idx: int = (r // 3) * 3 + (c // 3)
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_idx].add(num)
            else:
                zeros.append((r, c))  # 빈 칸 위치 저장
        board.append(line)

    # 스도쿠 풀이 시작 (0번째 빈 칸부터 시작)
    # MRV 최적화는 제거했어. PyPy3에서 MRV 계산 오버헤드 없이 Set 기반 O(1) 탐색이 더 빠를 때가 많아.
    solve_sudoku_fast(board, zeros, 0, rows, cols, boxes)

    # 결과 출력
    print_board(board)


if __name__ == "__main__":
    main()