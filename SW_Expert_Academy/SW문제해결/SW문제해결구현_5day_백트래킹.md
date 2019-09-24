### SW문제해결 응용_구현 - 05 백트래킹

### 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2

```python
def f(n, k, battery, cnt):    # n번 정류장에 도착할때 남은 에너지
    global min_cnt

    if n == k:
        if min_cnt > cnt:
            min_cnt = cnt
        return
    elif cnt > min_cnt:
        return
    elif n < k:
        if battery-1 >= 0:
            f(n+1, k, battery-1, cnt)   # 통과
        f(n + 1, k, M[n] - 1, cnt + 1)  # 교체



T = int(input())
for tc in range(1, T + 1):
    M = list(map(int, input().split()))

    min_cnt = 1000000
    f(1, M[0], M[1], 0)

    print('#{} {}' .format(tc, min_cnt))
```

```python
# 함수(지금 정류장 번호, 마지막 정류장번호, 배터리, 교체횟수)
def check(n, m, b, c):
	global min_cnt
	# 배터리를 하나씩 빼니까 음수가 될수도 있음. 그경우는 아예 뺴버려야함
	if b < 0:
		return
	# 지금정류장번호랑 마지막이 같으면 끝
	elif n == m:
		if min_cnt > c:
			min_cnt = c
			return
	elif c > min_cnt:
		return
	elif n < m:
		# 다음 정류장을 통과할때(다음으로 가면서 하나뺌)
		check(n + 1, m, b-1, c)
		# 다음 정류장에서 교체할때(다음으로 가면서 하나뺌)
		check(n + 1, m, battery[n]-1, c + 1)
        
T = int(input())
for tc in range(1, T + 1):
	# 정류장 수 battery[0], 정류장별 배터리 용량
	battery = list(map(int, input().split()))
	# 교체의 최소 횟수를 세야하니까
	min_cnt = 1000
	check(1, battery[0], battery[1], 0)
	print('#{} {}'.format(tc, min_cnt))
```

```python
def f(n, m): # n:도착점, m:시작점
    global cnt
    if m != 0:
        if m - n <= M[n]:
            cnt += 1
            f(0, n)
        else:
            f(n+1, m)


T = int(input())
for tc in range(1, T+1):
    NM = list(map(int, input().split()))
    N = NM[0]
    M = NM[1:]
    cnt = 0
    f(0, N-1)
    print('#{} {}'.format(tc, cnt-1))
```

```python
def f(n, k, s, c):
    global minV, M
    if s < 0 or c > minV:
        return
    if n == k:
        if minV > c:
            minV = c
        return
    else:
        f(n + 1, k, M[n] - 1, c + 1)
        f(n + 1, k, s - 1, c)

T = int(input())
for t in range(1, T + 1):
    inp = list(map(int, input().split()))
    N = inp[0]
    M = [0] + inp[1:]
    minV = 999
    f(1, N, 0, 0)
    print("#{} {}".format(t, minV-1))
```

```python
def find(now):
    global minV, stations, N
    for i in range(now):
        if now - i <= stations[i]:
            minV += 1
            find(i)
            break


t = int(input())
for tc in range(1, t+1):
    stations = list(map(int, input().split()))
    N = stations[0]
    stations = stations[1:]
    minV = 0
    find(N-1)
    print("#{} {}".format(tc, minV-1))
```

```python
def f(i, d, cnt):
    global minV
    global stations
    global N

    if i == N - 1:
        if cnt < minV:
            minV = cnt
    elif cnt > minV:
        return
    else:
        for dx in range(1, d + 1):
            ni = i + dx

            if ni < N - 1:
                f(ni, stations[ni], cnt + 1)
            elif ni == N - 1:  # 목적지까지 바로 갈 수 있을때
                if cnt < minV:
                    minV = cnt


T = int(input())

for tc in range(1, T + 1):
    info = list(map(int, input().split()))

    N = info[0]
    stations = info[1:]
    minV = len(stations)
    f(0, stations[0], 0)
    print("#{} {}".format(tc, minV))
```



```PYTHON
# 백트래킹이 아님
T = int(input())

def compare(i, charge):
    global battery_station

    for c in range(0, charge + 1):
        if battery_station[i + c] > battery_station[i]:
            return False
    return True


for tc in range(1, T + 1):
    battery = list(map(int, input().split()))
    N = battery[0]
    battery_station = [0] + battery[1:] + [0]

    cnt = 0
    charge = battery_station[1] - 1

    i = 2
    while i < N:
        if battery_station[i] > charge and compare(i, charge) or charge == 0:
            cnt += 1
            charge += battery_station[i]

        i += 1
        charge -= 1
    print('#{} {}'.format(tc, cnt))
```

compare(i, charge)





### 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용

```python
def f(n, k, value):
    global minV
    if n == k:
        if minV > value:
            minV = value
        return
    elif minV < value:
        return
    else:
        for i in range(n, k):
            p[i], p[n] = p[n], p[i]
            f(n+1, k, value + line[p[n]][n])
            p[i], p[n] = p[n], p[i]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    line = [list(map(int, input().split())) for _ in range(N)]

    p = [i for i in range(0, N)]
    minV = 1000000
    f(0, N, 0)
    print('#{} {}' .format(tc, minV))
```

