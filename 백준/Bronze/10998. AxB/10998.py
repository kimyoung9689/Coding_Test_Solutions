# 문제
# 두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 첫째 줄에 A×B를 출력한다.

# 예제 입력 1 
# 1 2
# 예제 출력 1 
# 2
# 예제 입력 2 
# 3 4
# 예제 출력 2 
# 12

1.
A,B = input().split()
print(int(A)*int(B))


2.
A,B = map(int,input().split())
print(A*B)


# input 로 사용자에게 답을 받고
# split 함수를 이용해 순서대로 나눈다.
# A와 B를 정수로 출력해주면 끝

#map함수를 이용해 한번에도 적용 가능








