# výsledek není správný, chybu jsem neodhalila. Pro vzorová data ze zadání program fungoval, tak nevím, kde je chyba.

with open("input_1.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

position = 50
count_zero = 0
for item in lines:
    direction = item[0]
    steps = int(item[1:])
    count_zero += steps // 100
    if steps > 100:
        steps = steps % 100
    if direction == "R":
        if position + steps >= 100:
            count_zero += 1
        position = (position + steps) % 100
    elif direction == "L":
        if steps >= position and position != 0:
            count_zero +=1
            position = (position - steps) % 100
        elif position != 0:
            position -= steps
        else:
            position = 100 - steps
print(count_zero)
