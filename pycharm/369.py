t = int(input())
for tc in range(t):
    n = int(input())
    num = list(map(int, input().split()))

    right_max = 0
    final = 0
    for i in range(n-1):
        right_sum = []
        for j in range(i+1, n):
            right_sum.append(num[j])
        if num[i] < max(right_sum):
            final += max(right_sum) - num[i]

    print(f'#{tc+1} {final}')
