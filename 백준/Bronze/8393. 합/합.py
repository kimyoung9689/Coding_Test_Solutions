# 사용자에게 입력 받기
n = int(input())

# 합계 저장할 변수 0으로 초기화
total_sum = 0

# 1부터 n까지 숫자 반복하고 1부터 n까지 정수 순서대로 생성
for i in range(1, n + 1):
    total_sum += i 

# 합계 저장한 변수 출력
print(total_sum)