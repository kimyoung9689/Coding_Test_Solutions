import sys
from typing import List

# N 입력받기
try:
    n: int = int(sys.stdin.readline())
except:
    n = 0

# N개 단어 입력받고 중복 제거
words: List[str] = list(set([sys.stdin.readline().strip() for _ in range(n)]))

# 길이가 짧은 것부터 같으면 사전 순으로 정렬
sorted_words: List[str] = sorted(words, key=lambda word: (len(word), word))

# 결과 출력
for word in sorted_words:
    print(word)