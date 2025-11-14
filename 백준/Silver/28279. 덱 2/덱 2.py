import sys
from collections import deque
from typing import Deque

# 입력이 많으므로 sys.stdin.readline 사용
input = sys.stdin.readline

# 명령의 수 N을 읽음
try:
    N: int = int(input())
except ValueError:
    N = 0

# 덱 초기화
d: Deque[int] = deque()

for _ in range(N):
    # 명령 한 줄을 읽고 공백 기준으로 분리
    command: list[str] = input().split()
    
    # 명령 번호
    cmd_num: str = command[0]

    if cmd_num == '1':
        # 1 X: 정수 X를 덱의 앞에 넣음
        d.appendleft(int(command[1]))
    
    elif cmd_num == '2':
        # 2 X: 정수 X를 덱의 뒤에 넣음
        d.append(int(command[1]))
    
    elif cmd_num == '3':
        # 3: 맨 앞 정수를 빼고 출력, 덱이 비었으면 -1
        if d:
            print(d.popleft())
        else:
            print(-1)
    
    elif cmd_num == '4':
        # 4: 맨 뒤 정수를 빼고 출력, 덱이 비었으면 -1
        if d:
            print(d.pop())
        else:
            print(-1)
            
    elif cmd_num == '5':
        # 5: 덱에 들어있는 정수의 개수를 출력
        print(len(d))
        
    elif cmd_num == '6':
        # 6: 덱이 비어있으면 1, 아니면 0을 출력
        if not d:
            print(1)
        else:
            print(0)
            
    elif cmd_num == '7':
        # 7: 맨 앞 정수를 출력, 덱이 비었으면 -1
        if d:
            print(d[0])
        else:
            print(-1)
            
    elif cmd_num == '8':
        # 8: 맨 뒤 정수를 출력, 덱이 비었으면 -1
        if d:
            print(d[-1])
        else:
            print(-1)