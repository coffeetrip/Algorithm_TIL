### 병합정렬

```python
def divide(m):
    if len(m) <= 1:
        return m
    mid = len(m)//2
    left = divide(m[:mid])
    right = divide(m[mid:])
    return merge(left, right)

def merge(left, right):
    global cnt

    if left[-1] > right[-1]:
        cnt += 1

    result = [0] * (len(left) + len(right))
    l, r, i = 0, 0 ,0
    while l < len(left) or r < len(right):
        if l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result[i] = left[l]
                i += 1
                l += 1
            else:
                result[i] = right[r]
                i += 1
                r += 1
        elif l < len(left):
            for k in range(l, len(left)):
                result[i] = left[k]
                i += 1
                l += 1
        elif r < len(right):
            for k in range(r, len(right)):
                result[i] = right[k]
                i += 1
                r += 1
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    cnt = 0
    print('#{} {} {}' .format(tc, divide(a)[N//2], cnt))
```

```python
def merge_sort(m):
    if len(m) == 1:
        return m
    a = len(m)

    left = m[:a//2]
    right = m[a//2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(L, R):
    global c

    result = []
    if L[-1] > R[-1]:
        c += 1
    while len(L) > 0 or len(R) > 0:
        if len(L) > 0 and len(R) > 0:
            if L[0] <= R[0]:
                result.append(L.pop(0))
            else:
                result.append(R.pop(0))
        elif len(L) > 0:
            result.append(L.pop(0))
        elif len(R) > 0:
            result.append(R.pop(0))
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    c = 0
    print('#{} {} {}'.format(tc, merge_sort(a)[N//2], c))
```

```python
def merge(left, right):
    global cnt
    result = [0] * (len(left) + len(right))
    if left[-1] > right[-1]:
        cnt += 1

    left_idx, right_idx = 0, 0
    left_len, right_len = len(left), len(right)
    m = 0
    while left_idx < left_len or right_idx < right_len:
        if left_idx < left_len and right_idx < right_len:
            if left[left_idx] <= right[right_idx]:
                result[m] = left[left_idx]
                left_idx += 1

            else:
                result[m] = right[right_idx]
                right_idx += 1

        elif left_idx < left_len:
            result[m] = left[left_idx]
            left_idx += 1

        elif right_idx < right_len:
            result[m] = right[right_idx]
            right_idx += 1
        m += 1

    return result


def split(li):
    if len(li) == 1:
        return li
    a = len(li) // 2
    left = [0] * a
    if len(li) % 2:
        right = [0] * (a + 1)
    else:
        right = [0] * a
    
    for i in range(a):
        left[i] = li[i]

    for i in range(a, len(li)):
        right[i - a] = li[i]

    left = split(left)
    right = split(right)

    return merge(left, right)


T = int(input()) + 1

for tc in range(1, T):
    N = int(input())

    cnt = 0

    li = split(list(map(int, input().split())))

    print('#{0} {1} {2}'.format(tc, li[N//2], cnt))
```

```python
def fms(base):
    global cnt
    if len(base) == 1:
        return base
    else:
        m = len(base) // 2
        left = base[:m]  # 리스트 왼쪽 절반
        right = base[m:]  # 오른쪽 절반
        left = fms(left)  # 정렬된 리스트 리턴
        right = fms(right)  # 정렬된 리스트 리턴
        idxl = 0
        idxr = 0
        i = 0
        while idxl < len(left) and idxr < len(right):  # 좌 우 리스트에서 비교 대상이 남은 경우
            if left[idxl] < right[idxr]:
                base[i] = left[idxl]
                idxl += 1
            else:
                base[i] = right[idxr]
                idxr += 1
            i += 1
        if left[-1] > right[-1]:  # 왼쪽 마지막 원소가 큰 경우
            cnt += 1
        if idxl < len(left):  # 왼쪽 리스트가 남은 경우
            base[i:] = left[idxl:]

        if idxr < len(right):  # 오른쪽 리스트가 남은 경우
            base[i:] = right[idxr:]
        return base  # 왼쪽 오른쪽을 합쳐 정렬된 리스트 반환


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    A = fms(A)
    print('#{} {} {}'.format(tc, A[N // 2], cnt))
```

