import sys

# N(숫자 카드의 개수)을 읽고 버림
sys.stdin.readline()

# N개의 숫자 카드를 읽어 set에 저장 (탐색 속도 O(1) 확보)
card_set = set(map(int, sys.stdin.readline().split()))

# M(확인해야 할 정수의 개수)을 읽고 버림
sys.stdin.readline()

# 확인해야 할 M개의 정수를 읽어 리스트에 저장
check_list = list(map(int, sys.stdin.readline().split()))

# 결과를 저장할 리스트
result = []

# M개의 정수를 순회하며 set에서 빠르게 존재 여부 확인
for number in check_list:
    # O(1) 탐색
    if number in card_set:
        result.append(1)
    else:
        result.append(0)

# 리스트의 모든 요소를 공백으로 구분하여 출력
print(*(result))