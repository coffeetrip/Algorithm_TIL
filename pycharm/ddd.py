def search(txt):
    txt = list(txt)
    i = 1
    while len(txt) > i:
        if txt[i] != txt[i-1]:
            i += 1
        elif txt[i] == txt[i-1]:
            txt.pop(i-1)
            txt.pop(i-1)
            i = 1
    return len(txt)

T = int(input())
for tc in range(1, T+1):
    txt = input()
    print(f'#{tc} {search(txt)}')