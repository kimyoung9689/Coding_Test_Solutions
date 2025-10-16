import sys
# 입력 최적화
N, M = map(int, sys.stdin.readline().split())

# 번호 <-> 이름 매핑 딕셔너리
num_to_name = {}
name_to_num = {}

# 도감 데이터 로드
for i in range(1, N + 1):
    name = sys.stdin.readline().strip()
    num_to_name[i] = name
    name_to_num[name] = i

# 문제 해결
for _ in range(M):
    problem = sys.stdin.readline().strip()
    
    # 입력이 숫자면 이름 출력, 문자면 번호 출력
    if problem.isdigit():
        print(num_to_name[int(problem)])
    else:
        print(name_to_num[problem])