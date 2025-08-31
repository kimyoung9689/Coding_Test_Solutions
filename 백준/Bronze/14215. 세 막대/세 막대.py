a, b, c = map(int, input().split())

# 막대 길이를 오름차순으로 정렬
lengths = sorted([a, b, c])

# 가장 긴 변
longest = lengths[2]
# 나머지 두 변의 합
others_sum = lengths[0] + lengths[1]

# 삼각형 조건을 만족하는지 확인
if longest < others_sum:
    # 조건을 만족하면 둘레는 세 막대 길이의 합
    perimeter = longest + others_sum
else:
    # 조건을 만족하지 않으면 가장 긴 변의 길이를 줄여야 함
    # 줄인 후 가장 긴 변은 나머지 두 변의 합보다 1 작은 값
    perimeter = (others_sum - 1) + others_sum

print(perimeter)