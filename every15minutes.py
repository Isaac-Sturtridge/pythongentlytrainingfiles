import math


for i in range(1, 96):
    hour = math.floor(i/4)
    if hour == 0:
        hour = 12
    if hour > 12:
        hour -= 12
    minute = (i % 4) * 15
    if minute == 0:
        minute = '00'
    if i < 48:
        print(f'{hour}:{minute} am')
    else:
        print(f'{hour}:{minute} pm')