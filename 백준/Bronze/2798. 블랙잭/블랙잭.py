import sys

def solve():
    """
    백준 2798번 블랙잭 문제 해결하는 함수
    """
    try:
        n, m = map(int, sys.stdin.readline().split())
        cards = list(map(int, sys.stdin.readline().split()))
    except ValueError:
        return # 입력 형식이 잘못된 경우 종료

    max_sum = 0
    # 세 장의 카드를 고르는 3중 반복문
    for i in range(n):
        for j in range(i + 1, n):
          for k in range(j + 1, n):
              current_sum = cards[i] + cards[j] + cards[k]

              # 세 카드의 합이 M 넘지 않는지 확인
              if current_sum <= m:
                  # M을 넘지 않고 가장 가까운 값으로 생성
                  if current_sum > max_sum:
                      max_sum = current_sum

    print(max_sum)

if __name__ == "__main__":
    solve()