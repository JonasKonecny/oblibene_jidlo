jidlo = input("Zadej svoje oblibene jidlo: ")

with open("oblibene_veci.txt", "w") as f:
    f.write(jidlo)

print("upraveno")
