# 영수증 총 금액 x 입력 받기
x = int(input())
# 구매한 물건 종류 수 n 입력 받기
n = int(input())

# 직접 계산할 총 금액 0으로 초기화
all_sum = 0

# n번 반복하며 물건 가격 a와 개수 b를 받아서 계산
for _ in range(n):
    a, b = map(int,input().split())
    
    all_sum += (a * b)

# 총 금액 x랑 내가 계산한 금액 같은지 비교
if x == all_sum:
    print("Yes")
else:
    print("No")
    
# 출력할때 yes no 이거 대소문자 구분해야함