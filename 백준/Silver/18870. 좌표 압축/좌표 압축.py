import sys

# 입력값 빠르게 받기
input = sys.stdin.read
data = input().split()

# N과 좌표 리스트 추출
n = int(data[0])
# 1부터 N까지가 좌표 X1, X2, ..., XN
coords = [int(x) for x in data[1:n+1]]

# 중복 제거 및 오름차순 정렬
# set을 이용해 중복을 제거하고, sorted로 정렬
unique_sorted_coords = sorted(list(set(coords)))

# 좌표 압축 결과를 저장할 딕셔너리 생성
coord_map = {val: i for i, val in enumerate(unique_sorted_coords)}

# 원본 좌표 리스트를 순회하며 압축된 좌표 값으로 변환
compressed_results = [str(coord_map[coord]) for coord in coords]

# 결과를 공백으로 구분하여 출력
print(" ".join(compressed_results))