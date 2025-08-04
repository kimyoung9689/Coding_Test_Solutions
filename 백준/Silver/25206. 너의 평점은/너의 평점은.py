# 딕셔너리 생성해 등급별 과목평점 저장
grade_dict = {
    'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0,
    'F': 0.0
}

# 변수 값 0으로 초기화
total_credits = 0
total_score = 0

# 20번 반복하며 과목명,학점,등급 입력 받기
for _ in range(20):
    subject, credit, grade = input().split()
    credit = float(credit)
     
    # 만약 등급이 P가 아니라면 해당 과목 학점 + (학점 * 과목평점)
    if grade != 'P':
        total_credits += credit
        total_score += credit * grade_dict[grade]

# 평점 계산하기 
if total_credits == 0:
    print(f'{0.0:.6f}')
    
# gpa 변수의 값을 소수점 6자리까지 출력
else:
    gpa = total_score / total_credits
    print(f'{gpa:.6f}')