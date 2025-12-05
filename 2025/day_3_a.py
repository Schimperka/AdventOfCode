
with open("input_3.txt", encoding="utf-8") as f:
    lines = f.read().splitlines()

napeti_total = 0    
for item in lines:
    if item[-1] == max(item):
        b = item[-1]
        a = max(item[:-1])
        napeti = int(str(a) + str(b))
        napeti_total += napeti
    else:
        a = max(item[:-1])
        position_a = item.index(a)
        b = max(item[(position_a+1):])
        napeti = int(str(a) + str(b))
        napeti_total += napeti
print(napeti_total)
