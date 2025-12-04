with open("input_2.txt", encoding="utf-8") as f:
    text = f.read().strip()

pairs = []

for part in text.split(","):
    if part:                    
        a, b = part.split("-")
        pairs.append([int(a), int(b)])

total = 0
for a, b in pairs:
    for number in range(a, b + 1):         # +1, aby se zahrnulo i 'b'
        s = str(number)
        if len(s) % 2 != 0:
            continue                        # přeskočí čísla s lichým počtem číslic

        half = len(s) // 2
        if s[:half] == s[half:]:
            total += number
print(total)

#print(pairs)