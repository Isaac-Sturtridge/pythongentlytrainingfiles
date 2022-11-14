def printHandshakes(people):
    handshakes = 0
    for i in range(0, len(people)):
        for j in range(0, len(people)):
            if i < j:
                print(f'{people[i]} shakes hands with {people[j]}')
                handshakes += 1
    return handshakes



assert printHandshakes(['Alice', 'Bob']) == 1

assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3

assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6