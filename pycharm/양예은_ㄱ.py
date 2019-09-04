T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    fly = [list(map(int, input().split())) for i in range(N)]
    maxV = 0
    for i in range(0, N - K + 1):  # 부분 영역의 왼쪽 위모서리칸 좌표, i, j
        for j in range(N - K + 1):
            s = 0
            for m in range(K):
                for n in range(K):
                    if m % 2 == 0 and n % 2 == 1:
                        s += fly[i + m][j + n]
                    elif m % 2 == 1 and n % 2 == 0:
                        s += fly[i + m][j + n]
            if maxV < s:
                maxV = s
    print(f'#{tc} {maxV}')