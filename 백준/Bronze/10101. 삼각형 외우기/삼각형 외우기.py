# 세 각을 입력받기
angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

# 세 각의 합을 계산
total_angle = angle1 + angle2 + angle3

# 삼각형의 종류를 판별하여 출력
if total_angle != 180:
    print("Error")
elif angle1 == 60 and angle2 == 60 and angle3 == 60:
    print("Equilateral")
elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
    print("Isosceles")
else:
    print("Scalene")