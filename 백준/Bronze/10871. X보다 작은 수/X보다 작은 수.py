import sys

# n과 x값 입력 받기
n, x = map(int, sys.stdin.readline().split())

# a값 입력 받기
a = map(int, sys.stdin.readline().split())

# x보다 작은 숫자 넣을 빈 리스트 생성
result = []

# 수열 a에 있는 숫자 하나씩 확인
for num in a:
    # 만약 현재 숫자가 x보다 작다면
    if num < x:
        # 그 숫자를 result 리스트에 추가
        result.append(num)

# result 리스트에 모든 숫자 공백으로 구분해서 출력
# join 함수는 리스트의 요소들을 특정 구분자(여기서는 ' ')로 연결해서 문자열로 만들어줘.
print(' '.join(map(str, result)))


#join 함수는 한 번에 큰 문자열을 효율적으로 만든다.