# Načtení dat ze souboru 'extra_paper_input.txt'

with open("extra_paper_input.txt", "r") as file:
    raw_data = file.read().strip()  # Načte obsah a odstraní prázdné řádky na začátku a konci

# Převod dat na seznam seznamů
input_data = [list(map(int, line.split('x'))) for line in raw_data.split('\n')]

# Výstup
print(input_data)
