a, b, c = map(int, input().split())

cnt = a // (c - b)
if b < c:
    while True:
        gen_num = a + (b * cnt)
        profit_num = c * cnt
        if gen_num < profit_num:
            break
        cnt += 1
        print(gen_num, profit_num)

    print(cnt)
else:
    print(-1)