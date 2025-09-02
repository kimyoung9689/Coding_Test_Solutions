import sys

def men_of_passion(n: int) -> None:
    """
    MenOfPassion 알고리즘의 수행 횟수와 최고차항 차수를 출력하는 함수

    Args:
        n: 입력의 크기
    """
    # 코드 1의 수행 횟수: for문은 1부터 n까지 n번 반복
    count = n

    # 최고차항의 차수: 수행 횟수 n은 다항식 n^1과 같으므로 차수는 1
    degree = 1

    print(count)
    print(degree)


if __name__ == "__main__":
    try:
        n_input = int(sys.stdin.readline().strip())
        men_of_passion(n_input)
    except ValueError:
        print("입력값이 올바른 정수가 아님")