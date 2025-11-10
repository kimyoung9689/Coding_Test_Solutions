def solve():
    # 학생 수 N은 실제 로직에 불필요
    N = int(input())
    
    # 현재 줄
    current_line = list(map(int, input().split()))

    # 보조 공간 (스택)
    side_stack = []

    # 다음에 받아야 할 번호
    next_required = 1

    # 현재 줄 처리
    while current_line:
        # 1. 현재 줄 맨 앞이 순서 맞으면 통과
        if current_line[0] == next_required:
            current_line.pop(0)
            next_required += 1
        
        # 2. 보조 공간 맨 위가 순서 맞으면 통과
        elif side_stack and side_stack[-1] == next_required:
            side_stack.pop()
            next_required += 1
        
        # 3. 둘 다 아니면 보조 공간으로 이동
        else:
            side_stack.append(current_line.pop(0))

    # 보조 공간 남은 사람 처리
    while side_stack:
        # 순서 맞으면 통과
        if side_stack[-1] == next_required:
            side_stack.pop()
            next_required += 1
        else:
            # 순서 안 맞으면 실패
            print("Sad")
            return

    # 모두 통과
    print("Nice")

solve()