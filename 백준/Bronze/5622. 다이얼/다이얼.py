def solve():  # 문제 해결 함수 정의
  word = input()  # 값 입력 받기
  
  # 알파벳에 해당하는 숫자 입력
  dial_times = {
      'A': 3, 'B': 3, 'C': 3,
        'D': 4, 'E': 4, 'F': 4,
        'G': 5, 'H': 5, 'I': 5,
        'J': 6, 'K': 6, 'L': 6,
        'M': 7, 'N': 7, 'O': 7,
        'P': 8, 'Q': 8, 'R': 8, 'S': 8,
        'T': 9, 'U': 9, 'V': 9,
        'W': 10, 'X': 10, 'Y': 10, 'Z': 10
    }
    
  total_time = 0 # 총 시간 0으로 초기화

  for char in word: # 각 글자 반복
      total_time += dial_times[char] # 글자별로 시간 더하기

  print(total_time) # 출력

solve() # 함수 실행

# 소문자로도 하고 싶으면 word 값 입력받는 곳 아래에
# word = word.upper() 코드 넣어주면 소문자로도 적용이 된다.