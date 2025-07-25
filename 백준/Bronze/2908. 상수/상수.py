# 두 수 입력 받기
a, b = input().split()

# 숫자 뒤집기
reversed_a = int(a[::-1])
reversed_b = int(b[::-1])

# 뒤집은 두 수 비교해 더 큰 수 출력
if reversed_a > reversed_b:
    print(reversed_a)
else:
    print(reversed_b)

# 숫자 뒤집기 할 때 문자열만 뒤집기가 가능