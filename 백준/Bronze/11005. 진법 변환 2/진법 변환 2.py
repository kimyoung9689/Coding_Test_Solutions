# 입력받은 N과 B 정수로 바꿔주기
N, B = map(int,input().split())

# B진법으로 변환된 결과 저장할 빈 문자열 생성
result = ""

# 0부터 35까지의 숫자를 문자열로 저장
nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# N이 0보다 클 때까지 반복
while N > 0:
   remainder = N % B          # N을 B로 나눈 나머지 구하기 
   result += nums[remainder]  # 나머지 result에 추가
   N = N // B                 # N을 B로 나눈 몫으로 업데이트

# result는 나머지를 뒤에서부터 추가했기에 뒤집어서 출력
print(result[::-1])