# 값 입력 받기
word = input()

# 단어를 뒤집어도 같은지 확인
if word == word[::-1]:
  print(1) # 같으면 1 출력
else:
  print(0) # 다르면 0 출력