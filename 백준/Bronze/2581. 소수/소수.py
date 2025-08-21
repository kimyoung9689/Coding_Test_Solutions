# 소수 판별 함수
def is_prime(num):
    # 1은 소수가 아니므로 False 반환
    if num < 2:
        return False
    # 2부터 num-1까지 나누어 보면서 나누어떨어지는지 확인
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# M과 N 입력받기
M = int(input())
N = int(input())

# 소수들을 저장할 리스트
prime_numbers = []

# M부터 N까지 반복하며 소수 찾기
for number in range(M, N + 1):
    if is_prime(number):
        prime_numbers.append(number)

# 결과 출력
if len(prime_numbers) > 0:
    # 소수가 있을 경우
    print(sum(prime_numbers))
    print(prime_numbers[0])
else:
    # 소수가 없을 경우
    print(-1)