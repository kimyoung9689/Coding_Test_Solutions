x = int(input())

# 현재 보고 있는 줄
line = 0

# 현재까지 분수의 총 개수
count = 0

# x가 속한 line 찾기
while count < x:  # x가 count보다 크면 반복
  line += 1       # line에 1씩 더한다.
  count += line   # count에 line만큼 더한다.

# x가 속한 줄의 시작 위치 계산
start_index = count - line + 1

# 분자, 분모 계산
if line % 2 == 0: # 짝수 줄일 때
  numerator = x - start_index + 1
  denominator = line - (x - start_index)
else: # 홀수 줄일 때
  numerator = line - (x - start_index)
  denominator = x - start_index + 1

print(f"{numerator}/{denominator}")