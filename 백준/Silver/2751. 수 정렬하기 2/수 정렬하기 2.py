import sys
from typing import List

def solve_sort_problem() -> None:
    """N개의 수 입력받아 오름차순으로 정렬 후 출력"""
    
    try:
        n: int = int(sys.stdin.readline())
    except:
        return
        
    numbers: List[int] = []
    
    for _ in range(n):
        try:
            numbers.append(int(sys.stdin.readline()))
        except:
            break
            
    # 리스트를 가장 빠른 방법으로 오름차순 정렬
    sorted_numbers: List[int] = sorted(numbers)
    
    # 정렬된 결과 하나씩 출력
    for num in sorted_numbers:
        print(num)

if __name__ == "__main__":
    solve_sort_problem()