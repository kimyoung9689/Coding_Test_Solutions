# N과 K를 입력받기
N, K = map(int, input().split())

# 약수의 개수 0으로 초기화
count = 0

# 1부터 N까지 반복하면서 약수를 찾기
for i in range(1, N + 1):
    if N % i == 0:
        # 약수를 찾으면 개수 1 증가
        count += 1
        # 만약 약수의 개수가 K번째가 되면
        if count == K:
            # 그 숫자를 출력
            print(i)
            break
else:
    # for문이 중간에 break 없이 끝까지 돌았으면
    # K번째 약수가 없다는 뜻
    print(0)