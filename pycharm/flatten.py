import sys
sys.stdin = open('input_flatten.txt', 'r')



for i in range(10):
    number = int(input())
    height = list(map(int, input().split()))
    while number > 0:
        height.sort()
        height[-1] -= 1
        height[0] += 1
        number -= 1
        result = max(height)-min(height)
        if max(height)-min(height) <= 1:
            break
    print('#{} {}' .format(i+1, result))


# for tc in range(1,11):
#     dump = int(input())
#     box = list(map(int, input().split()))
#     #for i in range(0, dump):
#     while dump > 0:
#         maxidx = 0
#         mindix = 0
#         for i in range(1, 100):
#             if box[maxidx] < box[i]:
#                 maxidx = i
#             if box[minidx] > box[i]:
#                 minidx = i
#             if box[maxidx] -box[minidx] <= 1:
#                 break
#             else:
#                 box[maxidx] = box[maxidx] - 1
#                 box[minidx] = box[minidx] + 1
#         dump = dump -1
#     print()