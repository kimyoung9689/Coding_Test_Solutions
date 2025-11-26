import sys
from collections import defaultdict

# 입력 속도 개선
input = sys.stdin.read

def solve():
    # 파일 전체 내용을 읽어와서 공백 기준으로 분리
    data = input().split()
    
    # N (단어 개수)과 M (최소 길이 기준)을 추출
    N = int(data[0])
    M = int(data[1])
    # 단어 리스트는 data[2]부터 시작
    words = data[2:]
    
    # 1. 단어 빈도를 저장할 딕셔너리 초기화
    # defaultdict를 사용하면 키가 없을 때 0으로 자동 초기화됨
    word_count = defaultdict(int)
    
    # 2. M보다 짧은 단어 제외 및 빈도 계산
    for word in words:
        if len(word) >= M: # 길이가 M 이상인 단어만 처리
            word_count[word] += 1
            
    # 3. 단어장 정렬을 위한 리스트 준비
    # 딕셔너리의 키(단어)들을 리스트로 만듦
    # 단어장에 단어가 반드시 1개 이상 존재함이 보장됨
    word_list = list(word_count.keys())
    
    # 4. 세 가지 기준에 따라 정렬 (Lambda 함수 사용)
    # 정렬 기준: (1. 빈도 내림차순, 2. 길이 내림차순, 3. 알파벳 오름차순)
    # 파이썬의 sorted는 안정 정렬(Stable Sort)이라서 뒤의 기준부터 역순으로 적용됨
    # 하지만 key에 튜플을 사용하면 튜플 요소 순서대로 우선순위가 적용됨
    # -word_count[x]: 빈도 내림차순을 위해 음수 사용 (1순위)
    # -len(x): 길이 내림차순을 위해 음수 사용 (2순위)
    # x: 알파벳 오름차순 (3순위)
    word_list.sort(key=lambda x: (-word_count[x], -len(x), x))
    
    # 5. 결과를 한 줄에 하나씩 출력
    print('\n'.join(word_list))

# PEP 8 준수를 위해 main 함수 형태로 호출
if __name__ == "__main__":
    solve()