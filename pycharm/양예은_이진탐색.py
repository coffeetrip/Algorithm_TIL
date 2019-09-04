def search(w):
    l = 1
    r = p
    c = (l+r)//2
    count = 1
    while c != w:
        c = (l + r) // 2
        count += 1
        if c > w:
            r = c
        else:
            l = c
    return count


test_number = int(input())
for tc in range(test_number):
    p, a, b = map(int, input().split())
    if search(a) > search(b):
        print('#{} B' .format(tc+1))
    elif search(a) < search(b):
        print('#{} A'.format(tc + 1))
    else:
        print('#{} 0'.format(tc + 1))

