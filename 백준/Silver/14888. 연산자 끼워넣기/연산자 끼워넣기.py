import sys
from typing import List

# 입력 함수 재정의
input = sys.stdin.readline

# 최대/최소 결과 초기값 설정
MAX_RESULT = -1_000_000_000
MIN_RESULT = 1_000_000_000

def solve() -> None:
    global MAX_RESULT, MIN_RESULT

    try:
        n: int = int(input()) # 수의 개수 N
    except:
        return

    numbers: List[int] = list(map(int, input().split())) # 숫자 리스트
    operators: List[int] = list(map(int, input().split())) # 연산자 개수 [+, -, *, /]

    def dfs(idx: int, current_value: int, ops: List[int]) -> None:
        global MAX_RESULT, MIN_RESULT

        if idx == n: # 종료 조건: 모든 숫자 사용 완료
            MAX_RESULT = max(MAX_RESULT, current_value)
            MIN_RESULT = min(MIN_RESULT, current_value)
            return

        # 연산자 4종류 순회 (0:+, 1:-, 2:*, 3:/)
        for i in range(4):
            if ops[i] > 0: # 남은 연산자가 있을 경우
                ops[i] -= 1 # 연산자 사용
                next_number: int = numbers[idx]
                next_value: int

                if i == 0:  # 덧셈
                    next_value = current_value + next_number
                elif i == 1:  # 뺄셈
                    next_value = current_value - next_number
                elif i == 2:  # 곱셈
                    next_value = current_value * next_number
                else:  # 나눗셈
                    # C++14 정수 나눗셈 규칙 적용
                    if current_value < 0:
                        next_value = -(abs(current_value) // next_number)
                    else:
                        next_value = current_value // next_number

                dfs(idx + 1, next_value, ops) # 다음 재귀 호출

                ops[i] += 1 # 백트래킹: 연산자 개수 복구

    # DFS 시작 (첫 번째 숫자부터 시작, 인덱스 1부터 연산)
    dfs(1, numbers[0], operators)

    print(MAX_RESULT)
    print(MIN_RESULT)

if __name__ == "__main__":
    solve()