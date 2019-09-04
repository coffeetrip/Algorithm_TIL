arr = [1, 2, 3]
bit = [0, 0, 0]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            print(bit)
            for m in range(3):
                if bit[m] != 0:  # m번 원소가 부분집합에 포함되면
                    print(arr[m], end=' ')
            print()


