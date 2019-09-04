# SW문제해결_7day_Linked List

### 5108. [파이썬 S/W 문제해결 기본] 7일차 - 숫자 추가

```python
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())  # 수열의 길이, 추가 횟수, 출력할 인덱스 번호
    num = [0] + list(map(int, input().split()))
    for mc in range(M):
        mm = list(map(int, input().split()))
        num.append(0)

        for i in range(len(num)-1, mm[0]+1, -1):
                num[i] = num[i-1]
        num[mm[0]+1] = mm[1]
    print('#{} {}' .format(tc, num[L+1]))
```



### 5110. [파이썬 S/W 문제해결 기본] 7일차 - 수열 합치기

```python
import sys

sys.stdin = open('sample_input.txt','r')
```

```python
T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())  # 수열의 길이, 수열의 개수
    num = list(map(int, input().split()))

    for mc in range(M-1):
        mm = list(map(int, input().split()))

        is_none = True

        for i in range(len(mm)):
            if mm[0] < num[i]:
                num = num[:i] + mm + num[i:]
                is_none = False
                break

        if is_none == True:
            num += mm

    print('#{}' .format(tc), end=" ")
    for j in range(len(num)-1, len(num)-11, -1):
        print(num[j], end=" ")
    print()
```

```python
def split(num_list, result):
    for i in range(len(result)):
        if result[i] > num_list[0]:
            left = result[:i]
            right = result[i:]
            break
    else:
        left = result
        right = []
    
    # result = left + num_list + right
    result = []
    result.extend(left)
    result.extend(num_list)
    result.extend(right)

    return result


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    result = []
    for i in range(M):
        num_list = list(map(int, input().split()))

        result = split(num_list, result)

    result = [str(result[i]) for i in range(len(result)-1, -1, -1) if i >= len(result) - 10]

    print('#{} {}'.format(tc, ' '.join(result)))
```



###  5120. [파이썬 S/W 문제해결 기본] 7일차 - 암호

```python
T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    num = list(map(int, input().split()))

    i = 0
    while K > 0:
        i += M
        if i < len(num):
            num = num[:i] + [num[i-1]+num[i]] + num[i:]

        elif i == len(num):
            num = num[:i] + [num[i-1] + num[0]]

        elif i > len(num):
            i -= len(num)
            num = num[:i] + [num[i - 1] + num[i]] + num[i:]
        K -= 1

    print('#{}' .format(tc), end=" ")
    if len(num) < 11:
        for i in range(len(num)-1, -1, -1):
            print(num[i], end=" ")
        print()
    else:
        for i in range(len(num)-1, len(num)-11, -1):
            print(num[i], end=" ")
        print()
```



### 5122. [파이썬 S/W 문제해결 기본] 7일차 - 수열 편집

```python
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())   # 수열의 길이, 추가 횟수, 출력 인덱스 번호
    num = list(map(int, input().split()))
    for mc in range(M):
        mm = list(input().split())

        if mm[0] == 'I':
            num = num[:int(mm[1])] + [int(mm[2])] + num[int(mm[1]):]

        elif mm[0] == 'D':
            num = num[:int(mm[1])] + num[int(mm[1])+1:]

        elif mm[0] == 'C':
            num[int(mm[1])] = int(mm[2])
    if len(num) < L:
        print('#{} -1' .format(tc))
    else:
        print('#{} {}' .format(tc, num[L]))

```









####  다른사람 코드

숫자추가

```python
t = int(input())
for tc in range(1, t+1):
    N, M, L = map(int, input().split()) # N 수열길이  M 필요한 숫자  L 출력인덱스
    res = list(map(int, input().split()))
    for i in range(M):
        idx, num = map(int, input().split())
        res.insert(idx, num)

    print("#{} {}".format(tc, res[L]))
```

```python
T = int(input())
for tc in range(1, T+1):
    N, M, L = list(map(int, input().split()))
    num_list = list(map(int, input().split()))

    # result = []
    for i in range(M):
        idx, num = map(int, input().split())

        left = num_list[:idx]
        right = num_list[idx:]

        num_list = []
        num_list.extend(left)
        num_list.extend([num])
        num_list.extend(right)
    # print(num_list)

    for i in range(len(num_list)):
        if i == L:
            print('#{} {}'.format(tc, num_list[i]))
```

