import sys

def solve():
    # 입력을 빠르게 받음
    try:
        N = int(sys.stdin.readline())
    except:
        N = 0
        
    if N < 1:
        print(0)
        return

    # 정답 횟수
    count = 0
    
    # 공격 가능한 위치를 표시할 세 개의 배열을 False로 초기화
    # 1. col_check[i]: i열에 퀸이 있는지 (세로)
    # 2. right_diag_check[i]: / 모양 대각선에 퀸이 있는지
    # 3. left_diag_check[i]: \ 모양 대각선에 퀸이 있는지

    # 열은 N개가 필요
    col_check = [False] * N
    
    # 대각선은 2N - 1개가 필요 (N=8일 때 0~14번까지 필요)
    # 오른쪽 대각선 (/)은 '행 + 열' 값이 같음 (r + c)
    right_diag_check = [False] * (2 * N - 1)
    
    # 왼쪽 대각선 (\)은 '행 - 열 + N - 1' 값이 같음 (r - c + N - 1)
    left_diag_check = [False] * (2 * N - 1)

    # 
    # 위 이미지는 대각선 검사를 위한 '행 + 열'과 '행 - 열' 값의 패턴을 보여줄 거야.

    # r번째 행에 퀸을 놓는 백트래킹 함수
    def n_queens_optimized(r):
        nonlocal count
        
        # 모든 행에 퀸을 다 놓았으면 끝!
        if r == N:
            count += 1
            return
            
        # r번째 행의 모든 열(c)을 시도
        for c in range(N):
            # 대각선 인덱스 계산
            # '/' 대각선: 행(r) + 열(c)
            diag_r = r + c
            # '\' 대각선: 행(r) - 열(c) + N - 1 (음수가 나오지 않게 N-1을 더함)
            diag_l = r - c + N - 1
            
            # 1. 같은 열(c)에 퀸이 없고 (col_check[c] == False)
            # 2. 같은 '/' 대각선에 퀸이 없고 (right_diag_check[diag_r] == False)
            # 3. 같은 '\' 대각선에 퀸이 없다면 (left_diag_check[diag_l] == False)
            if not col_check[c] and \
               not right_diag_check[diag_r] and \
               not left_diag_check[diag_l]:
                
                # 공격 가능 위치를 True로 설정 (퀸 놓기)
                col_check[c] = True
                right_diag_check[diag_r] = True
                left_diag_check[diag_l] = True
                
                # 다음 행으로 넘어감
                n_queens_optimized(r + 1)
                
                # 백트래킹: 이전에 설정했던 것을 다시 False로 되돌림 (퀸 빼기)
                col_check[c] = False
                right_diag_check[diag_r] = False
                left_diag_check[diag_l] = False

    # 0번째 행부터 시작
    n_queens_optimized(0)
    
    # 최종 결과 출력
    print(count)

# 함수 실행
solve()