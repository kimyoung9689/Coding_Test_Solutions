import sys

# t 값 입력 받기
t = int(sys.stdin.readline().strip())

# t 개수 만큼 반복
for _ in range(t):
    text = sys.stdin.readline().strip()
    print(text[0] + text[-1]) # 첫글자와 마지막 글자 출력