import sys


def power(a: int, b: int, c: int) -> int:
    """
    분할 정복을 이용하여 (a^b) % c를 계산한다.
    
    Args:
        a: 밑
        b: 지수
        c: 나누는 수
        
    Returns:
        나머지 값
    """
    if b == 1:
        return a % c
    
    # b를 절반으로 나눠서 재귀 호출
    temp: int = power(a, b // 2, c)
    
    # b가 짝수인 경우
    if b % 2 == 0:
        return (temp * temp) % c
    # b가 홀수인 경우
    else:
        return (temp * temp * a) % c


def main() -> None:
    """
    메인 실행 함수
    """
    # 입력을 빠르게 받고 정수로 변환
    input_data: list[str] = sys.stdin.read().split()
    if not input_data:
        return
        
    a: int = int(input_data[0])
    b: int = int(input_data[1])
    c: int = int(input_data[2])
    
    # 결과 출력
    print(power(a, b, c))


if __name__ == "__main__":
    main()