```python
import time
start = time.time()

def merge(left, right):
    global cnt
    result = [0]*(len(left) + len(right))
    if left[-1] > right[-1]:
        cnt += 1
    l, r, m = 0, 0, 0
    while len(left) != l or len(right) != r:
        if len(left) != l and len(right) != r:
            if left[l] <= right[r]:
                result[m] = left[l]
                l += 1
                m += 1
            else:
                result[m] = right[r]
                r += 1
                m += 1
        else:
            if len(left) != l:
                result[m] = left[l]
                l += 1
                m += 1
            elif len(right) != r:
                result[m] = right[r]
                r += 1
                m += 1
    return result


def merge_sort(nums):
    if len(nums) == 1:
        return nums
    middle = len(nums) // 2
    left = nums[:middle]
    right = nums [middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    numlist = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(numlist)
    # print(result)
    element = result[N//2]
    print("#{} {} {}".format(tc, element, cnt))

print(time.time() - start)
```

```python
def merge(l, r):
    global cnt

    if l[-1] > r[-1]:
        cnt += 1

    res = [0] * (len(l) + len(r))
    i, j, m = 0, 0, 0
    while True:
        if i <= len(l) - 1 and j <= len(r) - 1:
            if l[i] <= r[j]:
                res[m] = l[i]
                i += 1
            else:
                res[m] = r[j]
                j += 1
        elif i <= len(l) - 1:
            res[m] = l[i]
            i += 1
        else:
            res[m] = r[j]
            j += 1

        m += 1
        if i >= len(l) and j >= len(r):
            break

    return res

def merge_sort(lst):

    if len(lst) == 1:
        return lst

    mid = len(lst) // 2
    left, right = lst[:mid], lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

for T in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))

    cnt = 0
    A = merge_sort(A)
    print('#{} {} {}'.format(T + 1, A[N // 2], cnt))
```







### 퀵 정렬

```python
def quicksort(a, l, r):
    global N, res
    if l < r:
        s = partition(a, l, r)
        quicksort(a, l, s-1)
        quicksort(a, s+1, r)

def partition(a, l, r):
    p = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] <= p:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    l, r = 0, N-1
    quicksort(a, l, r)
    
    print('#{} {}' .format(tc, a[N//2]))
```

```python
def solution(sample, start_index, last_index):
    if start_index == last_index:
        return sample
    else:
        i = None
        for index in range(start_index, last_index):
            if i is None:
                if sample[index] > sample[last_index]:
                    i = index
            else:
                if sample[index] <= sample[last_index]:
                    sample[i], sample[index] = sample[index], sample[i]
                    i += 1
        if i is None:
            i = last_index
        else:
            sample[i], sample[last_index] = sample[last_index], sample[i]
        if i > start_index:
            solution(sample, start_index, i - 1)
        if i < last_index:
            solution(sample, i + 1, last_index)


for t in range(int(input())):
    size = int(input())
    sample = list(map(int, input().split()))
    
    solution(sample, 0, len(sample) - 1)
    print("#{} {}".format(t + 1, sample[size // 2]))
```

```python
def quick_sort(nlist, p, x):
    if p > x:
        q = partition(nlist, p, x)
        quick_sort(nlist, q-1, x)
        quick_sort(nlist, p, q+1)

def partition(arr, r, x):
    pivot = arr[r]
    for i in range(x, r):
        if pivot > arr[i]:
            arr[i], arr[x] = arr[x], arr[i]
            x += 1
    arr[x], arr[r] = arr[r], arr[x]
    return x

T = int(input())
for t in range(1, T+1):
    N = int(input())
    ilist = list(map(int, input().split()))

    quick_sort(ilist, len(ilist)-1, 0)
    print(ilist[N//2])
```

```python
def quicksort(l, r):
    global nums, N, res
    if l < r:
        s = partition(l, r)
        if s == N//2:
            res = nums[s]
            return
        quicksort(l, s-1)
        quicksort(s+1, r)


def partition(p, r):
    global nums
    x = nums[r]
    i = p - 1
    for j in range(p, r):
        if nums[j] <= x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i + 1


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    nums = list(map(int, input().split()))
    l, r = 0, N-1
    res = 0
    quicksort(l, r)
    if res != 0:
        print("#{} {}".format(tc, res))
    else:
        print("#{} {}".format(tc, nums[N//2]))


# def partition(l, r):
#     global nums
#     p = nums[l]
#     i, j = l, r
#     while i <= j:
#         while nums[i] <= p:
#             i += 1
#         while nums[j] >= p:
#             j -= 1
#         if i < j:
#             nums[i], nums[j] = nums[j], nums[i]
#
#     nums[l], nums[j] = nums[j], nums[l]
#     return j

```

