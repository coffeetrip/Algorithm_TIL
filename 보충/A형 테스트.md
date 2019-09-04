# A형 테스트

```python
# def diff(NEW, I):
#     print(I)
#     if NEW == up or NEW == down:
#         return I
#     else:
#         return -1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    up = sorted(card)
    down = sorted(card)[::-1]
    result = -1
    for i in range(N):
        new = []
        L = card[:N//2]
        R = card[N//2:]
        if i == 0:
            for j in range(N//2):
                new.append(L[j])
            for k in range(N//2):
                new.append(R[k])
            if new == up or new == down:
                result = i
        elif i == N//2-1:
            for j in range(N//2):
                new.append(L[j])
                new.append(R[j])
            if new == up or new == down:
                result = i
        elif i == N//2:
            for j in range(N//2):
                new.append(R[j])
                new.append(L[j])
            if new == up or new == down:
                result = i
        elif i == N-1:
            for j in range(N//2):
                new.append(R[j])
            for k in range(N//2):
                new.append(L[k])
            if new == up or new == down:
                result = i


    print('#{} {}' .format(tc, result))
```

