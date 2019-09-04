t = int(input())
for tt in range(t):
    arr = [[0] * 10 for i in range(10)]
    n = int(input())
    for nn in range(n):
        test = list(map(int, input().split()))

        for i in range(test[1], test[3]+1):
            for j in range(test[0], test[2]+1):
                arr[i][j] += test[4]

        count = 0
        for i in range(10):
            for j in range(10):
                if arr[i][j] == 3:
                    count += 1
    print(f'#{tt+1} {count}')
