# IM대비

```
문제 조건
- 좌표(0,0) -> (N-1, M-1)
- 칠하는 조건 : 명도가 크면 칠할 수 있음, 칠하려는 영역에 칠해진 명도가 크면 칠할 수 없음
- 넓이가 1인 경우도 있음
- 명도 범위 0~10

출력
가장 넓게 칠해진 명도에 해당하는 칸 수 

풀이
- NxM 빈 배열을 준비하고 일단 칠한다.
= 칠할 수 있는 영역인지 확인한다.(더 큰 명도 칸이 있는지 확인)
= 더 큰 명도칸이 없는 영역이면 새 명도를 칠한다.
- 전체 영역에 대해 각 명도의 개수를 기록한다. 0~10번 카운트 배열 작성
- 카운트 배열에서 가장 큰 값을 출력한다.
```

```python
# 1차원
result = 0
for i in range(N):
    if arr[i] == 1:
        result = 1
        break
```

```python
# 2차원 -> 좋지 않음(전부 다 돈다.)
result = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            result = 1
```

```python
T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())  # 행, 열, 페인트를 칠하는 횟수
    DRAW = [[0]*M for _ in range(N)]

    for kc in range(K):  # 칠하기
        x1, y1, x2, y2, P = map(int, input().split())   # 행열행열 페인트의 명도

        # 해당 영역에 더 큰 명도로 칠해진 칸이 있는지 확인
        result = 0
        for r in range(x1, x2+1):
            for c in range(y1, y2+1):
                if DRAW[r][c] > P:
                    result = 1

        # 칠할 수 있으면 칠함
        if result == 0:  # 더 큰 명도가 없었으면
            for r in range(x1, x2+1):
                for c in range(y1, y2+1):
                    DRAW[r][c] = P

    # 명도 개수 기록
    bright = [0]*11  # 0번~10번
    for i in range(N):
        for j in range(M):
            bright[DRAW[i][j]] += 1
    print('#{} {}' .format(test_case, max(bright)))
```

```
1
7 12 4
1 1 4 7 2
3 3 6 11 6
2 9 5 10 10
0 7 1 11 1
```

```
#1 30
0 0 0 0 0 0 0 0 0 0 0 0 
0 2 2 2 2 2 2 2 0 0 0 0 
0 2 2 2 2 2 2 2 0 10 10 0 
0 2 2 6 6 6 6 6 6 10 10 6 
0 2 2 6 6 6 6 6 6 10 10 6 
0 0 0 6 6 6 6 6 6 10 10 6 
0 0 0 6 6 6 6 6 6 6 6 6 
```





##  ss텔레콤

ss텔레콤에서 현재 기지국의 위치와 집들이 표시된 지도를 2차원 nxn배열로 변환하여, 기지국에 커버되지 않은 집의 수를 찾고자 한다.

기지국은 그림1과 같이 세가지 종류가 있다. 각각의 기지국은 기지국이 위치한 셀에서 동서남북으로 각 1개 2개 3개의(abc) 셀을 커버하며 하나의 집은 1개의 셀에 있다.

```
기지국과 집 위치를 2차원 리스트에 저장한다.
모든 영역에서 기지국을 찾는다.

기지국 타입에 따라 커버되는 집을 지운다.
전체 영역에 남은 집의 개수를 출력한다.
```

```python
def cover(i, j, N):
    k = 0
    if arr[i][j] == 'A':
        k = 1
    elif arr[i][j] == 'B':
        k = 2
    elif arr[i][j] == 'C':
        k = 
    for h in range(1, k+1):
        if j+h < N:
            arr[i][j+h] = 'X'   # 오
        if i+h < N:
            arr[i+h][j] = 'X'   # 아 
        if j-h >= 0:
            arr[i][j-h] = 'X'   # 왼
        if i-h >= 0:
            arr[i-h][j] = 'X'   # 위


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 기지국과 집 정보 입력
    arr = [list(input()) for _ in range(N)]
    # 기지국 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A' or 'B' or 'C':
                # 커버되는 집 지우기
                cover(i, j, N)

    # 남은 집 개수 세기
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1
```

```
1
9
XXXXXXXXX
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX
XXXXXXXXX
```

```
#1 4
X X X X X X X X X 
X X X X X X X X X 
X X X A X X X H X 
X X H X X X X X X 
X X X X X X X X X 
X X A X H X X X X 
X X X X X X A X X 
X X A X X X X X X 
X X X X H X X X X 
```



