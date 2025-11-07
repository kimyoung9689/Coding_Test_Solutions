import sys
# 입력 속도를 빠르게 하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# K는 입력받을 숫자의 개수
K = int(input())

# 숫자를 저장할 리스트 (스택으로 사용)
stack = []

# K번 반복
for _ in range(K):
    # 숫자 입력
    number = int(input())
    
    # 입력된 숫자가 0이면
    if number == 0:
        # 가장 최근에 추가된 숫자 제거 (pop)
        stack.pop()
    # 0이 아니면
    else:
        # 리스트에 숫자 추가 (append)
        stack.append(number)

# 최종적으로 남아있는 모든 수의 합 출력
print(sum(stack))