
# 숫자 개수 입력 받기
n = int(input())

# 공백 없는 숫자 문자열 입력 받기
number_str = input()

# 숫자 합 저장할 변수 0으로 초기화
total_sum = 0

# 각 문자열 하나씩 보면서 정수로 바꿔줌
for num_str in number_str:
    num_int = int(num_str)
    total_sum += num_int

# 최종 합계 출력
print(total_sum)