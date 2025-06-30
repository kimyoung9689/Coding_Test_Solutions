
# 주사위 세개



# 문제
# 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 
# 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
# 예를 들어, 3개의 눈 3, 3, 6이 주어지면 
# 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 
# 또 3개의 눈이 2, 2, 2로 주어지면 
# 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다. 
# 3개의 눈이 6, 2, 5로 주어지면 
# 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.

# 3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.

# 입력
# 첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.

# 출력
# 첫째 줄에 게임의 상금을 출력 한다.

# 예제 입력 1 
# 3 3 6
# 예제 출력 1 
# 1300
# 예제 입력 2 
# 2 2 2
# 예제 출력 2 
# 12000
# 예제 입력 3 
# 6 2 5
# 예제 출력 3 
# 600



a, b, c = map(int,input().split())

prize_money = 0

if a == b == c:
    prize_money = 10000 + a * 1000
elif a == b:
    prize_money = 1000 + a * 100
elif a == c:
    prize_money = 1000 + a * 100
elif b == c:
    prize_money = 1000 + b * 100
elif a != b != c:
    if a >= b and a >= c:
     prize_money = a * 100
    elif b >= a and b >= c:
        prize_money = b * 100
    else:
        prize_money = c * 100
else:
    pass

print(prize_money)

# if문을 이용해서 각 규칙을 명확하게 구분지어 코드를 짜려고 노력했다.

# 풀이 후기

# 문제점 1 elif a != b != c 의 조건
# elif a != b != c 이 코드는 a와 c가 같을 수도 있다.(눈 2개 참 일 수 있다는 뜻)
# 그런데 elif a == b, elif a == c, elif b == c 에서 
# 두 개가 같은 경우를 다 처리했기 때문에 
# elif a != b != c에 도달 하는건 자동으로 모두 다른 눈이라는 뜻이다. 

# 결론 : elif a != b != c: 대신 else: 를 쓰는게 훨씬 간결하고 정확하다.
#      (이미 앞에서 다른 모든 경우를 걸러냈기 때문에)

# 문제점 2 가장 큰 눈 찾기
# f a >= b and a >= c: 이런 식으로 비교해서 가장 큰 수를 찾는 방식도 맞지만, 
# 파이썬에는 max()라는 편리한 함수가 있다.
# max(a, b, c) 이렇게 쓰면 가장 큰 값 한 번에 찾아주는데.. 난 바보다

# 문제점 3 중복 코드
# 두 개가 같은 경우(elif a == b, elif a == c, elif b == c)를 보면 
# 1000 + (같은 눈) * 100 이라는 계산식이 반복되는데
# 이때 collections.Counter를 쓰면 더 깔끔하게 처리 가능하다.


# 이건 문제점을 확인하고 수정한 코드 (기존 방식 강화형)

a, b, c = map(int, input().split())

prize_money = 0

if a == b and b == c:
    prize_money = 10000 + a * 1000
elif a == b: 
    prize_money = 1000 + a * 100
elif a == c: 
    prize_money = 1000 + a * 100
elif b == c: 
    prize_money = 1000 + b * 100
else:
    # 파이썬의 max() 함수로 가장 큰 값을 한 번에 찾기
    max_eye = max(a, b, c)
    prize_money = max_eye * 100

print(prize_money)



# counter를 사용한 코드

a, b, c = map(int, input().split())

prize_money = 0

# 리스트에 담아두면 처리가 더 편함
dice_rolls = [a, b, c]

# 각 눈이 몇 번 나왔는지 세기
# counter = 각 항목이 몇 번 나왔는지 세어주는 도구
from collections import Counter
counts = Counter(dice_rolls)

# counts.values()는 각 눈이 나온 횟수를 보여줌

# 같은 눈이 3개 나올 때
if 3 in counts.values(): # 어떤 눈이 3번 나왔는지 확인
    # count.keys()에서 3번 나온 눈 찾아서 값 가져오기
    # 이때 3번 나온 눈은 무조건 하나
    for num in counts.keys():
        if counts[num] == 3:
            same_eye = num # 3번 나온 눈의 값
            break
    prize_money = 10000 + same_eye * 1000

# 같은 눈이 2개 일 때
elif 2 in counts.values():
     for num in counts.keys():
        if counts[num] == 2:
            same_eye = num # 2번 나온 그 눈의 값
            break
     prize_money = 1000 + same_eye * 100


# 모두 다른 눈 일 때
else:
 
    # max() 함수를 써서 가장 큰 눈을 한 번에 찾기
 max_eye = max(a, b, c)
 prize_money = max_eye * 100

print(prize_money)



# 아직 초보라 그런지 counter를 사용한 코드가 더 길고 복잡해 보이지만
# 주사위가 3개가 아니라 5개 10개가 된다면 기존 코드는 거의 못 쓴다고 봐야한다.
# 주사위 눈이 1~6이 아니라 1~100처럼 범위가 넓어져도 잘 작동하고
# 어떤 숫자가 몇 번 나왔는지 빈도를 계산하는 문제였다면 
# counter가 if문 보다 훨씬 직관적이고 깔끔해질 거 같다.



