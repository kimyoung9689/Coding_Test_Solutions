import sys # 모듈 불러오기

# 주어질 정수의 개수 n값 입력 받기
n = int(sys.stdin.readline().rstrip())

# 정수들 공백으로 구분지어서 입력 받기
numbers = list(map(int,sys.stdin.readline().rstrip().split()))

# 찾으려고하는 정수 v값 입력 받기
v = int(sys.stdin.readline().rstrip())

# numbers 라는 리스트 안에 v값이 몇 개 있는지 센 후 count라는 변수에 저장
count = numbers.count(v)

# v가 몇 개인지 출력
print(count)


# 하나의 값을 입력 받을때는 int()로 묶어주지만
# 여러개의 값을 받기 위해 map()를 사용할 땐 map(int,)라는 형태로 들어간다.

# 참고로 map는 한 번 쓰고나면 다시 못 쓴다.
# 그렇기에 list()로 감싸주면 map객체 안의 값들을 메모리에 저장된 실제 리스트로 만듬
# 여러 번 사용 가능해지고 특정 리스트 메서드 사용도 가능해진다.
# len(),append(),sort(),count()
