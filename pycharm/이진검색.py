left = 0
right = n-1  # 개수n
while left <= right:
    # 탐색 구간에 1개의 원소가 남을 때까지
    middle = (left + right)//2
    if find == arr[middle]:
        print('1')
    elif find > arr[middle]:
        # 작은 구간 버림
        left = middle + 1
    elif find < arr[middle]:
        # 큰 구간 버림
        right = middle - 1
# left > right가 1개만 남은 구간에서도 못찾으면
print('-1')