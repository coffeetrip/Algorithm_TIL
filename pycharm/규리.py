Test = 1
for tc in range(Test):
    dump = 826
    box = list(map(int, input().split()))
    # big = 0
    # small = 1000
    max_box = 0
    min_box = 0
​
    for d in range(dump):
        for i in range(len(box)):
            if box[max_box] < box[i]:
                max_box = i
            if box[min_box] > box[i]:
                min_box = i

        if box[max_box] - box[min_box] > 1:
            box[max_box] -= 1
            box[min_box] += 1
        else:
            print(box[max_box] - box[min_box])
            break
    print(box[max_box] - box[min_box])