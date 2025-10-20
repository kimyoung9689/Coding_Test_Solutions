# A와 B의 원소 개수 입력 (사용하지 않지만 입력 형식을 맞춤)
_a_count, _b_count = map(int, input().split())

# 집합 A의 원소 입력
A = set(map(int, input().split()))
# 집합 B의 원소 입력
B = set(map(int, input().split()))

# A-B (A에만 있는 원소)의 개수
only_A = len(A - B)
# B-A (B에만 있는 원소)의 개수
only_B = len(B - A)

# 대칭 차집합의 원소 개수 = (A-B)의 개수 + (B-A)의 개수
result = only_A + only_B

# 결과 출력
print(result)