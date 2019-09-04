t = int(input())
for tc in range(1, t+1):
    max_move, station, charger = map(int, input().split())
    station_number = [0] + list(map(int, input().split())) + [station]
    # station_number = [0 1 3 7 8 9 10]

    last = station_number[0]
    count = 0
    for i in range(1, len(station_number)):
        if station_number[i] - station_number[i-1] > max_move:
            count = 0
            break
        elif station_number[i] - last > max_move:
            count += 1
            last = station_number[i-1]

    print('#{} {}' .format(tc, count))

