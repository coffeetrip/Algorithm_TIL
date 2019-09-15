### [S/W 문제해결 응용] 3일차 - 공통조상 

```python
(1) 자식을 인덱스로 부모 저장
(2) N1의 조상 i를 빈 배열 a에 표시 a[i] = 1
(3) N2의 조상 j를 배열 a에서 확인 a[j] == 1인 경우
(4) a[j] == 1인 최초의 경우가 N1, N2에서 가장 가까운 공통 조상


c = N1
while par[c]!=0:
    a[par[c]] = 1
    c = par[c]

c = N2
while a[c] == 0:
    c = par[c]
print(c)
```

```python
def parent(n, parent_list):
    global tree
    temp = tree[n]
    if temp != 0:
        parent_list.append(temp)
        parent(temp, parent_list)
    return parent_list

def common_parent(p1, p2):
    for i in p1:
        for j in p2:
            if i == j:
               return i

def subtree(n):
    global ch1, ch2, cnt
    if n > 0:
        cnt += 1
        subtree(ch1[n])
        subtree(ch2[n])
    return cnt

T = int(input())
for tc in range(1, T + 1):
    V, E, common1, common2 = map(int, input().split())  # 정점, 간선
    node = list(map(int, input().split()))
    tree = [0]*(V+1)
    ch1 = [0]*(V+1)
    ch2 = [0]*(V+1)
    for i in range(E):
        p = node[2*i]
        c = node[2*i+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
        tree[c] = p

    parent1 = parent(common1, [])
    parent2 = parent(common2, [])
    common_p = common_parent(parent1, parent2)
    cnt = 0
    subtree(common_p)
    print('#{} {} {}' .format(tc, common_p, cnt))
```

```python
def ancestor(n1, n2):
    global a
    while par[n1] != 0:
        a[par[n1]] = 1
        n1 = par[n1]
    while a[n2] == 0:
        n2 = par[n2]
    return n2


def subtree(n):
    global cnt
    if n > 0:
        subtree(ch1[n])
        subtree(ch2[n])
        cnt += 1


T = int(input())
for tc in range(1, 11):
    V, E, X1, X2 = map(int, input().split())
    t = list(map(int, input().split()))

    a = [0] * (V + 1)
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    par = [0] * (V + 1)
    cnt = 0
    for i in range(V - 1):
        p = t[2 * i]
        c = t[2 * i + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
        par[c] = p

    x = ancestor(X1, X2)
    subtree(x)
    print('#{} {} {}'.format(tc, x, cnt))
```

```python
def find(A):
    global p
    temp = []
    while True:
        if p[A] == 1:
            break
        else:
            A = p[A]
            temp.append(A)
    return temp

def findroot(Alist, Blist):
    for i in Alist:
        if i in Blist:
            return i
    return 1

def findnum(root):
    global c1, c2
    a = c1[root]
    b = c2[root]
    if a and b:
        return findnum(a) + findnum(b) + 1
    elif a:
        return findnum(a) + 1
    elif b:
        return findnum(b) + 1
    else:
        return 1


t = int(input())
for tc in range(1, t + 1):
    V, E, A, B = map(int, input().split())
    gets = list(map(int, input().split()))

    p = [0] * (V + 1)
    c1 = [0] * (V + 1)
    c2 = [0] * (V + 1)
    for i in range(0, E * 2, 2):
        p[gets[i + 1]] = gets[i]
        if c1[gets[i]]:
            c2[gets[i]] = gets[i + 1]
        else:
            c1[gets[i]] = gets[i + 1]

    Alist = find(A)
    Blist = find(B)
    sameroot = findroot(Alist, Blist)
    allnums = findnum(sameroot)
    print("#{} {} {}".format(tc, sameroot, allnums))
```

