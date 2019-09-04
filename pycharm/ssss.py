for tc in range(1):
    x = int(input())
    nums = list(map(int, input().split()))
    N = len(nums)

    for y in range(x):
        big = 0
        big_idx = 0
        small = 1000
        small_idx = 0

        for i in range(N):
            if nums[i] >= big:
                big = nums[i]   # 큰값 업데이트
                big_idx = i     # 그 값의 위치
            if nums[i] <= small:
                small = nums[i]
                small_idx = i

        nums[big_idx] = nums[big_idx] - 1
        nums[small_idx] = nums[small_idx] + 1

        for i in range(N):
            if nums[i] >= big:
                big = nums[i]   # 큰값 업데이트
                big_idx = i     # 그 값의 위치
            if nums[i] <= small:
                small = nums[i]
                small_idx = i

        result = big - small
    print(f'#{tc + 1} {result}')