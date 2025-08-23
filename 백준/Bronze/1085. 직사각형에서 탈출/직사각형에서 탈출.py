x, y, w, h = map(int,input().split())

# 네 변까지의 거리 계산
dist_left = x
dist_right = w - x
dist_bottom = y
dist_top = h - y

# 최솟값 찾기
min_distance = min(dist_left, dist_right, dist_bottom, dist_top)

print(min_distance)