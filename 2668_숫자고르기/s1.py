n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
num = list(enumerate(num, start=1))

cnt = 0
for i in range(1, n + 1):
    now = num[i - 1][1]
    for j in range(n):
        if j + 1 != i:
            if num[j][0] == i and num[j][1] == now:
                cnt += 1
            if num[j][0] == now and num[j][1] == i:
                cnt += 1
print(cnt)
                
        