import sys
from typing import List, Tuple

def solve() -> None:
    """좌표를 x-y 순으로 정렬하여 출력한다."""
    read = sys.stdin.readline
    write = sys.stdout.write
    
    # N 입력
    try:
        n_line: str = read()
        if not n_line:
            return
        n: int = int(n_line.strip())
    except ValueError:
        return

    points: List[Tuple[int, int]] = []

    # N개의 점 (x, y) 입력 및 리스트 저장
    for _ in range(n):
        try:
            line: str = read()
            if not line:
                break
            
            x: int
            y: int
            # map을 사용해 간결하게 정수 변환
            x, y = map(int, line.split())
            
            points.append((x, y))
        except ValueError:
            continue
        except EOFError:
            break

    # 튜플의 기본 정렬(x 기준 정렬 후 y 기준 정렬) 사용
    sorted_points: List[Tuple[int, int]] = sorted(points)

    # 정렬 결과 출력
    for x_coord, y_coord in sorted_points:
        write(f"{x_coord} {y_coord}\n")

if __name__ == "__main__":
    solve()