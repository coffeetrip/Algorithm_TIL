def paper(n):
    global result
    if n >= 2 and result[n] == 0:
       result[n] = paper(n-1) + paper(n-2)*2
    return result[n]

t = int(input())
for tc in range(t):
    N = int(input())

    result = [0] * (N + 1)
    result[0] = 1
    result[1] = 3
    final = paper(int(N//10)-1)
    print("#{} {}".format(tc+1, final))