# 입력
s = input()

# 서로 다른 부분 문자열을 저장할 집합
substrings = set()

# 모든 부분 문자열 생성 및 집합에 추가
# 시작 인덱스 i
for i in range(len(s)):
    # 끝 인덱스 j
    for j in range(i, len(s)):
        # s[i:j+1]이 부분 문자열
        substrings.add(s[i:j+1])

# 서로 다른 부분 문자열의 개수 출력
print(len(substrings))