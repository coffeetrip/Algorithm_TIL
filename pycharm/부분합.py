t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    test = list(map(int, input().split()))

    test_sum=[]
    for j in range(0, n-m+1):
        t_sum = 0
        for k in range(j, j+m):
            t_sum += test[k]
        test_sum.append(t_sum)

    for k in range(len(test_sum)-1, 0, -1):
        for j in range(0, k):
            if test_sum[j] > test_sum[j+1]:
                test_sum[j],test_sum[j+1] = test_sum[j+1],test_sum[j]
    result = test_sum[-1] - test_sum[0]
    print('#{} {}' .format(tc, result))