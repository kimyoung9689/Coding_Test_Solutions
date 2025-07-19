# 모든 학생 만들기
all_students_set = set(range(1, 31))



# 제출한 학생 표시
# 제출한 학생들 번호 저장할 빈 집합
submitted_students_set = set()

# 제출한게 28개니 28번 반복해 출석번호 입력
for _ in range(28):
    student_num = int(input())              # 키보드로 입력받은 숫자를 정수로 바꿈
    submitted_students_set.add(student_num) # 제출한 학생 집합에 번호 넣기

# 전체 학생 집합 - 제출한 학생 집합
not_submitted_students = all_students_set - submitted_students_set

# 작은 수 부터 출력
# 집합을 리스트로 교체
not_submitted_list = list(not_submitted_students)

# 리스트를 작은 수부터 큰 수대로 정렬
not_submitted_list.sort()

# 첫 번째 숫자 두 번째 숫자 출력
print(not_submitted_list[0])
print(not_submitted_list[1])

# 집합을 이용해 더 빠르고 간결하게 출력
# 작은 수 부터 순서대로 하는게 아니면 리스트로 바꿔 줄 필요도 없다.