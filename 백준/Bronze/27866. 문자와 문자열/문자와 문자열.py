import sys

# s와 정수i 값 입력 받기
s = sys.stdin.readline().strip()
i = int(sys.stdin.readline().strip())

# i번째 글자 출력
print(s[i-1])