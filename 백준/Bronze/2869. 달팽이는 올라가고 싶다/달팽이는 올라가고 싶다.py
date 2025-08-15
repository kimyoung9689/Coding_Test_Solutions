import math

# A = 낮에 올라갈 수 있는 미터 
# B = 밤에 잠자는 동안 미끄러진 미터
# V =  오르는 나무 막대의 높이
# 정상에 올라간 후에는 미끄러지지않음
A, B, V = (map(int, input().split()))

# 달팽이가 마지막 날 올라가는 A를 제외한 높이
target = V - A

# 하루에 순수하게 올라가는 높이
daily_climb = A - B

# 마지막 날 제외 올라가는데 걸리는 일수
days_before_last = math.ceil(target / daily_climb)

# 마지막 날 제외한 일수 + 마지막 날
total_days = days_before_last + 1

# V - A가 0보다 작거나 같으면 첫날에 도착하니 1 출력
if V <= A:
    print(1)
else:
    print(total_days)