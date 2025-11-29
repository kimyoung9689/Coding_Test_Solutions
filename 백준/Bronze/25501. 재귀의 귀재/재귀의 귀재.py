import sys
# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 호출 횟수를 위한 전역 변수
global_count: int

def recursion(s: str, l: int, r: int) -> int:
    """팰린드롬 재귀 판별 및 호출 횟수 기록."""
    global global_count
    global_count += 1  # 호출 횟수 증가

    if l >= r:
        return 1  # 팰린드롬 맞음
    elif s[l] != s[r]:
        return 0  # 팰린드롬 아님
    else:
        return recursion(s, l + 1, r - 1)  # 재귀 호출


def is_palindrome(s: str) -> int:
    """recursion 호출 전 횟수 초기화."""
    global global_count
    global_count = 0  # 횟수 초기화

    return recursion(s, 0, len(s) - 1)


def solve() -> None:
    """메인 로직 처리."""
    try:
        t: int = int(input())
    except:
        return

    for _ in range(t):
        s: str = input().strip()
        result: int = is_palindrome(s)
        
        print(f"{result} {global_count}")


if __name__ == "__main__":
    solve()