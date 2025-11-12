import sys
from collections import deque

# 입력 받기
N = int(sys.stdin.readline())

# 1부터 N까지의 숫자로 덱(Deque) 초기화
cards = deque(range(1, N + 1)) # 카드 1, 2, 3, ... N 준비

# 카드가 한 장 남을 때까지 반복
while len(cards) > 1:
    # 1. 제일 위에 있는 카드를 버리기
    cards.popleft() # 맨 앞 카드 버림
    
    # 카드가 한 장 남았으면 루프 종료
    if len(cards) == 1:
        break
        
    # 2. 제일 위에 있는 카드를 제일 아래로 옮김
    top_card = cards.popleft() # 맨 앞 카드 꺼냄
    cards.append(top_card) # 꺼낸 카드를 맨 뒤에 넣음

# 마지막에 남은 카드 출력
print(cards[0])