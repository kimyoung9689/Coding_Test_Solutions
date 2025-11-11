import sys
# 입력 명령 수가 많으므로 sys.stdin.readline 사용
input = sys.stdin.readline

# 명령의 수 N 입력
N = int(input())
# 큐 역할을 할 리스트 초기화
queue = []
# 큐의 맨 앞(pop 대상)을 가리킬 인덱스
head = 0

# N개의 명령 처리
for _ in range(N):
    # 명령 한 줄 입력
    command = input().split()
    
    # 현재 큐에 저장된 실제 원소의 개수 (뒤 인덱스 - 앞 인덱스)
    # len(queue)는 리스트 전체 크기, len(queue) - head가 현재 큐 크기
    current_size = len(queue) - head

    if command[0] == 'push':
        # 정수 X를 큐의 끝에 추가
        queue.append(int(command[1]))
    
    elif command[0] == 'pop':
        if current_size == 0:
            # 큐가 비어있으면 -1 출력
            print(-1)
        else:
            # 큐의 맨 앞 원소 출력 (head가 가리키는 원소)
            print(queue[head])
            # head 인덱스를 1 증가시켜 맨 앞 원소를 제거한 효과
            head += 1
            
    elif command[0] == 'size':
        # 큐에 들어있는 정수의 개수 출력
        print(current_size)
        
    elif command[0] == 'empty':
        if current_size == 0:
            # 큐가 비어있으면 1 출력
            print(1)
        else:
            # 큐가 비어있지 않으면 0 출력
            print(0)
            
    elif command[0] == 'front':
        if current_size == 0:
            # 큐가 비어있으면 -1 출력
            print(-1)
        else:
            # 큐의 가장 앞에 있는 정수 출력 (head가 가리키는 원소)
            print(queue[head])
            
    elif command[0] == 'back':
        if current_size == 0:
            # 큐가 비어있으면 -1 출력
            print(-1)
        else:
            # 큐의 가장 뒤에 있는 정수 출력 (리스트의 마지막 원소)
            print(queue[-1])