import sys

def solve() -> None:
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])  # 수의 개수
    m: int = int(input_data[1])  # 합을 구해야 하는 횟수
    
    # 원본 숫자 리스트 (1-based indexing을 위해 앞에 0 추가)
    numbers: list[int] = [0] + list(map(int, input_data[2:n+2]))
    
    # 누적 합 배열 생성 (PEP 484 타입 힌트 준수)
    prefix_sum: list[int] = [0] * (n + 1)
    for k in range(1, n + 1):
        prefix_sum[k] = prefix_sum[k-1] + numbers[k]
    
    # 질문 처리
    current: int = n + 2
    results: list[str] = []
    for _ in range(m):
        i: int = int(input_data[current])
        j: int = int(input_data[current + 1])
        # 구간 합 공식 적용
        results.append(str(prefix_sum[j] - prefix_sum[i-1]))
        current += 2
        
    # 결과 출력
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()