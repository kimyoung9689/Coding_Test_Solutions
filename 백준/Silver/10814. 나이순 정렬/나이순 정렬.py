import sys
from typing import List, Tuple

# 입력을 빠르게 받기
def input() -> str:
    return sys.stdin.readline().rstrip()

# 회원의 수 N 입력
try:
    n: int = int(input())
except ValueError:
    sys.exit()

# 회원 정보를 저장할 리스트 생성 (나이, 이름, 가입순서)
members: List[Tuple[int, str, int]] = []

for i in range(n):
    # 나이와 이름 입력
    line: str = input()
    if not line:
        continue
        
    try:
        age_str, name = line.split()
        age: int = int(age_str)
    except ValueError:
        continue

    # (나이(int), 이름(str), 가입_순서(int)) 형태로 저장
    members.append((age, name, i))

# 나이(x[0])를 기준으로, 나이가 같으면 가입 순서(x[2])를 기준으로 오름차순 정렬
# 나이와 가입 순서 모두 오름차순으로 정렬됨 (작은 값 -> 큰 값)
sorted_members: List[Tuple[int, str, int]] = sorted(
    members, 
    key=lambda x: (x[0], x[2])
)

# 정렬된 결과 나이와 이름만 출력
for member in sorted_members:
    print(f'{member[0]} {member[1]}')