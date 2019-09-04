def f(n, v, arr):
    for idx in range(0, n):
        if arr[idx] == v:    # 키값을 찾으면 중단
            return idx
    return -1     # 배열 안에 키값이 없으면 -1


# 개수n, 키v
n, v = map(int, input().split())
arr = list(map(int, input().split()))
r = f(n, v, arr)
print(r)
