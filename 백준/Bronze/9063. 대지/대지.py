import sys

# 점의 개수 입력 받기
N = int(sys.stdin.readline())


# 점이 1개일 경우 넓이는 0이므로 예외처리
if N == 1:
    print(0)
# 점이 2개 이상일 경우 넓이 계산
else:
    # 첫 번째 점의 좌표를 입력받아 초기 최소/최대값 설정
    x, y = map(int, sys.stdin.readline().split())
    min_x = x
    max_x = x
    min_y = y
    max_y = y

    # N-1개의 점을 반복하며 최소값 최대값 갱신
    for _ in range(N - 1):
        x, y = map(int, sys.stdin.readline().split())
        
        # x좌표의 최소/최대값 갱신
        if x < min_x:
            min_x = x
        elif x > max_x:
            max_x = x
            
        # y좌표의 최소/최대값 갱신
        if y < min_y:
            min_y = y
        elif y > max_y:
            max_y = y

    # 최소/최대 좌표를 이용해 직사각형의 넓이 계산 후 출력
    width = max_x - min_x
    height = max_y - min_y
    area = width * height
    print(area)