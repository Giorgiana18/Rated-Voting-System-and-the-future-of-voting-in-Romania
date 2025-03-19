def calcR(lista):
    """Calculează suma valorilor dintr-o listă de numere întregi."""
    return sum(map(int, lista))

def calcT(lista):
    """Calculează distribuția voturilor și afișează rezultatele."""
    s1 = s2 = s3 = 0
    for i in range(100):
        z = 3 * i
        if int(lista[z]) == 10:
            s1 += 1
        elif int(lista[z + 1]) == 10:
            s2 += 1
        elif int(lista[z + 2]) == 10:
            s3 += 1
        else:
            print(">>> Eroare: niciun element nu este 10!")
    
    print("Distribuția voturilor:")
    print(f"Prima poziție: {s1}")
    print(f"A doua poziție: {s2}")
    print(f"A treia poziție: {s3}")

with open("r.txt", "r") as file:
    tokens = file.read().split()

print(f"Număr total de valori: {len(tokens)}")
print("Valorile citite:", tokens, "\n")


for i in range(100):
    z = 3 * i
    max_idx = z
    
    if int(tokens[z]) == 10 and int(tokens[z + 1]) == 10:
        tokens[z] = "9"
    if int(tokens[z + 2]) == 10 and int(tokens[z + 1]) == 10:
        tokens[z + 2] = "9"

    if int(tokens[z]) < int(tokens[z + 1]):
        max_idx = z + 1
    if int(tokens[max_idx]) < int(tokens[z + 2]):
        max_idx = z + 2

    tokens[max_idx] = "10"

print("Valorile procesate:", tokens, "\n")


c1, c2, c3 = [], [], []

for idx, el in enumerate(tokens):
    if idx % 3 == 0:
        c1.append(el)
    elif idx % 3 == 1:
        c2.append(el)
    else:
        c3.append(el)


print("Rezultatul votului tradițional:", calcR(c1))
print("Rezultatul votului prin rated diferențe:", calcR(c2))
print("Al treilea set de rezultate:", calcR(c3))


calcT(tokens)
