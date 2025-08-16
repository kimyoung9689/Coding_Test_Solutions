while True:
    a, b = map(int, input().split()) # 두 숫자를 입력받음
    
    if a == 0 and b == 0: # 0 0 이 입력되면 반복문 종료
        break
    
    if b % a == 0: # 두 번째 숫자가 첫 번째 숫자의 배수면 (첫 번째 숫자가 약수)
        print("factor")
    elif a % b == 0: # 첫 번째 숫자가 두 번째 숫자의 배수면
        print("multiple")
    else: # 둘 다 아니면
        print("neither")