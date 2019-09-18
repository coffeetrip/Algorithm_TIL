### 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 컨테이너 수, 트럭 수
    w = list(map(int, input().split()))  # N개의 컨테이너 무게
    t = list(map(int, input().split()))  # M개의 트럭의 적재용량

    w.sort()
    t.sort()

    idxW = N - 1  # 가장 무거운 화물
    idxT = M - 1  # 가장 큰 트럭
    total = 0
    while idxT >= 0 and idxW >= 0:  # 트럭과 화물 모두 남아있는 동안
        if w[idxW] <= t[idxT]:   # 현재 가장 무거운 화물을 현재 가장 큰 트럭이 옮길 수 있으면
            total += w[idxW]
            idxW -= 1
            idxT -= 1
        else:   # 옮길 수 없으면 해당 컨테이너는 포기하고 다음 컨테이너 선택
            idxW -= 1

    print('#{} {}' .format(tc, total))
```

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 컨테이너 수, 트럭 수
    w = list(map(int, input().split()))  # N개의 컨테이너 무게
    t = list(map(int, input().split()))  # M개의 트럭의 적재용량

    w.sort(reverse=True)
    t.sort(reverse=True)

    total = 0
    j = 0
    m = N
    for i in range(M):
        while len(w) != 0 and j<len(w):
            if t[i] >= w[j]:
                total += w[j]
                w.pop(j)
                j = 0
                break
            else:
                j += 1
    print('#{} {}' .format(tc, total))
```

```python
# 혁준님
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    weights = list(map(int, input().split()))
    truck_weights = list(map(int, input().split()))

    truck_weights.sort()
    weights.sort(reverse=True)
    used = []
    for available in truck_weights:  # 작은 놈들한테 큰거 먼저 준다
        for weight in weights:
            if weight <= available:
                used.append(weight)
                weights.remove(weight)
                break
    print("#{} {}".format(tc, sum(used)))
```

```python
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    tr = list(map(int, input().split()))
    w = sorted(w, reverse=True)
    total = 0
    for i in tr:
        for j in w:
            if i >= j:
                total += j
                w.remove(j)
                break
    print(total)
```

```python
t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers = list(reversed(sorted(containers)))
    trucks = list(reversed(sorted(trucks)))
    move = 0
    for i in range(M):
        for j in range(N):
            if trucks[i] >= containers[j]:
                move += containers[j]
                del containers[j]
                N -= 1
                break
    print("#{} {}".format(tc, move))
```

```python
for t in range(int(input())):
    number_container, number_truck = map(int, input().split())
    weight_containers = sorted(list(map(int, input().split())), reverse=True)
    limit_trucks = sorted(list(map(int, input().split())))
    ans = 0
    for index in range(number_container):
        if len(limit_trucks) == 0:
            break
        else:
            for truck in limit_trucks[::-1]:
                if truck >= weight_containers[index]:
                    limit_trucks.remove(truck)
                    ans += weight_containers[index]
                    break
    print(f"#{t+1} {ans}")
```







### 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크

```python
def f(time):
    global N, cnt
    j = 0
    for i in range(1, N):
        if time[i][0] >= time[j][1]:
            cnt += 1
            j = i
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 신청서
    time = []
    for nc in range(N):
        s, e = map(int, input().split())
        time.append([s, e])

    time.sort(key=lambda x: x[1])
    cnt = 1
    print('#{} {}' .format(tc, f(time)))
```

```python
t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    worklist = []
    for i in range(N):
        start, end = map(int, input().split())
        worklist.append([start, end])
    worklist.sort(key=lambda x: x[1])
    work = 1
    start, end = worklist.pop(0)
    for i in range(N-1):
        nstart, nend = worklist[i]
        if end <= nstart:
            work += 1
            end = nend
    print("#{} {}".format(tc, work))
```

