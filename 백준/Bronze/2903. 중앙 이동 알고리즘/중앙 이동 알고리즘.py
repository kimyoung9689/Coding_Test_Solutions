N = int(input())

# N번의 과정을 거 후 한 변의 점의 개수
points_per_side = 2**N + 1

# 총 점의 개수
total_points = points_per_side * points_per_side

print(total_points)
