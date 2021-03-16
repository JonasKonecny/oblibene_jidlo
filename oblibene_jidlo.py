print("Tento projekt je verejne dostupny na githubu")
jidlo = input("Zadej svoje oblibene jidlo: ")
if not jidlo:
        exit()

with open("oblibene_veci.txt", "w") as f:
    f.write(jidlo)
