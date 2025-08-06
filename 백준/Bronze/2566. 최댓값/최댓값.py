import sys

max_value = -1 # 입력값은 0 이상이므로 -1로 초기화해도 문제없음
row = 0
col = 0

for i in range(9):
    line = list(map(int, sys.stdin.readline().split()))
    
    for j in range(9):
        # 현재 값이 최댓값보다 크면
        if line[j] > max_value:
            max_value = line[j]
            row = i + 1
            col = j + 1

print(max_value)
print(row, col)