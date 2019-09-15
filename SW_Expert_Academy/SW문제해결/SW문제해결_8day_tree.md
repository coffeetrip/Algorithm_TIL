### 5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색 

```python
def inorder(n, last):
    global cnt
    if n<=last:   # 유효한 노드면(n이 마지막노드 이내면)
        inorder(n*2, last)    # 왼쪽 자식으로 이동
        tree[n] = cnt   # visit()
        cnt += 1
        inorder(n*2+1, last)  # 오른쪽 자식으로 이동


T = int(input())
for tc in range(1, T+1):
    N = int(input())   #6
    E = N - 1    # 5
    tree = [0]*(N+1)
    cnt = 1
    inorder(1, N)
    print('#{} {} {}' .format(tc, tree[1], tree[N//2]))
```



### 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree

```python
def subtree(N):
    global left
    global right
    global cnt
    if N > 0:
        cnt += 1
        subtree(left[N])
        subtree(right[N])
    return cnt


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    node_pair = list(map(int, input().split()))

    left = [0]*(E+2)
    right = [0]*(E+2)
    for i in range(E):
        p = node_pair[2*i]
        c = node_pair[2*i+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    cnt = 0
    print('#{} {}' .format(tc, subtree(N)))
```

```python
def subtree(N):
    global cnt, child
    for i in range(len(child)):
        if child[i] == N:
            cnt += 1
            temp = i
            subtree(temp)
    return cnt


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    node_pair = list(map(int, input().split()))

    child = [0]*(E+2)
    for i in range(E):
        p = node_pair[i*2]
        c = node_pair[i*2+1]
        child[c] = p

    cnt = 1
    print('#{} {}' .format(tc, subtree(N)))
```

```python
def find(N, link1, link2):
    global cnt
    if link1[N] == 0:
        return cnt
    if link1[N] != 0:
        temp = link1[N]
        cnt += 1
        find(temp, link1, link2)
    if link2[N] != 0:
        temp = link2[N]
        cnt += 1
        find(temp, link1, link2)
    return cnt


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    node = list(map(int, input().split()))

    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)
    for i in range(E):
        p = node[2 * i]
        c = node[2 * i + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    cnt = 1
    find(N, ch1, ch2)

    print('#{} {}'.format(tc, cnt))
```





### 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    node = [0] + list(map(int, input().split()))
    tree = [0]*(N+1)

    for i in range(1, N+1):
        tree[i] = node[i]
        if tree[i//2] > tree[i]:
            temp = i
            while tree[temp//2] > tree[temp]:
                tree[temp//2], tree[temp] = tree[temp], tree[temp//2]
                temp = temp//2
    #print(tree)
    j = N
    s = 0
    while j > 0:
        j = j // 2
        s += tree[j]
    print('#{} {}' .format(tc, s))
```

```python
def enq(n):
    global last
    # 완전 이진트리 유지
    last += 1   # 마지막 노드를 추가하고
    heap[last] = n  # 마지막 노드에 데이터 저장
    # 최소힙 유지(부모 노드의 데이터가 더 작음)
    c = last
    while(c//2>0 and heap[c//2]>heap[c]):  # 부모가 있고, 부모 노드의 데이터가 더 크면 교환
        heap[c // 2], heap[c] = heap[c], heap[c//2]
        c = c//2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = [0]*(N+1)
    num = list(map(int, input().split()))
    last = 0
    for x in num:
        enq(x)
    s = 0
    c = last
    while c//2>0:
        s += heap[c//2]
        c = c//2
    print('#{} {}' .format(tc, s))
```

```python
def parent(i):
    global I
    m = i//2
    if tree[m] > tree[I]:
        parent(m)
    return m

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    node = [0] + list(map(int, input().split()))
    tree = []
    tree.append(node.pop(0))
    tree.append(node.pop(0))
    tree.append(node.pop(0))

    i = 2
    while i <= N:
        I = i
        temp = parent(i)
        if tree[temp] > tree[I]:
            tree[temp], tree[I] = tree[I], tree[temp]
        i += 1
        if len(node) != 0:
            tree.append(node.pop(0))
    # print(tree)
    j = N
    s = 0
    while j > 0:
        j = j // 2
        s += tree[j]
    print('#{} {}' .format(tc, s))
```



### 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합 

```python
def postorder(n, last):
    global tree
    if n <= last:
        postorder(n*2, last)
        postorder(n*2+1, last)
        tree[n//2] += tree[n]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for mc in range(M):
        p, c = map(int, input().split())
        tree[p] = c

    postorder(1, N)
    print('#{} {}' .format(tc, tree[L]))
```

```python
def make(start, end):
    global N
    if start <= end:
        make(start * 2, end)
        make(start * 2 + 1, end)
        if visit[start] == 0:
            if start*2 +1 <= N:
                visit[start] = visit[start*2] + visit[start*2+1]
            else:
                visit[start] = visit[start*2]


t = int(input())
for tc in range(1, t + 1):
    N, M, L = map(int, input().split())
    visit = [0] * (N + 1)
    for i in range(M):
        nodenum, num = map(int, input().split())
        visit[nodenum] = num
    save1 = 0
    save2 = 0
    before = 0
    make(1, N)
    if visit[2] and visit[3]:
        visit[1] = visit[2] + visit[3]
    # print(visit)
    print("#{} {}".format(tc, visit[L]))

```

```python
TC = int(input())
for t in range(TC):
    N, M, L = map(int, input().split())

    tree = [0]*(N+1)
    for i in range(M):
        node, num = map(int, input().split())
        tree[node] = num

    for i in range(M-1):
        if N % 2 == 0:
            if i == 0:
                tree[(N-(2*i))//2] = tree[N-(2*i)]
            else:
                tree[(N-(2*i))//2] = tree[N-(2*i)] + tree[N-(i*2)+1]
        else:
            tree[(N-(2*i))//2] = tree[N-(2*i)] + tree[N-(i*2)-1]

    print('#{} {}'.format(t+1, tree[L]))
```

