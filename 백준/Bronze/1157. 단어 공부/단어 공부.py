from collections import Counter

# 값 입력 받기
word = input()

# 모든 문자를 대문자로 바꿔서 Counter로 개수 세기
counter_result = Counter(word.upper())

# 가장 많이 나온 알파벳 2개 리스트 형태로 가져오기
most_common_items = counter_result.most_common(2)

# 가장 많이 나온 알파벳이 1개 or 여러 개 라면
if len(most_common_items) == 1 or most_common_items[0][1] > most_common_items[1][1]:
    # 첫 번째로 가장 많이 나온 알파벳 출력
    print(most_common_items[0][0])
else:
    # 가장 많이 나온 알파벳이 여러 개 라면 ? 출력
    print('?')