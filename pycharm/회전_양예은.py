for tc in range(int(input())):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))

    while m > 0:
        num.append(num.pop(0))
        m -= 1
    print(f'#{tc+1} {num[0]}')