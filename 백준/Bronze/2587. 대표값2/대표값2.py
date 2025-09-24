import sys

def calculate_average_and_median() -> None:
    """
    다섯 개의 자연수를 입력받아 평균과 중앙값을 계산, 출력하는 함수
    """
    numbers = []
    total_sum = 0
    
    for _ in range(5):
        num = int(sys.stdin.readline())
        numbers.append(num)
        total_sum += num
        
    # 평균 계산
    average = total_sum // 5
    
    # 중앙값 계산
    numbers.sort()
    median = numbers[2]
    
    print(average)
    print(median)

if __name__ == "__main__":
    calculate_average_and_median()