
# 시험 성적

# 문제
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 시험 성적을 출력한다.

# 예제 입력 1 
# 100
# 예제 출력 1 
# A


test_point = int(input())

if test_point >= 90 and test_point <= 100:
    print("A")
elif test_point >= 80 and test_point <= 89:
    print("B")
elif test_point >= 70 and test_point <= 79:
    print("C")
elif test_point >= 60 and test_point <= 69:
    print("D")
else:
    print("F")

# int 와 input을 사용해 사용자에게 숫자로 된 점수를 입력 받는다.
# if elif else문을 이용해 각각의 점수 구간 일 때 A B C D 를 출력
# 마지막 F는 별다른 설정 없이 그 외에 점수는 F이기에 출력만 하면 끝














