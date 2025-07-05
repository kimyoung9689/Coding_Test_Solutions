# sys 불러오기
import sys

# 숫자로 테스트 케이스 t 값 입력 받기
t = int(sys.stdin.readline().strip())

# 1번 부터 t+1번까지 반복
for i in range(1, t + 1):
    a, b = map(int, sys.stdin.readline().split()) # a, b 값 숫자로 입력 받기
    

    print(f"Case #{i}: {a} + {b} = {a + b}") 



# 처음에 sys불러오는걸 까먹었다.
# t와 a,b 입력 받을 때 int를 넣지 않아 문자열로 받아버렸다.
# strip()는 공백 문자나 줄바꿈 문자를 처리해주는 것
# 여기선 필요 없지만 습관을 들이기 위해 넣어줬다.
# 이런 기본적인거 틀리지 않게 주의하기


