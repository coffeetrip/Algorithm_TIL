t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(n)]

    maxV = 0
    for i in range(n-k+1):
        for j in range(n-k+1):
            s = 0
            for r in range(i, i+k):
                for c in range(j, j+k):
                    if r-i == c-j or r+c-i-j == k-1:
                        s += fly[r][c]
            if maxV < s:
                maxV = s
    print(f'#{tc} {maxV}')