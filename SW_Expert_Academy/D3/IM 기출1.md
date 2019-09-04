# IM 기출1

```python
for tc in range(1, int(input())+1):
    N = int(input())
    room = [0] + list(map(int, input().split()))
    new = [0]*len(room)

    cnt = 0
    for i in range(1, N+1):
        if room[i] != new[i]:
            cnt += 1
            for j in range(i, N+1, i):
                if new[j] == 0:
                    new[j] = 1
                else:
                    new[j] = 0
            #print(new)
    print('#{} {}' .format(tc, cnt))
```

```python
어떤 방에 대한 조작으로 왼쪽의 방은 조작할 수 없다.
꺼진 상태에서 켜는 대신, 최종 상태에서 모두 꺼진 상태를 만들어본다.
왼쪽 부터 오른쪽으로 가면서 켜져있는 스위치만 찾아서 끔

for t in range(1, int(input())+1):
    N = int(input())
    room = [0] + list(map(int, input().split()))
    new_room = [0]*(N+1)

    cnt = 0
    for i in range(1, N+1):   # 켜진 스위치를 확인
        if room[i] != new_room[i]:   # i 번 방이 켜져있으면
            j = 1
            cnt += 1  # i번 방의 스위치를 끈 횟수
            while i*j <= N:   # i의 배수가 존재하는 방 번호일 때
                new_room[i*j] = (new_room[i*j] + 1) % 2  # 스위치 상태 반전
                j += 1
                print(new_room)
    print(cnt)
```

