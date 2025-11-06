# 명령의 수 N을 입력받음
import sys
# N = int(sys.stdin.readline())
# 빠른 입력을 위해 sys.stdin.readline 사용
try:
    N = int(sys.stdin.readline())
except:
    N = 0

stack = []  # 스택으로 사용할 리스트
results = []  # 출력 결과를 저장할 리스트

# N번 반복하며 명령 처리
for _ in range(N):
    # command_line = sys.stdin.readline().split()
    try:
        command_line = sys.stdin.readline().split()
    except:
        continue

    # 명령을 정수로 변환
    command_type = int(command_line[0])

    # 1: push X
    if command_type == 1:
        # 정수 X를 스택 끝에 추가 (push)
        stack.append(int(command_line[1]))
    # 2: pop
    elif command_type == 2:
        # 스택이 비었는지 확인
        if stack:
            # 맨 위 원소를 빼내고 결과에 추가 (pop)
            results.append(stack.pop())
        else:
            # 비었으면 -1
            results.append(-1)
    # 3: size
    elif command_type == 3:
        # 스택 크기를 결과에 추가
        results.append(len(stack))
    # 4: empty
    elif command_type == 4:
        # 스택이 비었으면 1, 아니면 0
        results.append(1 if not stack else 0)
    # 5: top
    elif command_type == 5:
        # 스택이 비었는지 확인
        if stack:
            # 맨 위 원소를 출력만 (top)
            results.append(stack[-1])
        else:
            # 비었으면 -1
            results.append(-1)

# 모든 결과를 한 번에 출력
sys.stdout.write('\n'.join(map(str, results)) + '\n')