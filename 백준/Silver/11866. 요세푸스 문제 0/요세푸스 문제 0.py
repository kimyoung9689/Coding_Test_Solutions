import sys
# sys.stdin.readline을 사용하여 N과 K를 입력받고 정수로 변환
# N은 사람 수, K는 제거할 순서
input_data = sys.stdin.readline().split()
N = int(input_data[0])  # 사람 수
K = int(input_data[1])  # 제거할 순서

# 1부터 N까지의 번호가 있는 리스트를 생성
people = list(range(1, N + 1))  # [1, 2, 3, ..., N]

# 제거된 사람들의 순서를 저장할 리스트를 생성
result = []  # 요세푸스 순열

# 다음에 제거할 사람의 인덱스(위치)를 저장하는 변수
# 리스트는 0부터 시작하므로 처음에는 0으로 초기화
# K번째를 찾을 때 K-1을 더해서 인덱스를 계산할 것
kill_index = 0

# people 리스트에 사람이 남아있지 않을 때까지 반복
# (모든 사람이 제거될 때까지)
while people:
    # 현재 남아있는 사람 수(리스트 길이)에 맞게
    # K-1만큼 다음 인덱스를 계산하고, 리스트의 끝을 넘어가면
    # 나머지 연산(%)으로 처음으로 돌아오게 한다.
    # 예: (현재 인덱스 0) + (3 - 1) = 2. kill_index = 2 % 7 = 2.
    # 예: (현재 인덱스 6) + (3 - 1) = 8. kill_index = 8 % 4 = 0.
    kill_index = (kill_index + K - 1) % len(people)

    # 계산된 kill_index 위치에 있는 사람을 리스트에서 제거(pop)하고
    # 그 값을 result 리스트에 추가
    # pop된 순간, 리스트 길이가 1 줄어들고 kill_index 다음 요소들이
    # 앞으로 당겨지므로, kill_index는 다음 시작 위치를 가리키게 된다.
    killed_person = people.pop(kill_index)
    result.append(killed_person)

# 결과를 예제 형식(<3, 6, 2, 7, 5, 1, 4>)에 맞게 문자열로 만든다.
# 리스트 요소들을 ", "로 연결하고 앞뒤에 "<"와 ">"를 붙임
output = f"<{', '.join(map(str, result))}>"

# 결과 출력
print(output)