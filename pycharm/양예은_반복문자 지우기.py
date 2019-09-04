def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return paper(n-1) + 2*paper(n-2)


t = int(input())
for tc in range(t):
    n = int(input())

    print(f'#{tc+1} {paper(n)}')