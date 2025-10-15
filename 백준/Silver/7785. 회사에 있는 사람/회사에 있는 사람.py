import sys
# 입력 속도를 높이기 위해 sys.stdin.readline 사용
input = sys.stdin.read
data = input().split()

# 첫 번째 원소는 로그 기록 수 n이므로 건너뛰고, 나머지 데이터만 사용
# 로그는 [이름, 상태, 이름, 상태, ...] 순서로 저장됨
# data[1:]부터 시작하여 2개씩 묶어서 처리
log_data = data[1:]

# 현재 회사에 있는 사람들을 저장할 집합 (Set)
# Set을 사용하면 이름의 추가(enter)와 삭제(leave)가 O(1)의 시간 복잡도로 매우 빠름
current_people = set()

# 로그 데이터를 두 개씩 (이름, 상태) 묶어서 반복
# zip(log_data[::2], log_data[1::2])는 (data[1], data[2]), (data[3], data[4]), ... 형태로 묶어줌
for name, action in zip(log_data[::2], log_data[1::2]):
    # 'enter'면 집합에 이름 추가
    if action == "enter":
        current_people.add(name)
    # 'leave'면 집합에서 이름 제거
    # 이미 'enter'가 되어있으므로, remove()를 안전하게 사용할 수 있음
    elif action == "leave":
        current_people.remove(name)

# 현재 회사에 있는 사람들을 리스트로 변환
# 출력을 위해 정렬
result = list(current_people)

# sorted() 함수에 reverse=True 옵션 사용
result.sort(reverse=True)

# 결과 출력
for name in result:
    print(name)

