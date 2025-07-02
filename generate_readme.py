import os
import re
# import requests # requests 모듈은 이제 필요 없으니 삭제하거나 주석 처리

ROOT_DIR = os.getcwd()
BASE_BAEKJOON_DIR = os.path.join(ROOT_DIR, '백준', 'Bronze')

problem_titles = {
    '1000': 'A+B', '1001': 'A-B', '1002': '터렛', '1003': '피보나치 함수',
    '1008': 'A/B', '10171': '고양이', '10172': '개', '10430': '나머지',
    '10869': '사칙연산', '10926': '??!', '10998': 'AxB', '11382': '꼬마 정민',
    '1330': '두 수 비교하기', '14681': '사분면 고르기', '18108': '1998년생인 내가 태국에서는 2541년생?!',
    '2480': '주사위 세개', '2525': '오븐 시계', '2557': 'Hello World!',
    '2588': '나머지', '2739': '구구단', '2753': '윤년', '2884': '알람 시계',
    '9498': '시험 성적', '10950': 'A+B - 3', '8393': '합', '25304': '영수증',
    '25314': '코딩은 체육과목입니다',
}

# 웹 스크래핑 함수 (get_baekjoon_problem_info)는 이제 필요 없으니 삭제하거나 주석 처리
# def get_baekjoon_problem_info(problem_num):
#     # ... (이전 코드 내용) ...
#     return None # 항상 None을 반환하도록 변경하거나 함수 자체를 삭제

def create_readme_file(folder_path, problem_num, problem_title): # problem_info 인자 삭제
    readme_path = os.path.join(folder_path, 'README.md')
    if os.path.exists(readme_path):
        return

    content = f"# 백준 {problem_num}번: {problem_title}\n\n"
    # 문제 설명 대신, 링크만 바로 넣음
    content += f"--- \n"
    content += f"**[백준 문제 링크](https://www.acmicpc.net/problem/{problem_num})**\n"

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

for folder_name in os.listdir(BASE_BAEKJOON_DIR):
    folder_path = os.path.join(BASE_BAEKJOON_DIR, folder_name)
    if os.path.isdir(folder_path):
        match = re.match(r'(\d+)\.', folder_name)
        if match:
            problem_num = match.group(1)
            problem_title = problem_titles.get(problem_num, '알 수 없는 문제 제목')
            # problem_info = get_baekjoon_problem_info(problem_num) # 문제 정보 가져오는 부분 삭제
            create_readme_file(folder_path, problem_num, problem_title) # problem_info 인자 삭제