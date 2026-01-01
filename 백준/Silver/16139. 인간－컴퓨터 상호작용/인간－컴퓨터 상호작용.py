import sys

def solve() -> None:
    # 입력 속도 최적화
    input_data: list[str] = sys.stdin.read().split()
    if not input_data:
        return

    s: str = input_data[0]
    q: int = int(input_data[1])
    
    # alphabet_counts[알파벳 index][문자열 위치 + 1]
    # 26개 알파벳에 대한 누적 합 테이블 초기화
    n: int = len(s)
    prefix_sums: list[list[int]] = [[0] * (n + 1) for _ in range(26)]

    # 누적 합 테이블 채우기
    for i in range(n):
        char_idx: int = ord(s[i]) - ord('a')
        for j in range(26):
            prefix_sums[j][i + 1] = prefix_sums[j][i]
        prefix_sums[char_idx][i + 1] += 1

    # 질문 처리
    results: list[str] = []
    current: int = 2
    for _ in range(q):
        char: str = input_data[current]
        l: int = int(input_data[current + 1])
        r: int = int(input_data[current + 2])
        current += 3

        char_idx = ord(char) - ord('a')
        # l번째부터 r번째까지의 개수 계산
        count: int = prefix_sums[char_idx][r + 1] - prefix_sums[char_idx][l]
        results.append(str(count))

    # 결과 한 번에 출력
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()