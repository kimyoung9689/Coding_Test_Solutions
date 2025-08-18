while True:
    n = int(input())  # 숫자 n을 입력받기

    if n == -1:  # -1이 입력되면 끝
        break

    divisors = []  # 약수들 담을 빈 목록 생성
    total = 0  # 약수들의 합을 담을 변수 생성

    for i in range(1, n):  # 1부터 n-1까지 반복
        if n % i == 0:  # n을 i로 나눴을 때 나머지가 0이면
            divisors.append(i)  # i는 약수니까 목록에 추가
            total += i  # 그리고 합계에 더함

    if total == n:  # 약수들의 합이 n과 같으면
        print(f"{n} = {' + '.join(map(str, divisors))}")
    else:  # 다르면
        print(f"{n} is NOT perfect.")