```python
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):

        node = Node(value)

        if not self.head:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.length += 1

        return self

    def pushleft(self, value):

        if not self.head:
            self.push(value)
        else:
            node = Node(value)

            self.head.prev = node
            node.next = self.head

            self.head = node

            self.length += 1

            return self

    def get(self, index):

        if index < 0 or index >= self.length:
            return None
        else:

            half = self.length // 2

            if index < half:
                current = self.head

                for i in range(self.length):
                    if i == index:
                        break
                    current = current.next

            else:
                current = self.tail

                for i in range(self.length - 1, -1, -1):
                    if i == index:
                        break
                    current = current.prev

            return current

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        else:
            if index == 0:
                self.pushleft(value)
            elif index == self.length - 1:
                self.push(value)
            else:
                node = Node(value)

                prev_node = self.get(index - 1)
                next_node = prev_node.next
                node.prev = prev_node
                node.next = next_node
                prev_node.next = node
                next_node.prev = node

                self.length += 1

                return True

    def get_data(self):
        data = []
        current = self.head
        for i in range(DLL.length):
            data.append(current.value)
            current = current.next
        return data


import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())

    sequence = list(map(int, input().split()))

    DLL = DoublyLinkedList()
    for num in sequence:
        DLL.push(num)

    for _ in range(M):
        index, number = map(int, input().split())
        DLL.insert(index, number)

    print("#{} {}".format(tc, DLL.get(L).value))
```

```python
import sys

sys.stdin = open('add.txt', 'r')


class SList:
    class Node:
        def __init__(self, data, link):
            self.data = data
            self.next = link

    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_front(self, data):
        if self.is_empty():
            self.head = self.Node(data, None)
        else:
            self.head = self.Node(data, self.head)
        self.size += 1

    def insert_after(self, data, p):
        p.next = SList.Node(data, p.next)
        self.size += 1

    def delete_front(self):
        if self.is_empty():
            return
        else:
            self.head = self.head.next
            self.size -= 1

    def delete_after(self, p):
        if self.is_empty():
            return
        t = p.next
        p.next = t.next
        self.size -= 1

    def search(self, target):
        p = self.head
        for k in range(self.size):
            if target == p.data:
                return p
            p = p.next
        return None

    def get_index(self, target):
        p = self.head
        for k in range(target-1):
            p = p.next
        return p

    def get_list(self):
        result = []
        p = self.head
        while p:
            if p.next != None:
                result.append(p.data)
            else:
                result.append(p.data)
            p = p.next
        return result


T = int(input())
for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))
    s = SList()
    for n in nums[::-1]:
        s.insert_front(n)
    for _ in range(M):
        idx, val = map(int, input().split())
        s.insert_after(val, s.get_index(idx))
    last = s.get_list()
    print(last)
    print(last[L])
```



수열합치기

```python
for t in range(int(input())):
    n, m = map(int, input().split())

    res = list(map(int, input().split()))
    for _ in range(m-1):
        arr = list(map(int, input().split()))
        for j in range(len(res)):
            if res[j] > arr[0]:
                res = res[:j] + arr + res[j:]
                break
        else:
            res += arr
    print('#{} {}'.format(t+1, ' '.join(map(str, res[::-1][:10]))))
```

```python
for T in range(int(input())):
    N, M = map(int, input().split())

    res = []
    for i in range(M):
        nums = list(map(int, input().split()))
        num = nums[0]
        if not res:
            res = nums
        else:
            for j in range(len(res)):
                if res[j] > num:
                    res[j:j] = nums
                    break
                elif j == len(res) - 1:
                    res += nums
                    break
    print('#{} {}'.format(T+1, ' '.join(map(str, res[::-1][:10]))))
```



