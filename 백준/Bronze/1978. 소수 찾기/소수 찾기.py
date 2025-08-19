def is_prime(n):
    # 1은 소수가 아니므로 False 반환
    if n < 2:
        return False
    # 2부터 n-1까지의 모든 수로 n 나누기
    for i in range(2, n):
        if n % i == 0:
            return False
    # 나누어 떨어지는 수가 없으면 소수이므로 True 반환
    return True

# 소수의 개수 입력 받기
n = int(input())
# 두 번째 줄의 입력 리스트로 저장
numbers = list(map(int, input().split()))

prime_count = 0
# 입력받은 리스트의 각 숫자 확인
for num in numbers:
    if is_prime(num):
        prime_count += 1

print(prime_count)