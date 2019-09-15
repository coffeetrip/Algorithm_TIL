## 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기

```PYTHON
test_number = int(input())
for tc in range(test_number):
    arr = [[0 for i in range(10)] for j in range(10)]
    a = int(input())

    for fn in range(a):
        x1, y1, x2, y2, c = map(int, input().split())

        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                arr[i][j] += c

    count = 0
    for i in range(10):
        count += arr[i].count(3)

    print('#{} {}' .format(tc+1, count))
```

```PYTHON
T = int(input())
for tc in range(1, T + 1):
    pallate = [[0 for i in range(10)] for i in range(10)]
    N = int(input())

    for t in range(N):
        rect = list(map(int, input().split()))
        
        for i in range(rect[0], rect[2]+1):
            for j in range(rect[1], rect[3]+1):
                if pallate[i][j] != rect[4]:
                    pallate[i][j] += rect[4]

    answer = 0
    for i in range(10):
        answer += pallate[i].count(3)
    print('#{0} {1}'.format(tc, answer))
```

처음에는 i, j 이중for문을 만들어서 3의 값을 찾는 코드를 만들어서 풀었는데 한줄씩 배열을 읽어서 카운트함수를 이용해서 원하는 값의 개수를 찾는 방법을 알게되었다.

print문을 이용해서 배열을 출력해보니 내가 생각하는 인덱스 범위가 다른것을 알게되었다.

정답이 나오더라도 확실하게 잘 구현했는지 파악해야겠다.



## 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합

```PYTHON
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    all = []
    for i in range(1, 1 << 12):
        temp = []
        for j in range(12):
            if i & (1 << j):
                temp.append(A[j])
        all.append(temp)

    result = 0
    for i in range(len(all)):
        if len(all[i]) == N and sum(all[i]) == K:
            result += 1
    print("#{} {}".format(tc, result))
```

```PYTHON
for T in range(1, int(input())+1):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    bit = [0]*12
    N, K = map(int, input().split())
    cnt = 0
    for a in range(2):
        bit[0] = a
        for b in range(2):
            bit[1] = b
            for c in range(2):
                bit[2] = c
                for c in range(2):
                    bit[3] = c
                    for d in range(2):
                        bit[4] = d
                        for e in range(2):
                            bit[5] = e
                            for f in range(2):
                                bit[6] = f
                                for g in range(2):
                                    bit[7] = g
                                    for h in range(2):
                                        bit[8] = h
                                        for j in range(2):
                                            bit[9] = j
                                            for k in range(2):
                                                bit[10] = k
                                                for l in range(2):
                                                    bit[11] = l

                                                    sum_bit = 0
                                                    for m in range(12):
                                                        sum_bit += bit[m]*arr[m]
                                                    if sum_bit == K and sum(bit) == N:
                                                        cnt += 1
    print(f'#{T} {cnt}')
```

바로 코드로 다 짜려는것보다 부분부분으로 나눠서 확인한 후 적는습관을 가져야겠다.

왜 안나오지? 그건 다 이유가 있다.



##  4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색 

```python
def search(w):
    l = 1
    r = p
    count = 0
    while l <= r:
        c = (l + r) // 2
        count += 1
        if c > w:
            r = c
        elif c < w:
            l = c
        else:
            return count
    return count


test_number = int(input())
for tc in range(test_number):
    p, a, b = map(int, input().split())

    if search(a) > search(b):
        print('#{} B' .format(tc + 1))
    elif search(a) < search(b):
        print('#{} A'.format(tc + 1))
    else:
        print('#{} 0'.format(tc + 1))
```

처음에 while문 조건을 다르게 주어서 c=(l+r)//2 문장을 두번이나 썼다.

그러나 이진탐색이 l과 r이 만나는 지점이 생기면 나가는 조건으로 바꾸면 중복없이 코드를 작성할 수 있었다.





## 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬

```python
def smin(num, k):
    for i in range(0, len(num)-1):
        min_index = i
        for j in range(i+1, len(num)):
            if num[min_index] > num[j]:
                min_index = j
        num[i], num[min_index] = num[min_index], num[i]
    return num[k//2]

def smax(num, k):
    for i in range(0, len(num)-1):
        max_index = i
        for j in range(i+1, len(num)):
            if num[max_index] < num[j]:
                max_index = j
        num[i], num[max_index] = num[max_index], num[i]
    return num[int(k/2)]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    num = list(map(int, input().split()))

    print(f'#{tc}', end=" ")
    for k in range(10):
        if not k % 2:
            print(smax(num, k), end=" ")
        else:
            print(smin(num, k), end=" ")
    print()
```

이 문제는 선택정렬을 이용해서 풀었다.

선택정렬은 저장되어 있는 자료로부터 k번째로 큰or작은 원소를 찾는 방법이다.

정렬 알고리즘을 이용하여 자료를 정렬한다음에 원하는 순서에 있는 원소를 가져온다.

마지막에 출력을 10개까지 하라는 글을 못보고 무조건 출력해서 fail했다.

항상 글을 잘 읽고 문제를 풀어야겠다.

```PYTHON
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    alist = list(map(int, input().split()))
    special = []
    for i in range(n//2):
        up = max(alist)
        down = min(alist)
        special.append(up)
        special.append(down)
        alist.remove(up)
        alist.remove(down)

    print("#{}".format(tc), end=" ")
    print(*special[:10])
```

```PYTHON
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers = sorted(numbers)
    numbers = [str(number) for number in numbers]

    result = []
    for i in range(10):
        if i % 2:
            result.append(numbers.pop(0))
        else:
            result.append(numbers.pop())
    print('#{} {}'.format(tc, ' '.join(result)))
Collapse
```

```PYTHON
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = sorted(list(map(int, input().split())), reverse=True)
    order = []
    for i in range(len(nums)//2):
        order.append(nums[i])
        order.append(nums[-i-1])
    if N %2 :
        order.append(nums[N//2])

    if len(order) > 10:
        order = order[:10]

    order2 = list(map(str, order))
    print('#{} {}'.format(tc, ' '.join(order2)))
```

```PYTHON
TC = int(input())
for t in range(TC):
    N = int(input()) # 정수 개수
    nums = list(map(int, input().split())) # N개의 정수들
    nums.sort() # 오름차순 정렬 ex) 1 2 3 4 5 ...

    nums_rev = nums[::-1] # 내림차순 정렬 ex) 10 9 8 7 6 5 4 ...

    res = [] # 최종 리스트
    for i in range(5): # 10개만 출력하므로 두 리스트에서 5개씩만 뽑아주면 된다.
        res.append(nums_rev[i]) # 내림차순에서 하나 넣고
        res.append(nums[i])     # 오름차순에서 하나 넣는다.

    print('#{} {}'.format(t+1, " ".join(map(str, res))))
```

```PYTHON
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    SA = sorted(A) # 오름차순 정렬 저장
    SP = [] # 특별한 정렬 저장

    # 특별한 정렬
    for i in range(5):
        SP.append(SA[-1])
        SA.pop()
        SP.append(SA[0])
        SA.pop(0)

    print('#{}'.format(tc), end=' ')
    for i in range(10):
        print(SP[i], end=' ')
    print()
```

```PYTHON
tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    arr = sorted([int(i) for i in input().split()])
    
    result = [0] * 10
    for i in range(0, 10):
        if i % 2 == 0:
            result[i] = str(arr.pop())
        else:
            result[i] = str(arr.pop(0))
    s = ' '.join(result)
    print(f'#{t} {s}')
```

