from typing import List

def sort_inside(n: int) -> int:
    """자연수 n의 각 자릿수를 내림차순으로 정렬한 수 반환"""
    
    str_n: str = str(n)
    digit_list: List[str] = list(str_n)
    
    # 자릿수를 내림차순으로 정렬
    sorted_digits: List[str] = sorted(digit_list, reverse=True)
    
    # 정렬된 자릿수를 합쳐 정수로 변환
    result_str: str = "".join(sorted_digits)
    
    return int(result_str)

# 메인 로직
if __name__ == "__main__":
    n_input: str = input()
    
    # 입력값을 자릿수 리스트로 분리
    digits: List[str] = list(n_input)
    
    # 리스트를 내림차순으로 정렬
    digits.sort(reverse=True)
    
    # 정렬된 자릿수들을 다시 문자열로 합치기
    result: str = "".join(digits)
    
    print(result)