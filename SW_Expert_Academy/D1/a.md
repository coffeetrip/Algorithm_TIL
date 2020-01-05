## a

```python
num = int(input())

for i in range(1, num+1):
    a, b = map(int,input().split())
    print(f'#{i} {divmod(a,b)[0]} {divmod(a,b)[1]}')
    
    
```





```python
p, k = map(int, input('').split())
count = 1
while p != k:
    k += 1
    count += 1
print(count)
```





```python
t = int(input())
for i in range(1, t+1):
    test = input()
    
    m1 = ['01', '03', '05', '07', '08', '10', '12']
    m2 = ['04', '06', '09', '11']
    if  (test[4:6] in m1) and 1 <= int(test[6:]) <= 31:
        print(f'#{i} {test[0:4]}/{test[4:6]}/{test[6:8]}')
    elif test[4:6] =='02' and 1 <= int(test[6:]) <= 28:
        print(f'#{i} {test[0:4]}/{test[4:6]}/{test[6:8]}')
    elif (test[4:6] in m2) and 1 <= int(test[6:]) <= 30:
        print(f'#{i} {test[0:4]}/{test[4:6]}/{test[6:8]}')
    else:
        print(f'#{i} -1')
```

```
5
22220228
20150002
01010101
20140230
11111111
```

```
#1 2222/02/28
#2 -1
#3 0101/01/01
#4 -1
#5 1111/11/11
```