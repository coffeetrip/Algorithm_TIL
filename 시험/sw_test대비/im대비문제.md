```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    buy_idx = 0
    for i in range(len(num)):
        if min(num[:-1]) == num[i]:
            buy_idx = i
    sell_num = num[buy_idx+1:]

    big_money = max(sell_num) - num[buy_idx]

    print('#{} {}' .format(tc, big_money))
```

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    
    max_revenue = -100000
    for i in range(N-1):
        for j in range(i+1, N):
            revenue = price[j] - price[i]
            if max_revenue < revenue:
                max_revenue = revenue
    print("#{} {}".format(tc, max_revenue))
```