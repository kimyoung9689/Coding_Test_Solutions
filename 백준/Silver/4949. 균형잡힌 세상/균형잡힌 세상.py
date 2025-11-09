import sys

# 입력 속도가 빨라지도록 설정
input = sys.stdin.read

def solve() -> None:
    """
    입력된 문자열들의 괄호 균형 여부를 판단하여 출력
    """
    # 모든 입력을 한 번에 읽고 줄 단위로 분리
    data = input().splitlines()

    # 결과 리스트
    results = []

    # 각 줄을 순회
    for line in data:
        # 종료 조건: 온점 하나만 있는 경우
        if line == ".":
            break

        # 괄호만 담을 스택
        stack: list[str] = []
        is_balanced: bool = True

        # 문자열의 각 문자를 순회
        for char in line:
            # 왼쪽 괄호는 스택에 추가
            if char == "(" or char == "[":
                stack.append(char)
            # 오른쪽 괄호 처리
            elif char == ")" or char == "]":
                # 스택이 비어있으면 짝이 없는 경우이므로 불균형
                if not stack:
                    is_balanced = False
                    break
                
                # 짝이 맞는지 확인
                top = stack.pop()
                if (char == ")" and top != "(") or (char == "]" and top != "["):
                    is_balanced = False
                    break

        # 순회를 마친 후 스택에 괄호가 남아있으면 짝이 안 맞는 불균형
        if is_balanced and not stack:
            results.append("yes")
        else:
            results.append("no")

    # 결과 출력
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()