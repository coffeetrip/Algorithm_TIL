def search(ab):
    l = 1
    r = p_a_b[0]
    c = (l + r) // 2
    count = 1
    while p_a_b[ab] != c:
        c = (l + r) // 2
        if p_a_b[ab] > c:
            l = c
            count += 1
        elif p_a_b[ab] < c:
            r = c
            count += 1
    return count


test_num = int(input())
for i in range(test_num):
    p_a_b = list(map(int, input().split()))

    count_list = []
    for j in range(1, 3):
        ccount = search(j)
        count_list.append(ccount)
    if count_list[0] < count_list[1]:
        print('#{} {}' .format(i+1, 'A'))
    elif count_list[0] > count_list[1]:
        print('#{} {}'.format(i + 1, 'B'))
    else:
        print('#{} {}'.format(i+1, '0'))