import sys

def solve() -> None:
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n: int = int(input_data[0])
    k: int = int(input_data[1])
    p: int = 1_000_000_007

    # k가 n보다 크거나 음수면 조합은 0
    if k < 0 or k > n:
        print(0)
        return

    # 팩토리얼 값 미리 계산 (나머지 연산 포함)
    fact: list[int] = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % p

    # 이항 계수 공식: n! / (k!(n-k)!)
    # 분자: n!
    numerator: int = fact[n]
    # 분모: k!(n-k)!
    denominator: int = (fact[k] * fact[n - k]) % p

    # 페르마의 소정리: a^(p-2) % p 가 a의 역원임을 이용
    # 분모의 (p-2)승을 구함
    def power(a: int, b: int) -> int:
        res: int = 1
        a %= p
        while b > 0:
            if b % 2 == 1:
                res = (res * a) % p
            a = (a * a) % p
            b //= 2
        return res

    # 결과 출력: (분자 * 분모의 역원) % p
    print((numerator * power(denominator, p - 2)) % p)

if __name__ == "__main__":
    solve()