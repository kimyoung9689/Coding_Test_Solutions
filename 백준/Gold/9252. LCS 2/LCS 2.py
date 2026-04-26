import sys

def solve() -> None:
    # 입력 처리
    str1: str = sys.stdin.readline().strip()
    str2: str = sys.stdin.readline().strip()
    
    n: int = len(str1)
    m: int = len(str2)
    
    # DP 테이블 초기화 (0으로 채워진 (n+1) x (m+1) 행렬)
    dp: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]
    
    # LCS 길이 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    lcs_length: int = dp[n][m]
    print(lcs_length)
    
    # LCS 문자열 추적
    if lcs_length > 0:
        result: list[str] = []
        curr_i: int = n
        curr_j: int = m
        
        while curr_i > 0 and curr_j > 0:
            if str1[curr_i - 1] == str2[curr_j - 1]:
                result.append(str1[curr_i - 1])
                curr_i -= 1
                curr_j -= 1
            else:
                if dp[curr_i - 1][curr_j] >= dp[curr_i][curr_j - 1]:
                    curr_i -= 1
                else:
                    curr_j -= 1
        
        # 역순으로 담겼으므로 뒤집어서 출력
        print("".join(reversed(result)))

if __name__ == "__main__":
    solve()