num = '444345'
run = 'run'
triplet = 'triplet'
count = 0

# 박스만들기
card = [0] *10
for idx in num:
    card[int(idx)] +=1


# run
for i in range(len(card)-2):
    if card[i] >= 1 and card[i+1] >= 1 and card[i+2] >= 1:
        card[i] -= 1
        card[i+1] -= 1
        card[i+2] -= 1
        count += 1

# triplet
for i in range(len(card)):
    if card[i] >= 3:
        card[i] -= 3
        count += 1

if count >= 2:
    print('baby-gin!')
else:
    print('not baby-gin')