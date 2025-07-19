import sys

# n: 바구니 총 개수, m: 공을 바꾸는 횟수 입력 받기
n, m = map(int, sys.stdin.readline().split())

# 바구니 번호 리스트 생성
balls = [i for i in range(1, n+1)]

# m번 공을 바꾼다.
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())

    # i번 바구니와 j번 바구니의 공을 바꾼다.
    balls[i-1], balls[j-1] = balls[j-1], balls[i-1]

# 바구니 번호 출력
print(' '.join(map(str, balls)))


# 리스트 컴프리헨션이라는 파이썬 문법

# balls = [] # 빈 리스트를 먼저 만들어
for i in range(1, n + 1): # 1부터 n까지 숫자를 하나씩 가져와서
    balls.append(i) # 리스트에 추가해줘

# 이게 일반적인 방법이라면 리스트 컴프리헨션으로 줄였을때

# balls = [i for i in range(1, n+1)] 이다.

# i는 표현식 부분. for 루프에서 가져온 i 값을 그대로 리스트에 넣겠다는 뜻
#range(1, n+1)에서 1을 가져오면 i가 1이 되고, 이 1을 리스트에 넣고.
#다음에 2를 가져오면 i가 2가 되고, 이 2를 리스트에 넣고
# 이렇게 반복해서 리스트에 1부터 n까지 숫자를 차례대로 넣어줘
# 이렇게 하면 코드도 간결해지고 읽기 쉬우며 속도도 빠랄진다.