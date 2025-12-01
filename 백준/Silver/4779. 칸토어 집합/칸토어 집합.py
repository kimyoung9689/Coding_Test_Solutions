import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def get_cantor_set(n: int) -> str:
    """
    N이 주어졌을 때, 3^N 길이의 칸토어 집합 근사 문자열을 구하는 함수.
    
    Args:
        n: 3^n 길이의 문자열을 만들 N (0 <= n <= 12).
        
    Returns:
        칸토어 집합 근사 문자열.
    """
    
    # N=0일 때, 3^0 = 1, 문자열 길이는 1. '-' 하나.
    if n == 0:
        return "-"
    
    # N-1일 때의 칸토어 문자열을 재귀적으로 구함.
    # 이것이 전체 문자열의 왼쪽 1/3과 오른쪽 1/3이 됨.
    prev_set = get_cantor_set(n - 1)
    
    # 가운데 1/3을 채울 공백 문자열의 길이
    # N-1일 때의 길이가 3^(N-1)이므로, 공백도 이와 같은 길이.
    # 예: N=1 (길이 3) -> N=0 (길이 1) + 공백 1개 + N=0 (길이 1)
    # 예: N=2 (길이 9) -> N=1 (길이 3) + 공백 3개 + N=1 (길이 3)
    middle_space = " " * len(prev_set)
    
    # 왼쪽 1/3 + 가운데 1/3(공백) + 오른쪽 1/3
    # 두 개의 prev_set과 그 사이에 공백을 합친다.
    return prev_set + middle_space + prev_set

# 여러 줄의 입력을 처리
while True:
    try:
        # 한 줄에서 N을 읽음
        n = int(input())
    except:
        # 파일의 끝 (EOF) 도달 시 루프 종료
        break
    
    # 칸토어 집합 근사 문자열을 구해서 출력
    print(get_cantor_set(n))