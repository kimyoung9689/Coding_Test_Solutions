import sys
from typing import List

def get_max_area(heights: List[int]) -> int:
    """
    스택을 사용하여 히스토그램에서 가장 큰 직사각형의 넓이를 계산함.
    """
    stack: List[int] = []
    max_area = 0
    # 모든 막대를 처리하기 위해 끝에 높이 0 추가
    heights.append(0)
    
    for i, h in enumerate(heights):
        # 스택이 비어있지 않고 현재 높이가 스택 top의 높이보다 낮으면 계산 시작
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            # 스택이 비어있으면 현재 i가 너비, 아니면 i - 1 - stack[-1]이 너비
            width = i if not stack else i - 1 - stack[-1]
            max_area = max(max_area, height * width)
        stack.append(i)
    
    # 원본 데이터 보존을 위해 추가했던 0 제거
    heights.pop()
    return max_area

def main() -> None:
    """
    입력을 처리하고 결과를 출력함.
    """
    for line in sys.stdin:
        data = list(map(int, line.split()))
        if data[0] == 0:
            break
        
        # 첫 번째 숫자는 n이므로 제외하고 전달
        print(get_max_area(data[1:]))

if __name__ == "__main__":
    main()