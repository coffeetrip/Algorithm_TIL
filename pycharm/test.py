def array90(array):
    new_90 = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_90[i][j] = array[-j-1][i]
    return new_90



for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(arr)

    arr_90 = array90(arr)
    arr_180 = array90(arr_90)
    arr_270 = array90(arr_180)
    print(arr_90)
    print(arr_180)
    print(arr_270)