```python
class Node:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.length = 0

        if iterable:
            for value in iterable:
                self.push(value)

    def push(self, value):

        node = Node(value)

        if not self.head:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.length += 1

        return self

    def find(self, node):
        value = node.value
        target_node = self.head

        for i in range(self.length):
            if target_node.value > value:
                return target_node

            target_node = target_node.next

        return None

    def link_sequence(self, DLL):

        target_node = self.find(DLL.head)

        if target_node:
            prev_node = target_node.prev

            # 중간에 삽입 -> 헤드, 테일 변경 없음
            if prev_node:
                prev_node.next = DLL.head
                DLL.head.prev = prev_node
                DLL.tail.next = target_node
                target_node.prev = DLL.tail

            # 맨앞에 삽입 -> 헤드 변경 필요
            else:
                DLL.tail.next = target_node
                target_node.prev = DLL.tail
                self.head = DLL.head

        # 맨 뒤에 삽입 -> 테일 변경 필요
        else:
            self.tail.next = DLL.head
            DLL.head.prev = self.tail
            self.tail = DLL.tail

        self.length += DLL.length

    def get_data(self):
        data = []

        current = self.head
        for _ in range(self.length):
            data.append(current.value)
            current = current.next

        return data

    def get_data_reverse_10(self):
        data = []

        current = self.tail

        for i in range(10):
            data.append(current.value)
            current = current.prev

        return data


# 테스트케이스 전체 통과 => 짧은 리스트는 오히려 더 오래 걸리는 편인데, 길어지면 능력을 발휘하는듯
def process_with_dll(tc, M):
    DLL = DoublyLinkedList(list(map(int, input().split())))

    for _ in range(M - 1):
        next_dll = DoublyLinkedList(list(map(int, input().split())))
        DLL.link_sequence(next_dll)

    print("#{} {}".format(tc, ' '.join(map(str, DLL.get_data_reverse_10()))))

#
# # 테스트케이스 10개 중 9개 통과 (시간초과)
# def process_with_slice(tc, M):
#     seq = list(map(int, input().split()))
#
#     for _ in range(M - 1):
#         next_seq = list(map(int, input().split()))
#
#         value = next_seq[0]
#
#         is_higher_value = False
#         h_idx = 0
#         for i in range(len(seq)):
#             if seq[i] > value:
#                 is_higher_value = True
#                 h_idx = i
#
#                 break
#
#         if is_higher_value:
#             seq = seq[:h_idx] + next_seq + seq[h_idx:]
#         else:
#             seq = seq + next_seq
#
#     data = []
#
#     for j in range(len(seq) - 1, -1, -1):
#         if len(data) == 10:
#             break
#         data.append(seq[j])
#
#     print("{} {}".format(tc, ' '.join(map(str, data))))


import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    process_with_dll(tc, M)
```



암호

```python
T = int(input())
for tc in range(1, T+1):
    n, M, K = list(map(int, input().split()))
    P = list(map(int, input().split()))
    start = 0
    for i in range(K):
        end = start+M
        N = len(P)
        if end < N: # 인덱스가 리스트의 길이보다 작으면
            P.insert(end, P[end-1] + P[end])
        elif end == N:
            P.append(P[0] + P[end-1])
        else: # 인덱스가 리스트 길이를 벗어나면
            end = end-N
            P.insert(end, P[end-1]+P[end])
        start = end

    result = ' '.join(list(map(str, P[-1:-11:-1])))
    print('#{} {}'.format(tc, result))
```



```python
for t in range(int(input())):
    N,M,K = map(int, input().split())
    num = list(map(int, input().split()))
    idx = M
    for i in range(K):
        if idx < len(num):
            num.insert(idx,'1')
            num[idx] = num[idx-1]+num[idx+1]
            idx += M
        elif idx == len(num):
            k = 0
            num.append(num[-1]+num[k])
            idx += M
        else:
            idx = idx - len(num)
            num.insert(idx,'1')
            num[idx] = num[idx-1]+num[idx+1]
            idx += M
    print(f'#{t+1}', end= ' ')
    for f in num[::-1][:10]:
        print(f, end = ' ')
    print()
```



```python
t = int(input())
for tc in range(1, t+1):
    N, M, K = map(int, input().split())
    line = list(map(int, input().split()))
    x = M
    for i in range(K):
        if x == N:
            line.append(line[x % N - 1]+line[x % N ])
        else:
            line.insert(x % N, line[x % N - 1]+line[x % N ])


        print(line, N, x)
        N += 1
        x += M
        if x > N:
            x = x % N
    print("#{}".format(tc),end=" ")
    print(*reversed(line[:]))
```



```python
import sys

sys.stdin = open('sample_input.txt', 'r')


class Node:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.length = 0

        if iterable:
            for value in iterable:
                self.push(value)

    def push(self, value):

        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.length += 1

        return self

    def insert_next_to_n(self, node, n):

        current = node

        for _ in range(n):
            next_node = current.next

            if next_node:
                current = next_node
            else:
                current = self.head

        # 맨 뒤에 추가될때
        if current == self.head:
            # 밀려난 칸이 없으면 시작 숫자(헤드벨류)와 더한다.
            value = self.tail.value + self.head.value
            new_node = Node(value)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        # 중간에 추가될때
        else:
            prev_node = current.prev
            value = prev_node.value + current.value
            new_node = Node(value)

            prev_node.next = new_node
            current.prev = new_node
            new_node.prev = prev_node
            new_node.next = current

        self.length += 1

        return new_node

    def get_data(self):
        data = []
        current = self.tail

        for i in range(self.length):
            if i == 10:
                break
            data.append(current.value)
            current = current.prev

        return data


T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    DLL = DoublyLinkedList(list(map(int, input().split())))

    start = DLL.head
    for _ in range(K):
        next_start = DLL.insert_next_to_n(start, M)
        start = next_start

    print("#{} {}".format(tc, ' '.join(map(str, DLL.get_data()))))
```



