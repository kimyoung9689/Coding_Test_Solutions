import sys

def check_group_word(word):
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            new_word = word[i + 1:]
            if word[i] in new_word:
                return False
    return True

n = int(sys.stdin.readline())
count = 0

for _ in range(n):
    word = sys.stdin.readline().strip()
    if check_group_word(word):
        count += 1

print(count)