import sys
from typing import Set

def solve():
    # 기록 수 N 입력
    try:
        n_str = sys.stdin.readline().strip()
        if not n_str:
            return
        n: int = int(n_str)
    except (EOFError, ValueError):
        return

    # 춤추는 사람 집합. 총총이로 시작
    dancing_people: Set[str] = {"ChongChong"}

    # N번의 만남 기록 처리
    for _ in range(n):
        line: str = sys.stdin.readline().strip()
        if not line:
            continue
        try:
            person_a, person_b = line.split()
        except ValueError:
            continue

        # 한 명이라도 춤추면 둘 다 추가
        if person_a in dancing_people or person_b in dancing_people:
            dancing_people.add(person_a)
            dancing_people.add(person_b)

    # 최종 인원 수 출력
    print(len(dancing_people))

if __name__ == "__main__":
    solve()