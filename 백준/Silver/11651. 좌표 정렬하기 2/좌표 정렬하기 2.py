import sys

input = sys.stdin.readline

def solve():
    # 점의 개수 N을 입력받기
    n = int(input())
    
    # N개의 점들을 [x, y] 형태로 리스트에 저장
    points = []
    for _ in range(n):
        # 정수로 변환 후 리스트에 저장
        points.append(list(map(int, input().split())))
    
    # key=lambda p: (p[1], p[0])는 정렬의 기준으로 튜플 (y좌표, x좌표)를 사용한다는 뜻
    # p[1]은 y좌표, p[0]은 x좌표
    # 1. 첫 번째 요소인 y좌표(p[1])를 기준으로 오름차순 정렬
    # 2. y좌표가 같으면 두 번째 요소인 x좌표(p[0])를 기준으로 오름차순 정렬
    points.sort(key=lambda p: (p[1], p[0]))
    
    # 정렬된 결과 출력
    for x, y in points:
        print(f"{x} {y}")

if __name__ == "__main__":
    solve()