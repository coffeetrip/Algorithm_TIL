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

```python
def order(n):
    global parent
    global calculator
    global calc
    if n > 0:
        order(ch1[n])
        order(ch2[n])
        if parent[n] == '+':
            result = calc.pop(-2) + calc.pop(-1)
            calc.append(result)
        elif parent[n] == '-':
            result = calc.pop(-2) - calc.pop(-1)
            calc.append(result)
        elif parent[n] == '*':
            result = calc.pop(-2) * calc.pop(-1)
            calc.append(result)
        elif parent[n] == '/':
            result = calc.pop(-2) / calc.pop(-1)
            calc.append(result)
        else:
            calc.append(int(parent[n]))
 
 
calculator = ['+', '-', '*', '/']
T = 10
for tc in range(1, T+1):
    N = int(input())
 
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    parent = [0]*(N+1)
 
    for n in range(N):
        node = input().split()
        for i in range(N+1):
            if i == int(node[0]):
                parent[i] = node[1]
                if len(node) == 3:
                    ch1[i] = int(node[2])
                elif len(node) == 4:
                    ch1[i] = int(node[2])
                    ch2[i] = int(node[3])
 
    calc = []
    order(1)
    print('#{} {}'.format(tc, int(calc[0])))
```

```python
def make(start, end):
    for i in range(end, start-1, -1):
        if p[i] == '/':
            p[i] = p[c1[i]] / p[c2[i]]
        elif p[i] == '+':
            p[i] = p[c1[i]] + p[c2[i]]
        elif p[i] == '-':
            p[i] = p[c1[i]] - p[c2[i]]
        elif p[i] == '*':
            p[i] = p[c1[i]] * p[c2[i]]
 
 
for tc in range(1, 11):
    N = int(input())
    p = [0] * (N+1)
    c1 = [0] * (N+1)
    c2 = [0] * (N+1)
    for i in range(N):
        line = input().split()
        if len(line) == 4:
            p[int(line[0])] = line[1]
            c1[int(line[0])] = int(line[2])
            c2[int(line[0])] = int(line[3])
        else:
            p[int(line[0])] = int(line[1])
    make(1, N)
    print("#{} {}".format(tc, int(p[1])))
```

