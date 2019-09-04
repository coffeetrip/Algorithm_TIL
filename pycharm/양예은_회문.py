test_number = int(input())
for tc in range(test_number):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]

    for i in range(N):
        arr_col = ''
        for j in range(N-M+1):
            arr_col = arr[i][j:j+M]
            if arr_col == arr_col[::-1]:
                print('#{} {}'.format(tc + 1, arr_col))

    for i in range(0, N):
        arr_col = ""
        for j in range(0, N):
            arr_col += arr[j][i]
        for k in range(0, N - M + 1):
            col = arr_col[k:k + M]
            if col == col[::-1]:
                print('#{} {}'.format(tc + 1, col))
