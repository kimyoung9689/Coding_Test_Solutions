import sys

def solve():
    # 입력을 빠르게 받기 위해 sys.stdin.readline 사용
    # N을 입력 받음
    try:
        # 첫 줄의 N을 입력 받음
        N = int(sys.stdin.readline())
    except:
        return

    # 총 곰곰티콘 사용 횟수
    gomgom_count = 0
    # ENTER 후 채팅 친 닉네임을 담을 집합 (중복 방지)
    current_chatters = set()

    # N개의 기록을 차례로 처리
    for _ in range(N):
        # 한 줄의 기록을 읽음
        record = sys.stdin.readline().strip()

        # 만약 "ENTER"가 나오면
        if record == "ENTER":
            # 1. 이전까지 모인 채팅 친 사람 수(Set 크기)를 더함
            gomgom_count += len(current_chatters)
            # 2. 새로운 입장이므로 Set을 비움 (초기화)
            current_chatters = set()
        # "ENTER"가 아닌 닉네임이 나오면
        else:
            # 닉네임을 Set에 추가
            current_chatters.add(record)

    # **가장 마지막 ENTER 이후** 채팅 친 사람들의 Set 크기를 최종적으로 더하기
    gomgom_count += len(current_chatters)

    # 최종 곰곰티콘 횟수를 출력
    print(gomgom_count)

if __name__ == "__main__":
    solve()