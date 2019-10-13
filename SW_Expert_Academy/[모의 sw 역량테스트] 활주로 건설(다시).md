# [모의 sw 역량테스트] 활주로 건설

```
왼쪽에서 오른쪽으로 내리막
오른쪽에서 왼쪽으로 내리막
경사로설치한 부분은 기록을해야한다.
```

```python
def


def f(n, x):
    cnt = 0
    for i in range(n):
        code = []
        c = 1
        idx = 1
        for idx in range(1, n):  # 1 줄의 높이 정보를 높이 - 폭으로 기록
            if m[j][0] - code[j-1][0] == 1: 
```

```python
def f(airstrip):
    global temp
    for j in range(N):
        cnt = 0
        result = 0
        for i in range(N-1):
            if airstrip[j][i] < airstrip[j][i+1]:
                if i + 1 >= X:
                    if len(set(airstrip[j][i-X+1:i+1])) == 1:
                        cnt += 1
                    else:
                        result = 1
                else:
                    result = 1
            elif airstrip[j][i] > airstrip[j][i+1]:
                if i + X < N:
                    if len(set(airstrip[j][i+1:i+X+1])) == 1:
                        cnt += 1
                    else:
                        result = 1
                else:
                    result = 1

        if cnt >= 1 and result == 0:
            temp += 1

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr1 = list(map(list, zip(*arr)))
    temp = 0
    f(arr)
    f(arr1)
    print(temp)
```

