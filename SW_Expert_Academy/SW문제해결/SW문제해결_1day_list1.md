## 4823. min, max

N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

```python
test_number = int(input())
for i in range(test_number):
    num = int(input())
    ai = list(map(int, input().split()))

    ai_min = ai[0]
    ai_max = ai[0]
    for a in range(num):
        if ai[a] > ai_max:
            ai_max = ai[a]
        if ai[a] < ai_min:
            ai_min = ai[a]
    print('#{} {}' .format(i+1, ai_max - ai_min))
```

```python
t = int(input())
for i in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))
    
    for j in range(n-1, 0, -1):
        for k in range(0, j):
            if a[k] > a[k+1]:
                a[k],a[k+1] = a[k+1],a[k]
    result = a[-1] - a[0]
    print('#{} {}' .format(i, result))
```

위에는 min과 max를 구하는 방법

아래는 버블정렬을 이용하여 정렬시킨 후 min, max를 구했다.



## 4831. 전기버스

```python
test_number = int(input())
for tc in range(test_number):
    max_move, station_idx, charger_count = map(int, input().split())
    charger_idx = [0] + list(map(int, input().split())) + [station_idx] 

    last = charger_idx[0]
    result = 0
    for i in range(1, len(charger_idx)):
        # 충전기 사이가 max_move 이상일 때
        if charger_idx[i] - charger_idx[i-1] > max_move:
            result = 0
            break
        # 정류장을 max_move 이상 이동할 때 충전기 들리기
        elif charger_idx[i] - charger_idx[last] > max_move:
            result += 1
            last = i-1

    print('#{} {}' .format(tc+1, result))
```

리스트를 append뿐만 아니라 + 이용하여 추가하는 방법을 배웠다.

last이용하여 이동하는 방법을 배웠다.

```
# 어떻게 해야할까...
1. 방전될 때까지 이동(K)
2. 충전기가 없는 경우 가능한 가장 먼 충전기로 이동

[충전기의 위치를 저장하는 방법 결정] # 어떻게 저장하느냐에 따라 풀이 방법이 전혀 달라진다.
1. 정류장 번호를 인댁스로 한 배열에 충전기 위치만 표시(문제에서 주어진 그대로 저장)
만약, 1, 3, 5, 7, 9에 충전기가 있다면
stop[] = {0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0} 또는 stop[] = {1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0} 

2. 충전기 설치된 정류장 번호로 저장(0번에는 항상 충전할 수 있음)
stop[] = {1, 3, 5, 7, 9} 또는 stop[] = {0, 1, 3, 5, 7, 9}

[방법 1]
stop[] = {0, 1, 3, 5, 7, 9}
stop[i]에 도착할 수 있는지 확인 : stop[1] ~ stop[M]
마지막 충전 위치(last) = (0부터 시작)
stop[i] - stop[last] <= K 를 만족하면 i에 도착 가능

선 이웃한 충전기 사이가 K이내여야 한다.(가장 큰 전제 조건!)

i번째 충전기까지 이동할 수 있는지 확인
stop[i] - stop[last]  <=k
stop[1] - stop[0] = 1 <=3, 가능, i 증가
stop[2] - stop[0] = 3 <=3, 가능, i 증가
stop[3] - stop[0] = 5 <=3, 불가능, last = 2(이전 충전기(i-1)), 충전횟수 1증가

stop[4] - stop[2] = 4 <=3, 불가능, last = 3(이전 충전기(i-1)), 충전횟수 1증가

....
처음부터 종점을 포함해서 도착 가능 여부를 확인하면
stop[] = {0, 1, 3, 5, 7, 9, 10} 마지막 번호에 도착할 수 있는지 확인 할 수 있다.(while?)


[방법 2]
stop[] = {1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0}
    ==> append나 +로 만들 수 있다.
(1) 현재위치 i에서 i+k로 이동
(2) 충전기가 있으면 충전, 현재 위치를 i로 바꾸고 (1)반복
(3) 충전기가 없으면 i+K에서 충전기가 나올때까지 -1까지 이동
    ==> i까지 감소하기 전에 충전기가 나오면 (2)를 실행
    ==> i가 되면 진행 불가(0출력)
```

```python
(1) 정류장 번호를 인덱스로 하는 배열을 만들고, 
입력된 충전기 위치를 표시한다.
(2) 마지막 충전위치 last = 0 (출발지에는 충전기가 있음)
충전횟수 cnt = 0 (출발지 충전은 포함하지 않음)
(3) last + K >= N (마지막 충전위치+운행거리가 종점을 지나면 종료)
따라서 last + K<N 인 동안 충전과 운행을 반복

(4) last+K인 자리 next_stop에 충전기가 있으면
last = last+K  방금 충전한 위치를 마지막 충전위치로 기록하고
cnt += 1 충전횟수 1 증가

(5) last+K인 자리next_stop에 충전기가 없으면
충전기를 찾을 때까지 next_stop 1 감소
- next_stop과 last가 같아지면 운행 불가
- last에 다다르기 전에 next_stop에 충전기가 있으면 
충전기가 있는 위치를 마지막 충전 위치로 기록 last = next_stop
cnt += 1 , (3)부터 반복


T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())  # 최대이동, 정류장수, 충전기수
    charger = list(map(int, input().split()))  # 충전기위치
    stop = [0] *(N+1)

    for i in charger:   # 정류장 번호 배열, 충전기 위치 1로 표시
        stop[i] = 1

    last = 0   # 마지막 충전위치(출발지에는 충전기가 있다.)
    cnt = 0    # 충전횟수
    next_stop = last + K
    while next_stop < N:   # '마지막 충전위치 + 운행거리'가 종점을 지나면 종료
        if stop[next_stop] == 0:   # 충전기가 없으면
            next_stop -= 1         # 충전기를 찾을 때 까지 1 감소
            if next_stop == last:  # 마지막 충전 위치까지 되돌아 오면
                break
        else:   # 충전기가 있으면
            last = next_stop       # 방금 충전한 위치를 마지막 충전 위치로 기록
            next_stop = last + K   # 현재 위치에서 최대로 이동가능한 거리 계산
            cnt += 1

    if next_stop == last:    # 운행 중단인 경우
        print('#{} 0'.format(tc))
    else:   # 종점에 도착한 경우
        print('#{} {}'.format(tc, cnt))
```

