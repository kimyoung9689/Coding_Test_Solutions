import sys # 모듈 임포트해 표준 입출력 기능 사용

# 테스트 케이스의 개수 입력 받기
t = int(sys.stdin.readline()) 

# 1부터 t까지 반복하여 테스트 케이스를 처리
for i in range(1, t + 1):
    # 한 줄에 공백으로 구분된 두 정수를 입력 받기
    a, b = map(int,sys.stdin.readline().split())

    # f=string 포매팅 기법 사용하여 출력
    print(f"Case #{i}: {a + b}")


# 여기서 케이스 #1이라고 적어서 틀렸었다.
# 이전에는 for _ in range(t)로 0부터 반복되어 출력되기도 함

# 문제 요구사항에 맞춰 1부터 시작하도록 
# for _ in range(t)에서 _는 i로, (t)는 (1, t + 1)로 수정
# 0부터 반복되던것을 1부터 표기하게 변경
# #1은 {i}로 바꿔줌으로써 상황에 따라 숫자가 바뀌게 만들어줌
