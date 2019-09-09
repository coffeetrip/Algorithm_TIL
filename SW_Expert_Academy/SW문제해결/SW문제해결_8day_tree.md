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
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())   # 간선의 개수

    node = list(map(int, input().split()))
    #
    # ch1 = [0]*(E+2)
    # ch2 = [0]*(E+2)
    #
    # for i in range(E):
    #     p = node[2*i]
    #     c = node[2*i + 1]
    #     if ch1[p] == 0:
    #         ch1[p] = c
    #     else:
    #         ch2[p] = c
    # print(ch1)
    # print(ch2)
    # for i in range(E+1):
    #     if N == ch1[i]:
    #         result = len(ch1) - ch1.count(0) - 1
    #         break
    #     elif N == ch2[i]:
    #         print(ch2.count(0))
    #         result = len(ch2) - ch2.count(0) - 1
    #         break
    #
    # print('#{} {}' .format(tc, result))
    node_dict = {}
    for i in 
```

