import sys

# 한 줄씩 반복 처리
for line in sys.stdin:
    # 각 줄을 그대로 출력 (줄 끝 공백문자 제거)
    print(line.rstrip())