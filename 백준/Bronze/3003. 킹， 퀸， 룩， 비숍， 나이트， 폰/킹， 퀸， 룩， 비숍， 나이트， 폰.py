# 필요한 체스 피스 개수
correct_pieces = [1, 1, 2, 2, 2, 8]

# 동혁이가 발견한 체스 피스 개수
donghyeok_pieces = list(map(int, input().split()))

# 결과 값 저장할 빈 리스트 생성
result = []

# 각 체스 피스의 개수 차이를 계산하여 결과 리스트에 추가
for i, count in enumerate(donghyeok_pieces):
    diff = correct_pieces[i] - count
    result.append(diff)

# 계산된 결과들 공백으로 구분해서 한 줄로 출력
print(' '.join(map(str, result)))