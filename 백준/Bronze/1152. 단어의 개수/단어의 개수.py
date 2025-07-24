# 문자열 입력 받기
text = input()

# 문자열 앞뒤 공백 제거
stripped_text = text.strip()

# 만약 strip()결과가 빈 문자열이라면
if not stripped_text:
    print(0)
else:
    words = stripped_text.split(' ')

    # 리스트 길이가 단어의 개수로 출력
    print(len(words))

