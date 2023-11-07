from random import randint

# 1:
lista = ["Table", "Chair", "Shelf", "Sofa"]
print(lista)
print(lista[0:2])

if "Sofa" in lista:
    print("Sofa found.")

# 2:
thrownDiceNumbers = []

for i in range(5):
    random_number = randint(1, 6)
    thrownDiceNumbers.append(random_number)

print(thrownDiceNumbers)

summa = 0
for number in thrownDiceNumbers:
    summa += number

print(f"Summa on: {summa}")

highest_value = 0
for number in thrownDiceNumbers:
    if number > highest_value:
        highest_value = number

print(highest_value)

# 3:
random_number_list = []

while len(random_number_list) < 5:
    random_number = randint(1, 20)
    if random_number not in random_number_list:
        random_number_list.append(random_number)

print(random_number_list)
