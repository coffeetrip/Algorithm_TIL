### 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수

```python
T = int(input())
for tc in range(1, T+1):
    N, num = input().split()

    print('#{}' .format(tc), end=" ")
    for i  in range(int(N)):
        if '0' <= num[i] <= '9':
            digit = ord(num[i]) - ord('0')
        elif 'A' <= num[i] <= 'F':
            digit = ord(num[i]) - ord('A') + 10
        for j in range(3, -1, -1):
            if digit & (1 << j) == 0:
                print('0', end="")
            else:
                print('1', end="")
    print()
```

```python
arr = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
for t in range(1, int(input())+1):
    n, c = input().split()
    res = ''
    for i in c:
        res += arr[i]
    print('#{} {}'.format(t, res))
```

```python
t = int(input())
for tc in range(1, t + 1):
    N, num = input().split()
    res = []
    change = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for i in range(int(N)):
        if num[i].isdigit():
            temp = int(num[i])
            res.append(str(bin(temp)))
        else:
            temp = change[num[i]]
            res.append(str(bin(temp)))
    # print(res)
    for j in range(int(N)):
        diff = 4 - len(res[j][2:])
        res[j] = res[j][2:]
        if diff > 0:
            for k in range(diff):
                res[j] = '0' + res[j]
    # print(res)
    print('#{} {}'.format(tc, ''.join(res)))
```

```python
import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    data = input().split()

    total_binary = ''

    for char in data[1]:
        binary = bin(int(char, 16)).replace('0b', '')
        total_binary += binary.zfill(4)

    print("#{} {}".format(tc, total_binary))
```





### 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2

```python
T = int(input())
for tc in range(1, T+1):
    num = float(input())

    s = ''
    while num != 0:
        num = num*2
        if num >= 1:
            s += '1'
            num -= 1
        else:
            s += '0'

        if len(s) >= 13:
            s = 'overflow'
            break
    print('#{} {}' .format(tc, s))
```

```python
def f(n, res, c):
    global arr, arr2
    if res > n:
        return
    if res <= n:
        arr2.add(res)
    if res == n:
        print('#{} {}'.format(t, c))
        return c
    else:
        for i in range(len(arr)):
            if not check[i]:
                check[i] = True
                f(n, res+arr[i], c+'1')
                check[i] = False
                check[i] = True
                f(n, res, c+'0')

arr = []
for i in range(1, 13):
    arr.append(2**(-i))

for t in range(1,int(input())+1):
    check = [False] * len(arr)
    n = float(input())
    arr2 = set()
    f(n, 0,'')
    if n not in arr2:
        print('#{} overflow'.format(t))
```

```python
T = int(input())
for tc in range(1, T+1):
    N = input()
    num = float(N)
    res = []
    i = 1
    while num != 0:
        if num*2 >= 1:
            res.append('1')
            num = num * 2 - 1
        else:
            res.append('0')
            num = num * 2
        i += 1
    if len(res) > 12:
        print('#{} overflow'.format(tc))
    else:
        print('#{} {}'.format(tc, "".join(res)))
```

