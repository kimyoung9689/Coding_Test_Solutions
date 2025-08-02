import sys

# 값 입력 받기
word = sys.stdin.readline().strip()

# 크로아티아 알파벳 리스트에 저장
croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 입력된 값 크로아티아 알파벳 조합 찾아 바꿔주기
for alpha in croatian_alphabets:
    word = word.replace(alpha, '_')

# 문자열의 길이를 출력
print(len(word))