import sys

def solve():
    """
    N개의 수를 오름차순으로 정렬하는 함수
    """
    try:
        n = int(sys.stdin.readline())
        numbers = []
        for _ in range(n):
            numbers.append(int(sys.stdin.readline()))
        
        numbers.sort()
        
        for number in numbers:
            print(number)
            
    except (ValueError, IndexError) as e:
        print(f"입력 형식이 올바르지 않음. 오류: {e}")

if __name__ == "__main__":
    solve()