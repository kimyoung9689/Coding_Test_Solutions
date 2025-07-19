# 가장 큰 숫자 저장할 변수 0값으로 등록
max_value = 0
# 가장 큰 숫자 몇 번째에 있었는지 저장 0값 등록
max_index = 0

# 숫자 9개니까 9번 반복
for i in range(9):
    num = int(input())

    # 만약 지금 들어온 숫자가 max_value 보다 크면
    if num > max_value:
        max_value = num   # 이 숫자가 max_value가 됨
        max_index = i + 1 # 이 숫자는 (i + 1)번째에 있다.

# 제일 큰 숫자 출력   
print(max_value)
# 제일 큰 숫자 몇 번째인지 출력
print(max_index)