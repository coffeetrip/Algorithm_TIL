# arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# n = 3  # row, 줄 수
# m = 4  # column 칸 수
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for i in range(n)]
#
#
# # 가로의 합
# for i in range(n):
#     rk = 0
#     for j in range(m):
#         rk += arr[i][j]
#     print(rk)

# # 세로의 합
# for i in range(m):  # 칸 변경
#     tp = 0
#     for j in range(n):   # 칸 고정, 줄 변경
#         tp += arr[j][i]
#     print(tp)
# a = [1, 2, 3, 4, 5]
# for j in a[1::2]:
#     print(j)

# t = int(input())
# for i in range(t):
#     test = int(input())
#     test_0 = []
#     for t in range(1, test+1):
#         test_0.append(t)
#
#     a_sum = 0
#     for j in test_0[0::2]:
#         a_sum += j
#     b_sum = 0
#     for k in test_0[1::2]:
#         b_sum += k
#     result = a_sum - b_sum
#     print('#{} {}' .format(i+1, result))


t = int(input())
for i in range(t):
    n = int(input())
    result = 0
    for j in range(1, n+1):
        if j % 2:
            result += j
        else:
            result -= j
    print('#{} {}'.format(i + 1, result))