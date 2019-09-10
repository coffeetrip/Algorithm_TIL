### [S/W 문제해결 기본] 9일차 - 사칙연산

```python
op = ['+', '-', '*', '/']
def f(n, last):
    if tree[n] in op:
        r1 = f(ch1[n], last)
        r2 = f(ch2[n], last)
        if tree[n] == '+':
            return r1 + r2
        elif tree[n] == '-':
            return r1 - r2
        elif tree[n] == '*':
            return r1 * r2
        elif tree[n] == '/':
            return r1 / r2
    else:
        return int(tree[n])


for tc in range(1, 11):
    N = int(input())
    tree = [0]*(N+1)
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    for i in range(N):
        node = list(input().split())
        if len(node) > 2:
            ch1[int(node[0])] = int(node[2])
            ch2[int(node[0])] = int(node[3])
        tree[int(node[0])] = node[1]
    r = f(1, N)
    print('#{} {}' .format(tc, int(r)))
```

```python
op = ['+', '-', '/', '*']
def order(n, N):
    global tree
    if tree[n] in op:
        l = order(ch1[n], N)
        r = order(ch2[n], N)

        if tree[n] == '+':
            return l + r
        elif tree[n] == '-':
            return l - r
        elif tree[n] == '*':
            return l * r
        elif tree[n] == '/':
            return l / r
    else:
        return int(tree[n])

for i in range(1, 11):
    N = int(input())   # 정점의 총 수
    tree = [0]*(N+1)
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    for nc in range(N):
        num = list(input().split())
        if len(num) > 2:
            ch1[int(num[0])] = int(num[2])
            ch2[int(num[0])] = int(num[3])
        tree[int(num[0])] = num[1]
    #print(tree)
    print('#{} {}' .format(i, int(order(1, N))))
```

