## 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교

```python
for tc in range(int(input())):
    short = input()
    long = input()
    short_n = len(short)
    long_n = len(long)

    result = 0
    for i in range(0, long_n - short_n + 1):
        if long[i:i+short_n] == short:
            result = 1
    print('#{} {}' .format(tc+1, result))
```

고지식한 알고리즘을 이용하였다.

텍스트의 모든 위치에서 패턴 비교하고 한칸씩 이동한다.

```python
for tc in range(int(input())):
    short = input()
    long = input()
    short_idx = 0
    long_idx = 0

    while short_idx < len(short) and long_idx < len(long):
        if long[long_idx] != short[short_idx]:
            long_idx = long_idx - short_idx
            short_idx = -1
        long_idx += 1
        short_idx += 1
    if short_idx == len(short):
        result = 1
    else:
        result = 0

    print('#{} {}' .format(tc+1, result))
```





## 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문

```python
test_number = int(input())
for tc in range(test_number):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]
    arr_new = list(map(list, zip(*arr)))

    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                print(f'#{tc + 1} {arr[i][j:j+M]}')
            if arr_new[i][j:j+M] == arr_new[i][j:j+M][::-1]:
                print(f"#{tc+1} {''.join(arr_new[i][j:j+M])}")
```

zip함수를 이용해서 행열의 위치를 바꾸는 법을 배웠다.

''.join()함수를 이용해서 하나씩 떨어져있는 문자열을 붙여서 표현하는 법을 배웠다.

```python
test_number = int(input())
for tc in range(test_number):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]
    arr_new = list(map(list, zip(*arr)))

    for i in range(N):
        for j in range(N-M+1):
            arr_col = arr[i][j:j+M]
            arr_row = arr_new[i][j:j+M]

            if arr_col == arr_col[::-1]:
                print(f'#{tc+1} {arr_col}')
            if arr_row == arr_row[::-1]:
                print(f"#{tc+1} {''.join(arr_row)}")
```

```python
test_number = int(input())
for tc in range(test_number):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            arr_col = arr[i][j:j+M]
            if arr_col == arr_col[::-1]:
                print('#{} {}'.format(tc + 1, arr_col))

    for i in range(0, N):
        arr_row = ""
        for j in range(0, N):
            arr_row += arr[j][i]
        for k in range(0, N - M + 1):
            row = arr_row[k:k + M]
            if row == row[::-1]:
                print('#{} {}'.format(tc + 1, row))
```

zip함수를 이용하지않고 푸는 방법

```python
def pal(n,m):
    lists = [list(input()) for x in range(n)]
    lists_r = list(zip(*lists))
    for i in range(n):
        for j in range(n-m+1):
            if lists[i][j:m+j] == lists[i][j:m+j][::-1]:
                return "".join(lists[i][j:m+j])
            elif lists_r[i][j:m+j] == lists_r[i][j:m+j][::-1]:
                return "".join(lists_r[i][j:m+j])

for tc in range(int(input())):
    n,m = map(int, input().split())
    print(f"#{tc+1} {pal(n,m)}")
```





## 4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수

```PYTHON
test_number = int(input())
for tc in range(test_number):
    str1 = input()
    str2 = input()

    str1_dict = {}
    for i in str1:
        #if i not in str1:   dict의 key 값은 중복x
        str1_dict[i] = 0

    for j in str2:
        if j in str1_dict:
            str1_dict[j] += 1

    print('#{} {}'.format(tc + 1, max(str1_dict.values())))
```









## 다른사람 코드

### 문자열비교

```python
x = int(input())
for tc in range(1, x+1):
    s1 = input()
    s2 = input()
    N = len(s1)
    M = len(s2)
    total = ''
    for i in range(M-N+1):
        for j in range(N):
            if s2[i+j] != s1[j]:
                total += '0'
                break
            else:
                total += '1'
    if '1'*N in total:
        result = 1
    else:
        result = 0
    
    print(f'#{tc} {result}')
```

### 문자열

```python
T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    max = 0
    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str2[j] == str1[i]:
                cnt += 1
        if max < cnt:
            max = cnt
    print('#{0} {1}'.format(tc,max))
```

```python
T = int(input())
for test_case in range(T):
    s1 = input()
    s2 = input()
    s1_dict = {}
    s2_dict = {}
    li = []
    for i in s1:
        if i in s1_dict:
            s1_dict[i] += 1
        if i not in s1_dict:
            s1_dict[i] = 1
    for i in s2:
        if i in s2_dict:
            s2_dict[i] += 1
        if i not in s2_dict:
            s2_dict[i] = 1
    for key,val in s1_dict.items():
        if key in s2_dict:
            li.append(s2_dict[key])
    li.sort()
    print(f'#{test_case+1} {li[-1]}')
    # print(s1_dict)
    # print(s2_dict)
```

```python
T = int(input())
for tc in range(1, T + 1):
    first = list(input())
    second = list(input())

    number = 0
    numlist = []

    for i in range(0, len(first)):
        for j in range(0, len(second)):
            if first[i] == second[j]:
                number += 1
                numlist.append(number)
        number = 0

    print("#{} {}".format(tc, max(numlist)))
```

