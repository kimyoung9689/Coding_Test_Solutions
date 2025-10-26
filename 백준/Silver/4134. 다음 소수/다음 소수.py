import sys

# 표준 입력을 더 빠르게 읽음
input = sys.stdin.read
# 모든 입력을 문자열로 읽고 공백 기준으로 분리
data = input().split()

# 소수 판별 함수
def is_prime(k):
    if k < 2:
        return False  # 2 미만은 소수 아님
    i = 2
    while i * i <= k:
        if k % i == 0:
            return False  # 나누어 떨어지면 소수 아님
        i += 1
    return True  # 모두 나누어 떨어지지 않으면 소수

# 테스트 케이스 개수
T = int(data[0])
# 결과 저장 리스트
results = []
# 입력 데이터 인덱스
current_index = 1

# 각 테스트 케이스 처리
for _ in range(T):
    # n 값
    n = int(data[current_index])
    current_index += 1
    
    # n부터 시작해서 소수를 찾음
    k = n
    while True:
        if is_prime(k):
            results.append(str(k)) # 찾으면 결과에 추가
            break
        k += 1 # 1씩 증가시키며 다음 수 확인

# 결과 출력
sys.stdout.write('\n'.join(results) + '\n')