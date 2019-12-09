# SW문제해결_4day

## 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기

```python
def paper(num):
    if num == 1:
        return 1
    elif num == 2:
        return 3
    else:
        return paper(num-1) + 2*paper(num-2)

for tc in range(1, int(input())+1):
    n = int(input())
    print(f'#{tc} {paper(n//10)}')
```

재귀함수를 이용한 방법

```python
for tc in range(1, int(input())+1):
    n = int(input())

    f = [1]   # n = 0
    f.append(1)   # n = 1
    f.append(3)   # n = 2
    for i in range(3, (n//10)+1):
        f.append(f[i-1] + 2*f[i-2])
    print(f'#{tc} {f[-1]}')
```

for 반복문을 이용한 스택쌓기

```python
for tc in range(1, int(input())+1):
    n = int(input())

    f = [0]*(n//10+1)
    f[1] = 1
    f[2] = 3
    for i in range(3, (n//10)+1):
        f[i] = f[i-1] + 2*f[i-2]
    print(f'#{tc} {f[-1]}')
```

for 반복문을 이요한 스택쌓기 2

```python
def paper(n):
    global result
    if n >= 2 and result[n] == 0:
        result[n] = paper(n-1) + paper(n-2)*2
    return result[n]

t = int(input())
for tc in range(1, t+1):
    N = int(input())

    result = [0]*(N//10+1)
    result[1] = 1
    result[2] = 3
    final = paper(N//10)
    print(f'#{tc} {final}')
```

메모이제이션을 이용한 방법

```python
f = [1,3]
for i in range(2, n//10):
    f.append(f[i-1] + 2*f[i-2])
print(f[-1])
```

for 반복문을 이용한 스택쌓기









## 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사

```
#모든 글자에 대해
(1) 여는 괄호 '{' 또는 '(' 인 경우  push()
(2) 닫는 괄호인 경우
(2-1) '}'인 경우
	pop() 결과 짝이 맞으면. '{'인 경우 계속
	아니면 중지(비정상)
(2-2) ')'인 경우
	pop() 결과 짝이맞으면 계속
	아니면 중지(비정상)
# 모든 글자에 대한 검토 후
스택에 남은 괄호가 있으면 비정상
남은 괄호가 없으면 정상
```

```python
def parentheses(word):
    paren = []
    for i in word:
        if i == '(' or i == '{':
            paren.append(i)
        elif i == ')':
            if len(paren) != 0 and paren[-1] == '(':
                paren.pop()
            else:
                return 0
        elif i == '}':
            if len(paren) != 0 and paren[-1] == '{':
                paren.pop()
            else:
                return 0
    if len(paren) != 0:
        return 0
    else:
        return 1


for tc in range(1, int(input())+1):
    Word = input()
    print(f'#{tc} {parentheses(Word)}')
```



## 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로

#### 반복

```python
def dfs1(n, G, V):  # 반복구조, 각 노드를 1번씩만 방문
    visited = [0]*(V+1)
    s = []  # 스택 생성
    s.append(n)  # 시작노드 push(), 방문할 노드를 저장
    visited[n] = 1  # push()한 노드를 표시

    while s:  # 방문하지 않은 노드가 있으면(갈림길에서 남겨놓은 노드가 있으면)
        visited[n] = 1
        n = s.pop()  # 갈림길에서 하나를 선택
        # print(n, end=" ")  # 처리 순서를 출력
        if n == G:
            return 1
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i] == 0:  # i가 n에 인접하고 방문하지 않은노드면
                s.append(i)
                visited[i] = 1
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    result = 0
    for i in range(E):  # 간선 정보로부터 인접행렬 만들기
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
    S, G = map(int, input().split())

    result = dfs1(S, G, V)
    print('#{} {}' .format(tc, result))
```

#### 재귀

```python
def dfs2(n, G, V):  # 각 노드를 1번씩만 방문
    visited2[n] = 1
    if n == G:
        return 1
    else:
        # n에 인접하고, 방문하지 않은 노드로 이동
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited2[i] == 0:  # i가 n에 인접하고
                if dfs2(i, G, V) == 1:
                    return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    result = 0
    for i in range(E):  # 간선 정보로부터 인접행렬 만들기
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
    S, G = map(int, input().split())

    visited2 = [0]*(V+1)
    result = dfs2(S, G, V)
    print('#{} {}' .format(tc, result))
```



