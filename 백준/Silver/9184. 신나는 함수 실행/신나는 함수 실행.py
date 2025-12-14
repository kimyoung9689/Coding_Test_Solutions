# DP 테이블 선언. 최대 인덱스는 20이므로 크기는 21x21x21
# 모두 0으로 초기화
# a, b, c가 0부터 20까지의 값을 가질 때의 결과를 저장
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(a: int, b: int, c: int) -> int:
    """w(a, b, c) 재귀 함수를 DP(메모이제이션)로 구현"""

    # 종료 조건: 셋 중 하나라도 0 이하이면 1 반환
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    # 제한 조건: 셋 중 하나라도 20을 초과하면 w(20, 20, 20) 호출
    # 이 경우 a, b, c는 20이므로, 아래 DP 테이블 범위(0~20) 안에 들게 됨
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # 메모이제이션: 이미 계산된 값이면 테이블에서 찾아 반환
    # a, b, c가 모두 1 이상 20 이하인 경우에만 DP 테이블 사용
    if dp[a][b][c] != 0:
        return dp[a][b][c]

    # 조건 3: a < b < c
    if a < b and b < c:
        # 공식: w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        result = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    
    # 조건 4: 그 외의 경우
    else:
        # 공식: w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        result = (
            w(a - 1, b, c)
            + w(a - 1, b - 1, c)
            + w(a - 1, b, c - 1)
            - w(a - 1, b - 1, c - 1)
        )

    # 계산된 결과를 DP 테이블에 저장
    dp[a][b][c] = result
    
    # 결과 반환
    return result

# 메인 실행 부분
import sys
# 입력 속도 개선
input = sys.stdin.read

# 한 번에 모든 입력을 읽어와 공백 기준으로 분리
data = input().split()
results = []
i = 0

# 입력 데이터가 남아있는 동안 반복
while i < len(data):
    # a, b, c 값을 정수로 변환
    a = int(data[i])
    b = int(data[i+1])
    c = int(data[i+2])
    
    # -1 -1 -1이 입력의 마지막
    if a == -1 and b == -1 and c == -1:
        break
    
    # w(a, b, c) 계산
    value = w(a, b, c)
    
    # 출력 형식에 맞게 결과 저장
    results.append(f"w({a}, {b}, {c}) = {value}")
    
    # 다음 세 개의 숫자로 이동
    i += 3

# 저장된 모든 결과를 한 번에 출력
sys.stdout.write('\n'.join(results) + '\n')