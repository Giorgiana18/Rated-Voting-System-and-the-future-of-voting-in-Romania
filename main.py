import matplotlib.pyplot as plt
import numpy as np

def calcR(lista):
    """Calculează suma valorilor dintr-o listă de numere întregi."""
    return sum(map(int, lista))

def calcT(lista):
    """Calculează distribuția voturilor și returnează rezultatele."""
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
    return [s1, s2, s3]

with open("r.txt", "r") as file:
    tokens = file.read().split()

print("Numărul total de alegători:")
num_votanti = len(tokens) // 3
print(num_votanti)
print()


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


c1, c2, c3 = [], [], []

for idx, el in enumerate(tokens):
    if idx % 3 == 0:
        c1.append(el)
    elif idx % 3 == 1:
        c2.append(el)
    else:
        c3.append(el)

print("Vot Tradițional")
tv = calcT(tokens)
for i, el in enumerate(tv):
    print(f"Candidatul {['Ion', 'Vasile', 'Constantin'][i]} a obținut {el} voturi")
print()

print("Vot prin sistemul Rating")
rv = [calcR(c1), calcR(c2), calcR(c3)]
for i, el in enumerate(rv):
    print(f"Candidatul {['Ion', 'Vasile', 'Constantin'][i]} a obținut {el} puncte")
print()


cand = ["Ion", "Vasile", "Constantin"]  

egalitate_tv = tv.count(max(tv)) > 1
egalitate_rv = rv.count(max(rv)) > 1


if egalitate_tv:
    candidati_egalitate = [cand[i] for i in range(len(tv)) if tv[i] == max(tv)]
    print(f"În momentul actual, candidatul {candidati_egalitate[0]} și candidatul {candidati_egalitate[1]} au obținut un număr egal de voturi în sistemul de votare tradițional, așa că se va organiza turul al doilea de scrutin între cei doi candidați.")

if egalitate_rv:
    candidati_egalitate = [cand[i] for i in range(len(rv)) if rv[i] == max(rv)]
    print(f"În momentul actual, candidatul {candidati_egalitate[0]} și candidatul {candidati_egalitate[1]} au obținut un număr egal de puncte în sistemul de votare cu rating, așa că se va organiza turul al doilea de scrutin între cei doi candidați.")

if not egalitate_tv and not egalitate_rv:
    print("Rezultate finale:")
    print(f"Câștigător prin sistemul de vot tradițional: Candidatul {cand[tv.index(max(tv))]}")
    print(f"Câștigător prin sistemul de vot rating: Candidatul {cand[rv.index(max(rv))]}")


x = np.arange(len(cand))

fig, pt = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("Rezultatele Alegerilor", fontsize=14, fontweight='bold')


colors = ['#ff9999','#66b3ff','#99ff99']

pt[0].bar(x, tv, color=colors, alpha=0.8, edgecolor='black')
pt[0].set_xticks(x)
pt[0].set_xticklabels(cand, fontsize=10)
pt[0].set_title("Vot Tradițional", fontsize=12, fontweight='bold')
pt[0].set_xlabel("Candidați")
pt[0].set_ylabel("Număr de voturi")
pt[0].grid(axis='y', linestyle='--', alpha=0.7)

pt[1].bar(x, rv, color=colors, alpha=0.8, edgecolor='black')
pt[1].set_xticks(x)
pt[1].set_xticklabels(cand, fontsize=10)
pt[1].set_title("Vot cu Rating", fontsize=12, fontweight='bold')
pt[1].set_xlabel("Candidați")
pt[1].set_ylabel("Număr de puncte")
pt[1].grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