```python
# 현재 row, 지금까지 선택된 공장(column)들, 지금까지 든 비용
def DFS(i, selected_factories, total_cost):
    global costs
    global N
    global minV
    global factories

    # 맨 마지막 줄에 도달하면 종료
    if i == N - 1:
        if total_cost < minV:
            minV = total_cost
    else:
        for j in factories - selected_factories:  # 이미 선택한 공장(column)을 제외한 나머지 공장중 하나를 선택한다.
            next_row = i + 1  # 같은 제품은 선택 할 수 없으므로 무조건 다음 row로 넘어간다
            next_cost = total_cost + costs[next_row][j]

            if next_cost < minV:  # 다음 가격이 현재 최소보다 작을 경우에만 더 탐색을 진행하도록 한다
                next_selected_factories = selected_factories | {j}
                DFS(next_row, next_selected_factories, next_cost)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    costs = [list(map(int, input().split())) for _ in range(N)]

    minV = 99 * N

    factories = set(i for i in range(N))

    for j in range(N):
        DFS(0, {j}, costs[0][j])  # 첫번째 줄 모든 column이 출발점이 될 수 있음

    print("#{} {}".format(tc, minV))
```

```python
def solution(depth, n, temp, history):
    global status, price
    if depth == n:
        if temp < price:
            price = temp
    else:
        for index in range(size):
            if index not in history:
                if temp + status[depth][index] < price:
                    history.append(index)
                    solution(depth + 1, n, temp + status[depth][index], history)
                    history.remove(index)


for t in range(int(input())):
    size = int(input())
    status = [list(map(int, input().split())) for _ in range(size)]
    price = sum([status[_][_] for _ in range(size)])
    solution(0, size, 0, [])
    print(f"#{t+1} {price}")
```

```python
def perm(n, k, hap):
    global minV, price, product, N
    if n == k:
        if minV > hap:
            # print(hap, product)
            minV = hap
    else:
        for i in range(n, k):
            product[i], product[n] = product[n], product[i]
            # hap = sum([price[j][product[j]] for j in range(n + 1)])
            temp = hap + price[n][product[n]]
            if temp < minV:
                perm(n + 1, k, temp)
            product[i], product[n] = product[n], product[i]


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    price = [list(map(int, input().split())) for i in range(N)]
    product = list(range(N))
    possiblity = []
    minV = 10000000000000000
    perm(0, N, 0)
    print("#{} {}".format(tc, minV))
```

```python
def per(n, k, total):
    global ans
    if n == k:
        if total < ans:
            ans = total
        return
    elif total > ans:
        return
    else:
        for i in range(k):
            if used[i] == 0:
                temp[n] = table[n][i]
                used[i] = 1
                per(n+1, k, total + table[n][i])
                used[i] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for n in range(N)]
    ans = 300
    used = [0] * N
    temp = [0] * N
    per(0, N, 0)
    print(f"#{t} {ans}")
```

#### 최소 생산 비용 변형

```
3
-24 -3
-59 5
-2 -79
25 -15
-15 71
-99 -92
```

```python
def f(n, k):
    global min_cost
    if n == k:
        s = 0
        for i in range(N):
            s += abs(a[bit[i]-1][0] - b[bit[i]-1][0]) + abs(a[bit[i]-1][1] - b[bit[i]-1][1])
        if min_cost > s:
            min_cost = s
    else:
        for i in range(n, k):
            bit[i], bit[n] = bit[n], bit[i]
            f(n+1, k)
            bit[i], bit[n] = bit[n], bit[i]

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
b = [list(map(int, input().split())) for _ in range(N)]
bit = list(range(1, N+1))
min_cost = 1000000
f(0, N)
print(min_cost)
```

```python
def perm(n, k):
    global minV
    if n == k:
        s = 0
        for i in range(N):
            s += (abs(local[i][0]-factory[p[i]][0]) + abs(local[i][1]-factory[p[i]][1]))
        if s < minV:
            minV = s
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k)
            p[n], p[i] = p[i], p[n]

# N = 3
N = int(input())
# local = [[-24, -3], [-59, 5], [-2, -79]]
local = [list(map(int, input().split())) for _ in range(N)]
# factory = [[25, -15], [-15, 71], [-99, -92]]
factory = [list(map(int, input().split())) for _ in range(N)]
p = [_ for _ in range(N)]
minV = 1000000
perm(0, N)
print(minV)
```

```python
bit = list(range(1, 2*N+1))
min_cost = 10000000
f(0, 2, 2*N)
print(min_cost)
def check(n, k):
	global minV
	if n == k:
		distance=0
		for i in range(N):
			x1 = local[i][0]
			y1 = local[i][1]
			x2 = factory[i][0]
			y2 = factory[i][1]
			distance += abs(x1 - x2) + abs(y1 - y2)
		if minV > distance:
			minV = distance
		return
	else:
		for i in range(k):
			if used[i] != 1:
				res[n] = i
				used[i] = 1
				check(n + 1, k)
				used[i] = 0


N = int(input())
local = [list(map(int, input().split())) for x in range(N)]
factory = [list(map(int, input().split())) for x in range(N)]

res = [0] * N
used = [0] * N
minV = 1000000
check(0, N)
print(minV)
```

```python
def npr(n, k):
    global minval, N
    if n == k:
        compare = 0
        for i in range(N):
           compare +=abs(house[i][0] - fac[p[i] - 1][0]) + abs(house[i][1] - fac[p[i] - 1][1])
        if minval > compare:
            minval = compare
    else:
        for i in range(N):
            if used[i] == 0:
                used[i] = 1
                p[n] = i+1
                npr(n+1, k)
                used[i] = 0

minval = 99999
N = int(input())
coord = [list(map(int, input().split())) for _ in range(N*2)]

house = coord[0:N]
fac = coord[N:]

used = [0]* N
p = [0] * N

npr(0, N)
print(minval)
```

