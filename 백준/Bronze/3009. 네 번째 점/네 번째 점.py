x_list = []
y_list = []

for _ in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

result_x = 0
result_y = 0

# x 좌표 찾기
for x in x_list:
    if x_list.count(x) == 1:
        result_x = x
        break

# y 좌표 찾기
for y in y_list:
    if y_list.count(y) == 1:
        result_y = y
        break

print(result_x, result_y)