import sys
# 입력 속도를 빠르게 하기 위해 sys.stdin.readline 사용
# map(int, ...)을 이용해 N과 M을 정수로 받는다.
input: '() -> str' = sys.stdin.readline
N, M = map(int, input().split())

# 완성된 수열을 저장할 리스트 (M 길이)
# M의 최대 길이가 7이므로, 리스트 대신 튜플을 사용해도 되지만,
# 수정이 필요할 수 있는 백트래킹 과정에서 리스트가 더 일반적이다.
result: 'list[int]' = [0] * M

def solve(k: int) -> None:
    # 종료 조건: 길이 M인 수열이 완성됨
    if k == M:
        # result 리스트의 원소들을 공백으로 구분하여 출력
        print(*(result))
        return

    # 1부터 N까지의 숫자를 현재 자리(k)에 넣어본다
    for i in range(1, N + 1):
        result[k] = i  # 현재 자리에 숫자 i 저장
        solve(k + 1)   # 다음 자리(k+1)를 채우러 재귀 호출

# 0번째 인덱스부터 수열 채우기 시작
solve(0)