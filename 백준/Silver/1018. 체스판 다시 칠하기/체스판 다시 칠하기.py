import sys

def solve():
    """
    체스판 문제 해결 함수
    """
    n, m = map(int, sys.stdin.readline().split())
    board = [sys.stdin.readline().strip() for _ in range(n)]

    min_repaint = float('inf')

    for r_start in range(n - 7):
        for c_start in range(m - 7):
            repaint_w = 0  # 왼쪽 위가 W일 때 칠해야 할 칸
            repaint_b = 0  # 왼쪽 위가 B일 때 칠해야 할 칸

            for r in range(8):
                for c in range(8):
                    # 현재 위치의 실제 색상
                    current_color = board[r_start + r][c_start + c]

                    # (r+c)가 짝수이면 시작점과 같은 색
                    if (r + c) % 2 == 0:
                        # Case 1: W로 시작하는 체스판
                        if current_color != 'W':
                            repaint_w += 1
                        # Case 2: B로 시작하는 체스판
                        if current_color != 'B':
                            repaint_b += 1
                    # (r+c)가 홀수이면 시작점과 다른 색
                    else:
                        # Case 1: 'W'로 시작하는 체스판
                        if current_color != 'B':
                            repaint_w += 1
                        # Case 2: 'B'로 시작하는 체스판
                        if current_color != 'W':
                            repaint_b += 1
            
            # 두 경우 중 더 적은 횟수를 최소값과 비교
            min_repaint = min(min_repaint, repaint_w, repaint_b)
    
    print(min_repaint)

if __name__ == '__main__':
    solve()