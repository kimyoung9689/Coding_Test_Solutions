import sys
from collections import deque
from typing import Deque, List

# 입력 속도 최적화
def read_input_line():
    """한 줄을 읽고 공백으로 나눈 문자열 리스트를 반환"""
    return sys.stdin.readline().split()

def solve():
    """queuestack 문제를 해결하는 메인 함수"""
    
    try:
        # N: 자료구조의 개수
        n: int = int(sys.stdin.readline())

        # A: 자료구조 타입 (0: 큐, 1: 스택)
        a_str: List[str] = read_input_line() 

        # B: 초기 원소
        b_str: List[str] = read_input_line() 

        # 큐 원소만 모아서 저장할 덱(Deque)
        queue_elements: Deque[int] = deque()
        
        # 큐가 하나라도 있는지 미리 확인
        is_queue_exists: bool = False
        
        # B와 A를 순회하며 큐 원소만 덱에 추가
        for i in range(n):
            if a_str[i] == '0':  # 큐인 경우
                is_queue_exists = True
                # B[i]를 덱에 추가 (int로 변환)
                queue_elements.append(int(b_str[i]))
        
        # M: 삽입할 수열의 길이
        m: int = int(sys.stdin.readline())

        # C: 삽입할 원소
        c_str: List[str] = read_input_line()
    except Exception:
        # 입력이 제대로 안 들어왔다면 종료
        return

    results: List[str] = []

    # C 수열의 원소를 차례대로 queuestack에 삽입
    for insert_val_str in c_str:
        insert_val: int = int(insert_val_str)
        pop_val: int
        
        # 1. 반환 값 결정
        if is_queue_exists:
            # 큐가 있는 경우: 덱의 맨 뒤 원소(초기값 중 가장 나중에 있던 큐의 원소)가 튀어나옴
            if queue_elements:
                 pop_val = queue_elements.pop()
            else:
                 # 덱이 비었으면 새로 들어온 원소(insert_val)가 튀어나와야 함
                 pop_val = insert_val
        else:
            # 모두 스택인 경우: 삽입값(insert_val)이 그대로 리턴됨 (예제 2)
            pop_val = insert_val

        results.append(str(pop_val))

        # 2. 새로운 삽입 원소는 덱의 맨 앞에 삽입 (다음에 튀어나갈 위치)
        if is_queue_exists:
            queue_elements.appendleft(insert_val)
        
        # 참고: 모두 스택이라면 덱에 삽입할 필요가 없음.
        # 왜냐하면 새로운 삽입 원소는 항상 그 자리에서 다시 튀어나와 리턴되기 때문.

    # 결과를 공백으로 구분하여 한 번에 출력
    sys.stdout.write(" ".join(results) + "\n")

if __name__ == "__main__":
    solve()