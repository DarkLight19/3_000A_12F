
lista = []

with open("03_000.txt" , "r", encoding="utf8") as f:
    for i in f:
        lista.append(int(i))

print(f"Hány elemű a sorozat? {len(lista)}")

print("Van e sorozatban negatív szám ? ")

"""
negative = 0
for item in lista:
    if item < 0:
        negative = 1
        break

if negative == 1:
    print("van")
else:
    print("nincs")
"""
i = 0
while(i< len(lista) and not lista[i] < 0):
    i+=1

print("van" if i<len(lista) else "nincs")

print("hany paros szam van a sorozatban? ")

db = 0
for i in lista:
    if i%2 == 0:
        db+=1

print(db)