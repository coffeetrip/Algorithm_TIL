# arr = [[4,4,3,2,1],[2,2,1,6,5],[3,5,4,6,7],[4,2,5,9,7],[8,1,9,5,6]]
# print(arr)
# for i in range(5):
#     for j in range(5):
#


# n개의 정수를 입력받아 정수로 리스트에 저장
# n = int(input())
# arr = list(map(int, input().split()))
#
# count = 0  # 짝수의 개수 기록
# for i in range(0, n):  # 탐색 구간(0부터 n개)
#     if not arr[i] % 2:  # 각 숫자에 대해(리스트의 각 원소에 대해)
#         count += 1
# print(count)

# n과 m이 주어진다. n개의 정수가 입력될 때 m보다 큰 수의 개수를 출력하시오.
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# count = 0
# for i in range(0, n):
#     if arr[i] > m:
#         count += 1
# print(count)

n = int(input())
arr = list(map(int, input().split()))

result_list = []
for i in range(1, n):  # 탐색구간 1 : 처리할 원소의 범위
    min_left = arr[0]
    for j in range(0, i):  # ai의 왼쪽 구간에 대해
        if min_left > arr[j]:
            min_left = arr[j]
    result = arr[i] - min_left
    if result < 0:
        result *= -1
    print(result, end=" ")