```python
T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    schedules = [tuple(map(int, input().split())) for _ in range(N)]

    schedules.sort(key=lambda x: x[1])  # 종료시간으로 정렬

    result_schedules = [schedules[0]]
    for start, end in schedules[1:]:

        prev_schedule = result_schedules[-1]
        prev_end = prev_schedule[1]

        if start < prev_end <= end:
            pass
        else:
            result_schedules.append((start, end))

    print("#{} {}".format(tc, len(result_schedules)))
```

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 끝나는 시간 기준으로 정렬한다. lambda 사용
    apply = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda s: s[1])
    time_table = []
    cnt = 0
    for i in apply:
        if time_table == []:
            time_table.append(i)
            cnt += 1
        if i[0] >= time_table[-1][1]:
            time_table.append(i)
            cnt += 1
    print('#{} {}'.format(tc, cnt))
```







### 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임

```python
def baby(p, r):
    card_idx = [0]*10
    for i in range(len(p)):
        card_idx[p[i]] += 1

    for i in range(len(card_idx)):
        if card_idx[i] >= 3:
            return r
    for i in range(len(card_idx)-2):
        if card_idx[i] >= 1 and card_idx[i+1] >= 1 and card_idx[i+2] >= 1:
            return r
    return 0

T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))

    p1 = []
    p2 = []
    for i in range(len(card)):
        if i % 2 == 0:
            p1.append(card[i])
            if len(p1) >= 3:
                result = baby(p1, 1)
                if result != 0:
                    break
        else:
            p2.append(card[i])
            if len(p2) >= 3:
                result = baby(p2, 2)
                if result != 0:
                    break
    print('#{} {}' .format(tc, result))
```

```python
def check(nums):
    for i in range(8):
        if nums[i] != 0 and nums[i+1] != 0 and nums[i+2] != 0:
            return True
        elif nums[i] >= 3:
            return True
    if nums[8] >=3 or nums[9] >= 3:
        return True
    return False


t = int(input())
for tc in range(1, t + 1):
    orders = list(map(int, input().split()))
    playerA = [0] * 10
    playerB = [0] * 10
    winner = 0
    for i in range(12):
        if i % 2 == 0:
            playerA[orders[i]] += 1
        else:
            playerB[orders[i]] += 1

        if i >= 5:
            if check(playerA):
                winner = 1
                break
            elif check(playerB):
                winner = 2
                break
    print("#{} {}".format(tc, winner))

```

```python
def is_run(cards):
    return cards.count(3) > 0


def is_triplet(cards):
    for i in range(8):
        if cards[i:i + 3].count(0) == 0:
            return True

    return False


T = int(input())
for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))

    odd_counting = [0] * 10
    even_counting = [0] * 10
    winner = 0
    for i in range(len(numbers)):
        # 카드 분배
        if i % 2 == 0:  # 여기선 홀수
            odd_counting[numbers[i]] += 1
            run1 = is_run(odd_counting)
            tri1 = is_triplet(odd_counting)
            
            if run1 or tri1:
                if winner == 0:
                    winner = 1
                    break
        else:
            even_counting[numbers[i]] += 1
            run2 = is_run(even_counting)
            tri2 = is_triplet(even_counting)
            if run2 or tri2:
                if winner == 0:
                    winner = 2
                    break

    print("#{} {}".format(tc, winner))
```

```python
def perm(n, k, p):
    global judge
    if n == k:
        
        if p[0] == p[1] == p[2]:
            judge = 1
        if p[2] == p[1]+1 == p[0]+2:
            judge = 1
    else:
        for i in range(n, k):
            p[n], p[i] = p[i], p[n]
            perm(n+1, k, p)
            p[n], p[i] = p[i], p[n]


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))

    p1 = []
    p2 = []
    judge = 0
    result = 0
    for i in range(12):
        if i % 2 == 0:
            p1.append(card[i])
        else:
            p2.append(card[i])
        if i >= 4:
            if i % 2 == 0:
                perm(0, len(p1), p1)
                if judge == 1:
                    result = 1
                    break
            else:
                perm(0, len(p2), p2)
                if judge == 1:
                    result = 2
                    break
    print('#{} {}'.format(tc, result))
```