```python
(1) 충전기 위치만 저장. 마지막으로 충전한 충전기에서 최대로 이동할 수 있는 충전기(반드시 지나야 하는 정류장)를 찾는 방식 (출발지는 충전기가 있고, 종점은 충전기는 아니지만 종점까지 갈 수 있는지 확인하기 위한 용도)

[0, 1, 3, 5, 7, 9, 10]

(1) stop[i] - stop[i-1] <= K 
(두 충전기 사이 간격이 최대 이동거리 이내여야 함)
만약 stop[i] - stop[i-1] > K 인 상황이면 운행 중단
(2) 마지막 충전 인덱스를 last라 하고,
stop[i] - stop[last] > K 마지막 충전위치에서 갈 수 없는 인덱스i에
다다르면,  이전 충전기에서 충전.(last = i-1, 
(도착할 수 있는 충전기는 통과해서 다음 충전기로 가봄. 도착할 수
없는 충전기면 바로 이전에 통과한 충전기에서 충전)


T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())  # 최대이동, 정류장수, 충전기수
    stop = [0] + list(map(int, input().split())) +[N]   # 충전기위치
    last = 0 # 마지막 충전기 인덱스
    cnt = 0
    result = 1
    for i in range(1, M+2):
        if stop[i]-stop[i-1]>K: # 두 충전기 거리가 K보다 크면 중단
            result = 0
            break
        else:
            if stop[i] - stop[last]>K: # i번 충전기에 도착할 수 없으면
                last = i - 1 # 하나 전 충전기에서 충전하고
                cnt += 1 # 충전횟수 증가
    if result == 0:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, cnt))
```



## 4832. 숫자카드

0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

```python
# 카운팅 정렬 이용
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    card = input()

    card_list = []
    for i in range(len(card)):
        card_list.append(int(card[i]))

    max_card = 0
    for i in range(len(card_list)):
        if max_card < card_list[i]:
            max_card = card_list[i]
    card_idx = [0] * (max_card + 1)

    for i in range(len(card_list)):
        card_idx[card_list[i]] += 1
    max_count = max(card_idx)

    cnt = 0
    max_number = 0
    for i in range(len(card_idx)):
        if card_idx[i] == max_count:
            max_number = i

    print(f'#{tc} {max_number} {max_count}')
```

카운팅정렬을 이용해서 구해보았다.

카운팅 정렬은 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하는 정렬이다.

카운팅 정렬을 하기위해서 집합내의 가장 큰 정수를 알아야 한다.(n이 작을수록 좋다.)

max값보다 한개 더 크게 card_idx를 만들어줘야한다.

인덱스 위치를 정하기 위해서 카드개수를 누적해서 만들어줘야한다.

```python
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num = input()
    
    card = [0] * 10 # 0~9까지 0리스트 만들기
    for i in range(0, n):
        card[int(num[i])] += 1  # 몇장인지
        
    maxidx = 0 
    for i in range(0, 10): # 0~9까지의 카드
        if card[maxidx] <= card[i]:  # 같은값도 바꿔야함
            maxidx = i  # 카드 인덱스
    print('#{} {} {}' .format(tc, maxidx, card[maxidx]))
```

처음에 풀었던 방법이다.

카드가 몇장인지 리스트를 만들고, 가장큰값의 인덱스를 구해서 값과 인덱스를 모두 구한다.

가장 큰 값이기 때문에 <= 기호를 이용했다.



## 4835. 구간합

N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.

M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.  

```python
for tc in range(1, int(input())+1):
    max_s = 0
    min_s = 1000000
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    
    for i in range(0, n-m+1):
        s = 0
        for j in range(i, i+m):
            s += nums[j]
            
        if max_s < s:
            max_s = s
        if min_s > s:
            min_s = s
    print(f'#{tc} {max_s - min_s}')
```

```python
test_number = int(input())
for tc in range(test_number):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))

    m_list = []
    for i in range(0, n-m+1):
        t_sum = 0
        for j in range(i, i+m):
            t_sum += num[j]
        m_list.append(t_sum)

    m_max = m_list[0]
    m_min = m_list[0]
    for k in m_list:
        if k > m_max:
            m_max = k
        if k < m_min:
            m_min = k

    print('#{} {}' .format(tc+1, m_max-m_min))
```



```
1. 길이가 M인 구간의 시작 인덱스 i의 범위

M=3인경우
i : 0 ->   N-3   => i : 0 -> N-M

2. M개를 더하는 구간
j : 0 -> M-1

3. 전체
maxS = 0
minS = 10000 * M # 혹은 1000000
for i : 0 -> N-M
	s = 0
	for j : 0 -> M-1
		s = s + A[ i + j]
	if maxS < s
		maxS = s
	if minS > s
		minS = s
print(maxS - minS)
```



