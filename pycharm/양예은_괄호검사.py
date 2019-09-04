def search(txt):
    txt_list = list(txt[0])
    print(txt[0])
    for i in range(1, len(txt)):
        if txt[i] != txt_list[-1]:
            txt_list.append(txt[i])
        elif txt[i] == txt_list[-1]:
            txt_list.pop(txt_list[-1])
        print(txt_list)

T = int(input())
for tc in range(1, T+1):
    txt = input()
    print(txt[0])
    result = search(txt)
    #print(f'#{tc} {result}')