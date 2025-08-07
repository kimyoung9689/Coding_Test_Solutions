import sys

# 5개 단어 저장할 리스트 생성
words = []
for _ in range(5):
  # 한 줄씩 입력 받아 리스트에 추가
  words.append(sys.stdin.readline().strip())

# 가장 긴 단어 길이 찾기
# 이 길이만큼 세로로 반복해서 글자 읽기
max_length = 0
for word in words:
  if len(word) > max_length:
    max_length = len(word)

# 세로로 읽을 글자 넣을 빈 문자열 준비
result = ''

# 세로로 글자 읽기
for j in range(max_length): # 세로로 읽을 열을 먼저 반복
    for i in range(5):      # 세로줄 안에서 위에서 아래로 읽을 행을 나중에 반복
        if j < len(words[i]):
            result += words[i][j]
print(result)