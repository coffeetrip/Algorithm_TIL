# SW문제해결_5day

## 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth

```python
t = int(input())
for tc in range(t):
    num = list(input().split())
    oper = ['+', '-', '*', '/', '.']
    num_list = []
    for i in num:
        try:
            if i not in oper:
                num_list.append(i)
            else:
                if i == '+':
                    result = int(num_list.pop(-2)) + int(num_list.pop(-1))
                    num_list.append(result)
                elif i == '*':
                    result = int(num_list.pop(-2)) * int(num_list.pop(-1))
                    num_list.append(result)
                elif i == '/':
                    result = int(num_list.pop(-2)) // int(num_list.pop(-1))
                    num_list.append(result)
                elif i == '-':
                    result = int(num_list.pop(-2)) - int(num_list.pop(-1))
                    num_list.append(result)
                elif i == '.':
                    if num_list not in oper and len(num_list) <= 1:
                        print(f'#{tc+1} {num_list[0]}')
                    else:
                        print(f'#{tc+1} error')
                        break
        except IndexError:
            print(f'#{tc + 1} error')
            break


```

```PYTHON
T = int(input())
for case in range(1, T+1):
	formula = input().split()
	stack = []
	for ele in formula:
		if ele.isnumeric():
			stack.append(ele)
		elif ele == '.':
			if len(stack) != 1:
				print(f'#{case} error')
				break
			print(f'#{case} {stack[0]}')
			break
		else:
			try:
				if len(stack) < 1:
					print(f'#{case} error')
					break
				t2 = int(stack.pop())
				t1 = int(stack.pop())
			except(IndexError):
				print(f'#{case} error')
				break
			except(ValueError):
				print(f'#{case} error')
				break
			if ele == '+':
				stack.append(t1 + t2)
			elif ele == '-':
				stack.append(t1 - t2)
			elif ele == '*':
				stack.append(t1 * t2)
			elif ele == '/':
				try:
					stack.append(t1 // t2)
				except(ZeroDivisionError):
					print(f'#{case} error')
					break
			else:
				print(f'#{case} error')
				break
```



## 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로

```python
# 재귀를 이용한 미로찾기
def f(i, j):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    global maze
    global N
    # if maze[i][j] == '1':   # 벽이면
    #     return 0
    if maze[i][j] == '3':   # 목적지면
        return 1
    else:
        maze[i][j] = '1'   # 방문 표시, 벽으로 바꿈
        # 이동할 좌표 생성
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni>=0 and ni<N and nj>=0 and nj<N:
                if maze[ni][nj] != '1':  # 벽이 아니면 방문 (0,3)
                    if f(ni, nj) == 1:  # 진행방향에서 목적지를 찾은 경우
                        return 1
        return 0  # 현재위치에서 갈 수 있는 방햐에서 목적지를 찾지 못함. 이전의 다른 방향 탐색


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    # 시작점 찾기
    startI = 0
    startJ = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                startI = i
                startJ = j
    print('#{} {}' .format(tc, f(startI, startJ)))
```

```
감사합니다 정우님. 덕분이 재귀를 이해했습니다!!!
if miro(ni, nj) == 1:    # 여기 1은 '3'의 리턴값
     return 1
이부분을 좀더 디테일하게 하면
next_ = miro(ni, nj)
if next_ == 1:
   return 1
   
저 위에 miro라는 함수는 리턴 조건이 for문이 다 돌았을때, 3을 만났을때 재귀에서 1이 리턴됐을때 인데
일단 미로를 여러칸이라고 생각하지않고 바로 밑에 칸에 도착점이 있다고 생각해봐
1, 1에서 출발을 하면
miro(1, 1)이 돌아가잔아 그리고 for문 돌면서 오른쪽 좌표부터 받으니깐
mori(1, 2)로 다시 재귀가 들어가겠지
그러면 miro(1, 1) 함수는 지금 for문 k가 0에 멈춘상태인거고
miro(1, 2)는 돌아가고 있어
miro(1, 2)에서 1, 2가 3이면 리턴 1이 되잔아
그럼 miro(1,2) 함수가 종료하고
miro(1,1) 함수로 돌아가
if miro(ni, nj) == 1:  이 위치로
그럼 miro(1, 2)에서 1이 리턴되었으니깐
miro(1,1) if문 안쪽으로 들어가서 1을 리턴하게 되는거지
그럼 마지막에 1이 찍히는거야
```

```python
# 스택이용
def find(sRow, sCol):
    dRow = [0, 1, 0, -1]
    dCol = [1, 0, -1, 0]
    s = []
    s.append([sRow,sCol])    # 입구로 이동
    maze[sRow][sCol] = 1     # 방문 표시
    while len(s) != 0:
        n = s.pop()          # 이동할 칸 좌표를 꺼내고
        for i in range(4):    # 주변 좌표 계산
            nRow = n[0] + dRow[i]
            nCol = n[1] + dCol[i]
            if nRow >=0 and nRow<N and nCol>=0 and nCol <N:  # 미로 내부인지 확인
                if maze[nRow][nCol] == '3':     # 목적지인 경우 1반환
                    return 1
                elif maze[nRow][nCol] == '0':    # 갈 수 있는 곳 저장
                    s.append([nRow, nCol])
                    maze[n[0]][n[1]] = 1
    return 0    # 출구에 가지 못하고 모든칸 방문

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    startI = 0
    startJ = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                startI = i
                startJ = j
    print('#{} {}' .format(tc, find(startI, startJ)))
```





### 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합

```python
def f(n, k, s):
    global minV
    if n == k:
        if minV > s:
            minV = s
        return
    elif minV < s:
        return
    else:
        for i in range(n, k):
            bit[i], bit[n] = bit[n], bit[i]
            f(n+1, k, s + array[n][bit[n]])
            bit[i], bit[n] = bit[n], bit[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    bit = list(range(N))
    minV = 1000000000
    f(0, N, 0)
    print('#{} {}' .format(tc, minV))
```

