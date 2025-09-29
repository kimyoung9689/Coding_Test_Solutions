import sys
# 입력 속도 최적화
input = sys.stdin.readline
# 출력 속도 최적화
write = sys.stdout.write

def counting_sort_production_ready():
    # N을 입력받고 예외 처리
    try:
        N = int(input().strip())
    except:
        return
        
    # 수의 최대 범위 (10,000)를 이용한 계수 정렬
    MAX_VALUE = 10000
    # 메모리 절약을 위해 counts 배열만 생성
    counts = [0] * (MAX_VALUE + 1)

    # N번 반복하며 수의 개수를 카운트
    for _ in range(N):
        try:
            num = int(input().strip())
            # 입력 범위 내 수만 처리
            if 1 <= num <= MAX_VALUE:
                counts[num] += 1
        except:
            break
            
    # 정렬된 결과를 바로 출력
    for i in range(1, MAX_VALUE + 1):
        count = counts[i]
        
        # 해당 숫자가 존재하면
        if count > 0:
            # 출력 문자열을 미리 생성
            output_str = str(i) + '\n'
            
            # 문자열을 반복 생성하지 않고 write를 반복 호출하여 메모리 초과 방지
            for _ in range(count):
                write(output_str)

if __name__ == "__main__":
    counting_sort_production_ready()