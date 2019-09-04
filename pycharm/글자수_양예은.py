test_case = int(input())
for tc in range(test_case):
    str1 = input()
    str2 = input()

    str1_dict = {}
    for i in str1:
        str1_dict[i] = 0

    for j in str2:
        for k in str1_dict:
            if j == k:
                str1_dict[j] += 1

    dict_value = []
    for idx, value in str1_dict.items():
        dict_value.append(value)
    result = max(dict_value)
    print('#{} {}'.format(tc + 1, result))