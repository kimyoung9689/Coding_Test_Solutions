def solve():
    """
    삼각형의 세 변의 길이를 입력받아 종류를 판별하고 출력하는 함수
    """
    while True:
        # 입력값을 공백 기준으로 나누어 정수로 변환
        sides = list(map(int, input().split()))

        # 입력의 마지막 줄(0 0 0)이면 반복문 종료
        if sum(sides) == 0:
            break

        # 삼각형 변의 길이를 오름차순으로 정렬
        # 이렇게 하면 가장 긴 변이 마지막 요소에 위치하게 돼
        sides.sort()
        a, b, c = sides

        # 삼각형 성립 조건: 가장 긴 변(c)이 나머지 두 변(a, b)의 합보다 작아야 함
        if a + b <= c:
            print("Invalid")
        elif a == b and b == c: # 세 변의 길이가 모두 같은 경우
            print("Equilateral")
        elif a == b or b == c or a == c: # 두 변의 길이가 같은 경우
            print("Isosceles")
        else: # 세 변의 길이가 모두 다른 경우
            print("Scalene")

if __name__ == "__main__":
    solve()