import sys

def solve() -> None:
    # 빠른 입력을 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    
    # 원본 데이터를 2차원 리스트로 저장 (인덱스 계산 편의를 위해 n+1 크기)
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    idx = 2
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            matrix[i][j] = int(input_data[idx])
            idx += 1
            
    # 2차원 누적 합 배열 생성
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i][j]
            
    # 질의 처리
    results = []
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input_data[idx:idx+4])
        idx += 4
        # 구간 합 공식 적용
        ans = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
        results.append(str(ans))
        
    # 결과 한 번에 출력
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()