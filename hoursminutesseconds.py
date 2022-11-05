def getHoursMinutesSeconds(totalSeconds):
    if totalSeconds == 0:
        return '0s'
    if totalSeconds > 100000000:
        return 'Nope, too big'
    if totalSeconds < 60:
        return str(totalSeconds) + 's'
    hours = 0
    minutes = 0
    seconds = 0
    while totalSeconds >= 3600:
        hours += 1
        totalSeconds -= 3600
    while totalSeconds >= 60:
        minutes += 1
        totalSeconds -= 60
    seconds = totalSeconds
    hms = []
    if hours > 0:
        hms.append(str(hours) + 'h')
    if minutes > 0:
        hms.append(str(minutes) + 'm')
    if seconds > 0:
        hms.append(str(seconds) + 's')
    return ' '.join(hms)



total = int(input("Enter seconds: "))

print(getHoursMinutesSeconds(total))


assert getHoursMinutesSeconds(30) == '30s'

assert getHoursMinutesSeconds(60) == '1m'

assert getHoursMinutesSeconds(90) == '1m 30s'

assert getHoursMinutesSeconds(3600) == '1h'

assert getHoursMinutesSeconds(3601) == '1h 1s'

assert getHoursMinutesSeconds(3661) == '1h 1m 1s'

assert getHoursMinutesSeconds(90042) == '25h 42s'

assert getHoursMinutesSeconds(0) == '0s'
