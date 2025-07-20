A, B, C = map(int, input().split())

result_1 = (A+B)%C
result_2 = ((A%C) + (B%C))%C
result_3 = (A*B)%C
result_4 = ((A%C) * (B%C))%C

print(result_1)
print(result_2)
print(result_3)
print(result_4)
