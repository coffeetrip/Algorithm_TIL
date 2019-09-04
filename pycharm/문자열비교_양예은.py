test_number = int(input())
for tc in range(test_number):
    str1 = input()  # 짧음
    str2 = input()  # 김

    str1_idx = 0
    str2_idx = 0
    while str1_idx < len(str1) and str2_idx < len(str2):
        if str2[str2_idx] != str1[str1_idx]:
            str2_idx = str2_idx - str1_idx
            str1_idx = -1
        str2_idx = str2_idx + 1
        str1_idx = str1_idx + 1

    if str1_idx == len(str1):
        print('#{} 1'.format(tc + 1))
    else:
        print('#{} 0'.format(tc + 1))