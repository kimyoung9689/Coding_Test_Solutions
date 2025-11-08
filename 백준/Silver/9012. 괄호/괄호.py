# 입력 데이터 수 T를 받는다.
T = int(input())

# T번 반복하며 각 테스트 케이스를 처리한다.
for _ in range(T):
    # 괄호 문자열을 입력받는다.
    ps = input()
    # 스택으로 사용할 빈 리스트를 만든다.
    stack = []
    # VPS 여부를 저장할 플래그. 일단 YES로 시작한다.
    is_vps = True

    # 문자열의 각 문자를 순서대로 확인한다.
    for char in ps:
        # 여는 괄호면 스택에 넣는다.
        if char == '(':
            stack.append(char)
        # 닫는 괄호면 짝이 있는지 확인한다.
        elif char == ')':
            # 스택이 비어있지 않으면 (짝 '('가 있으면)
            if stack:
                # 짝을 찾았으니 스택에서 뺀다.
                stack.pop()
            # 스택이 비어있으면 (짝이 없으면)
            else:
                # VPS 아님을 표시하고 반복을 멈춘다.
                is_vps = False
                break

    # 반복이 끝난 후, is_vps가 True일 때만 스택 상태를 최종 확인한다.
    if is_vps:
        # 스택에 남아있는 '('가 없으면 YES
        if not stack:
            print("YES")
        # 남아있는 '('가 있으면 NO
        else:
            print("NO")
    # 중간에 이미 VPS가 아니라고 판단된 경우 NO
    else:
        print("NO")