수열편집

```python
for t in range(int(input())):
    n, m, l = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(m):
        a = input().split()
        if a[0] == 'I':
            arr.insert(int(a[1]), int(a[2]))
        elif a[0] == 'D':
            del arr[int(a[1])]
        elif a[0] == 'C':
            arr[int(a[1])] = int(a[2])

    if len(arr) < l+1:
        print('#{} {}'.format(t + 1, -1))
    else:
        print('#{} {}'.format(t+1, arr[l]))
```

```python
for tc in range(int(input())):
    N,M,L = map(int, input().split())
    lists = list(map(int, input().split()))
    for i in range(M):
        n = list(input().split())
        if n[0] =='I':
            lists.insert(int(n[1]),int(n[2]))
        elif n[0] == "D":
            lists = lists[:int(n[1])]+lists[int(n[1])+1:]
        elif n[0] == 'C':
            lists[int(n[1])] = int(n[2])
    if L > len(lists):
        print('#{} {}'.format(tc+1, -1))
    else:
        print('#{} {}'.format(tc+1, lists[L]))
```



```python
t = int(input())
for tc in range(1, t+1):
    N, M, L = map(int, input().split())
    getlist = list(map(int, input().split()))
    res = 0
    for i in range(M):
        get = input().split()
        if get[0] == 'I':
            getlist.insert(int(get[1]), int(get[2]))
        elif get[0] == 'D':
            del getlist[int(get[1])]
        elif get[0] == 'C':
            getlist[int(get[1])] = int(get[2])

    if len(getlist) > L:
        print("#{} {}".format(tc, getlist[L]))
    else:
        print("#{} -1".format(tc))
```



```python
import sys

sys.stdin = open('sample_input.txt', 'r')


class Node:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.length = 0

        if iterable:
            for value in iterable:
                self.push(value)

    def push(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
            self.tail = node

        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.length += 1

        return self

    def pushleft(self, value):

        if not self.head:
            self.push(value)
        else:
            node = Node(value)
            node.next = self.head
            self.head.prev = node

            self.head = node

            self.length += 1

            return self

    def pop(self):

        if not self.head:
            return None
        else:
            target_node = self.tail
            self.tail = target_node.prev
            self.tail.next = None

            target_node.prev = None
            self.length -= 1
            return target_node

    def popleft(self):

        if not self.head:
            return None
        else:
            target_node = self.head
            self.head = target_node.next
            self.head.prev = None

            target_node.next = None

            self.length -= 1
            return target_node

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:

            half = self.length // 2

            if index < half:
                current = self.head

                for i in range(self.length):
                    if i == index:
                        break

                    current = current.next

            else:
                current = self.tail

                for i in range(self.length - 1, -1, -1):
                    if i == index:
                        break

                    current = current.prev

            return current

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        else:
            if index == 0:
                self.pushleft(value)
            elif index == self.length - 1:
                self.push(value)
            else:
                new_node = Node(value)
                prev_node = self.get(index - 1)
                next_node = prev_node.next

                new_node.prev = prev_node
                new_node.next = next_node

                prev_node.next = new_node
                next_node.prev = new_node

                self.length += 1

                return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        else:
            if index == 0:
                self.popleft()
            elif index == self.length - 1:
                self.pop()
            else:
                target_node = self.get(index)
                prev_node = target_node.prev
                next_node = target_node.next

                prev_node.next = next_node
                next_node.prev = prev_node

                target_node.prev = None
                target_node.next = None

                self.length -= 1

                return target_node

    def set(self, index, value):
        if index < 0 or index >= self.length:
            return False
        else:
            node = self.get(index)

            node.value = value
            return True


T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())

    DLL = DoublyLinkedList(list(map(int, input().split())))

    for _ in range(M):
        cmds = input().split()

        cmd = cmds[0]

        if cmd == 'I':
            index = int(cmds[1])
            value = int(cmds[2])
            DLL.insert(index, value)

        elif cmd == 'D':
            index = int(cmds[1])
            DLL.remove(index)

        elif cmd == 'C':
            index = int(cmds[1])
            value = int(cmds[2])
            DLL.set(index, value)

    result = -1
    if DLL.get(L):
        result = DLL.get(L).value

    print("#{} {}".format(tc, result))

```

