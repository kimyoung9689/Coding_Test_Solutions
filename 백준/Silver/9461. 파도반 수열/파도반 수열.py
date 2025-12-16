from typing import List

# 최대 N이 100이므로, 101까지 수열을 미리 계산
MAX_N = 101
# 수열 P(N)을 저장할 리스트 (인덱스 1부터 사용)
# 자료형 힌트: List[int] 대신 List[int]로 타입 힌트
# 문제의 N 범위가 100까지이고 P(100) 값도 int 범위를 넘지 않으므로 int 사용
padovan_sequence: List[int] = [0] * MAX_N

# 초기값 설정 (N=1, 2, 3)
padovan_sequence[1] = 1
padovan_sequence[2] = 1
padovan_sequence[3] = 1

# 점화식으로 P(4)부터 P(100)까지 계산
# N=4 일때: P(4) = P(2) + P(1) = 1 + 1 = 2
# P(N) = P(N-2) + P(N-3)
for i in range(4, MAX_N):
    padovan_sequence[i] = padovan_sequence[i - 2] + padovan_sequence[i - 3]

def solve() -> None:
    """
    테스트 케이스 T를 입력받아 각 N에 대한 P(N)을 출력한다.
    """
    try:
        # PEP 8: 변수 이름은 소문자 스네이크 케이스
        num_test_cases_str: str = input()
        num_test_cases: int = int(num_test_cases_str)
    except EOFError:
        # 입력이 없으면 종료
        return

    # 각 테스트 케이스 처리
    for _ in range(num_test_cases):
        try:
            n_str: str = input()
            n: int = int(n_str)
        except EOFError:
            break
        except ValueError:
            # 숫자가 아닌 입력이 들어왔을 경우
            continue
        
        # P(N) 출력 (미리 계산된 값 사용)
        print(padovan_sequence[n])

if __name__ == "__main__":
    solve()