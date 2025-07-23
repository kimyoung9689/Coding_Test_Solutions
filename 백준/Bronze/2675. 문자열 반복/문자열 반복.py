def solve():
    t = int(input()) # 테스트 케이스 수
    for _ in range(t):
        r, s = input().split() # 반복 횟수, 문자열
        r = int(r)
        p = ""
        for char in s:
            p += char * r # 문자 반복 후 추가
        print(p)

solve()