```python
def stack(S, G):
    global link
    for i in range(len(link[S])):
        if link[S] == []:
            return 0
        a = link[S].pop()
        if G in link[a]:
            return 1
        else:
            if stack(a, G) == 1:
                return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    link = {}
    for vv in range(1, 1+V):
        link[vv] = []

    for ec in range(E):
        node1, node2 = map(int, input().split())
        link[node1].append(node2)

    S, G = map(int, input().split())
    print('#{} {}' .format(tc, stack(S, G)))
```

```python
def f(S, G):
    global result
    for i in range(E):
        a = line[i][0]
        b = line[i][1]
        if S == a:
            if G == b:
                result = 1
            else:
                f(b, G)


T= int(input())
for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    line = [list(map(int, input().split())) for _ in range(E)]
    S, G = list(map(int, input().split()))

    result = 0
    f(S, G)
    print('#{} {}'.format(tc, result))
```

```python
def find(S, G):
    global spider
    for i in range(len(spider[S])):
        if spider[S] == []:
            return 0
        a = spider[S].pop()
        if a == G:
            return 1
        elif G in spider[a]:
            return 1
        else:
            if a != S:
                if find(a, G) == 1:
                    return 1
    return 0


t = int(input())
for tc in range(1, t + 1):
    V, E = map(int, input().split())
    spider = {i: [] for i in range(1, V + 1)}
    for i in range(E):
        start, end = map(int, input().split())
        spider[start].append(end)
    S, G = map(int, input().split())
    res = find(S, G)
    print("#{} {}".format(tc, res))
```

```python
def DFS(start):
    global result
    visited[start] = 1
    for next in range(1, V+1):
        if MyMap[start][next] and not visited[next]:
            if next == end_node:
                result = 1
                return
            DFS(next)


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())   # V노드 E간선
    MyMap = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V+1)

    for i in range(E):
        start, end = map(int, input().split())
        MyMap[start][end] = 1

    start_node, end_node = map(int, input().split())   # S, G
    result = 0
    DFS(start_node)
    print(f'#{tc} {result}')
```







## 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기

```
모든 글자에 대해
	스택이 비어있지 않으면 현재 글자를 마지막으로 저장된 글자와 비교
	일치하면 pop() 하고 버림
   	일치하지 않으면 push()
스택이 비어있으면
	push()
```

```python
def repeat(word):
    new_word = []
    for i in word:
        if len(new_word) == 0:
            new_word.append(i)
        elif len(new_word) != 0 and new_word[-1] == i:
            new_word.pop()
        elif len(new_word) != 0 and new_word[-1] != i:
            new_word.append(i)
    return len(new_word)

for tc in range(1, int(input())+1):
    Word = input()
    print(f'#{tc} {repeat(Word)}')
```

```python
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
```

```python
#  선생님 코드
t = int(input())
for tc in range(1, t+1):
    txt = input()
    s = list()
    s.append(txt[0])

    for i in range(1, len(txt)):
        # 스택이 비어있거나 스택의 맨 위 글자와 다르면 push(txt[i]), 같으면 pop(txt[i])
        if len(s) == 0 or s[-1] != txt[i]:
            s.append(txt[i])
        else:
            s.pop()
    print('#{} {}' .format(tc, len(s)))
```

```python
def repeat(txt):
    s = list()
    for i in range(len(txt)):
        s.append(txt[i])
        if len(s) > 1:
            if s[-1] == s[-2]:
                s.pop()
                s.pop()
    return len(s)

T = int(input())
for tc in range(1, T+1):
    words = input()
    print('#{} {}'.format(tc, repeat(words)))
```

```python
# 문자열 조작
for t in range(int(input())):
    text = input()
    res = text[0]
    for i in text[1:]:
        if len(res) != and i == res[-1]:
            res = res[:-1]
        else:
            res += i
   	print(f'#{t+1} {len(res)}')
```

```python
def repeat(txt):
    s = list()
    for i in range(len(txt)):
        s.append(txt[i])
        if len(s) > 1:
            if s[-1] == s[-2]:
                s.pop()
                s.pop()
    return len(s)

T = int(input())
for tc in range(1, T+1):
    words = input()
    print('#{} {}'.format(tc, repeat(words)))
```



