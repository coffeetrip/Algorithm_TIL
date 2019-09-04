t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(n)]

    maxV = 0
    for i in range(n-k+1):
        for j in range(n-k+1):
            s = 0
            for m in range(k):
                for c in range(k):
                    if m == 0 or m == k-1 or c == 0:
                        s += fly[i+m][j+c]
            #print(s)
            if maxV < s:
                maxV = s
    print(f'#{tc} {maxV}')
