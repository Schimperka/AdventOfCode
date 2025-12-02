with open("input_1.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

position = 50 # pozice, kde začínáme
stop = [] # vytvoří seznam všech pozic
for item in lines:
    if item[0] == "L":
        position = (position - int(item[1:])) % 100
        stop.append(position)
    elif item [0] == "R":
        position = (position + int(item[1:])) % 100
        stop.append(position)
zero_count = stop.count(0)
#print(position)
#print(stop[:5])
#print(lines[:5])
print(zero_count)