

# 나머지

# 문제
# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)

# 출력
# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 
# 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

# 예제 입력 1 
# 5 8 4
# 예제 출력 1 
# 1
# 1
# 0
# 0

A, B, C = map(int, input().split())

result_1 = (A+B)%C
result_2 = ((A%C) + (B%C))%C
result_3 = (A*B)%C
result_4 = ((A%C) * (B%C))%C

print(result_1)
print(result_2)
print(result_3)
print(result_4)

# A B C에게 각각 입력 받을 수 있는 값을 설정
# 첫째줄에서 넷째줄 까지 변수1부터 4까지 저장
# 변수로 출력하면 끝! 5 8 4 라는 값을 입력하면 1 1 0 0 출력된다.