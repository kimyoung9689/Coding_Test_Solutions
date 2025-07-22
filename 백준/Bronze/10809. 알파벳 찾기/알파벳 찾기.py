# s값 입력 받기
s = input()

# 결과 저장할 리스트 a부터z까지 26개 알파벳 -1로 채움
result = [-1] * 26

# a부터 z까지 하나씩 돌면서 찾아보기
for i in range(26):
    text = chr(ord('a') + i)
    index = s.find(text)
     
    # 찾은 위치 result에 저장
    result[i] = index

# 결과 리스트 숫자 공백 구분해서 출력
# map(str, result) 숫자들을 문자열로 바꿔줌
# ' '.join(...) 이 문자열들을 공백으로 연결
print(' '.join(map(str, result)))