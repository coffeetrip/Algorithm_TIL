import sys
sys.stdin = open('input.txt', 'r')

for cc in range(1, 11):
    count = int(input())
    test_list = list(map(int, input().split()))

    good = 0
    for k in range(len(test_list) - 4):
        test_5 = []
        for i in test_list[k:k + 5]:
            test_5.append(i)
        if max(test_5) == test_5[2]:
            so_test = sorted(test_5)
            good += (so_test[4] - so_test[3])
    print('#{} {}'.format(cc, good))