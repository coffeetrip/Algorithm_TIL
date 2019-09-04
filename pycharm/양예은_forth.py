t = int(input())
for tc in range(t):
    num = list(input().split())
    oper = ['+', '-', '*', '/', '.']
    num_list = []
    for i in num:
        try:
            if i not in oper:
                num_list.append(i)
            else:
                if i == '+':
                    result = int(num_list.pop(-2)) + int(num_list.pop(-1))
                    num_list.append(result)
                elif i == '*':
                    result = int(num_list.pop(-2)) * int(num_list.pop(-1))
                    num_list.append(result)
                elif i == '/':
                    result = int(num_list.pop(-2)) // int(num_list.pop(-1))
                    num_list.append(result)
                elif i == '-':
                    result = int(num_list.pop(-2)) - int(num_list.pop(-1))
                    num_list.append(result)
                elif i == '.':
                    if num_list not in oper and len(num_list) <= 1:
                        print(f'#{tc+1} {num_list[0]}')
                    else:
                        print(f'#{tc+1} error')
                        break
        except IndexError:
            print(f'#{tc + 1} error')
            break

