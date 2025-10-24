# 첫 번째 분수의 분자 A1, 분모 B1 입력
A1, B1 = map(int, input().split())
# 두 번째 분수의 분자 A2, 분모 B2 입력
A2, B2 = map(int, input().split())

# 두 분수의 합을 통분하여 계산
# 합의 분자 (A1*B2 + A2*B1)
result_A = A1 * B2 + A2 * B1
# 합의 분모 (B1*B2)
result_B = B1 * B2

# 최대공약수(GCD)를 구하는 유클리드 호제법 구현
def get_gcd(a, b):
    # a가 0이 될 때까지 반복
    while b:
        # a, b를 b, a%b로 갱신
        a, b = b, a % b
    # a에 최대공약수가 저장됨
    return a

# 합의 분자와 분모의 최대공약수 계산
gcd = get_gcd(result_A, result_B)

# 기약분수를 얻기 위해 최대공약수로 분자와 분모를 나눔
final_A = result_A // gcd
final_B = result_B // gcd

# 결과 출력
print(final_A, final_B)