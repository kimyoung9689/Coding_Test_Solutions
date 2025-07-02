# N 값을 입력받기
N = int(input())

# 결과 문자열을 만들 변수 초기화
result = ""

# N을 4로 나눈 횟수만큼 long 추가
for _ in range(N // 4): # //는 정수 나눗셈. 몫만 가져옴
    result += "long "

# 마지막에 int 추가
result += "int"

# 결과 출력
print(result)






