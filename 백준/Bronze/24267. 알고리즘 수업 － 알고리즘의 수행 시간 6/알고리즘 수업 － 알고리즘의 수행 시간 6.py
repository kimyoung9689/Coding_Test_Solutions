import sys

def solve():
    """
    주어진 n에 대해 MenOfPassion 알고리즘의 수행 횟수와
    최고차항의 차수를 계산하는 함수
    """
    try:
        n_str = sys.stdin.readline().strip()
        if not n_str:
            return

        n = int(n_str)
        
        # 조합 공식 nC3을 사용하여 수행 횟수 계산
        # 1. n * (n - 1) * (n - 2)를 먼저 계산
        # 2. 결과값을 6으로 나누어 수행 횟수를 구함
        count = (n * (n - 1) * (n - 2)) // 6
        
        # 3중 반복문이므로 최고차항의 차수는 3
        degree = 3
        
        print(count)
        print(degree)
    except (ValueError, IndexError) as e:
        # 입력이 유효하지 않을 경우를 대비한 예외 처리
        print(f"입력 오류: {e}", file=sys.stderr)

if __name__ == "__main__":
    solve()