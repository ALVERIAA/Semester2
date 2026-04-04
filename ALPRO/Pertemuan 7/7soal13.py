exo = []

exo.append("suho")
exo.append("kai")
exo.append("chanyeol")
exo.append("sehun")
print(exo)
for nama in ["DO", "baekhyun", "kris", "lay", "luhan", "tao", "chen"]:
    exo.append(nama)
print(exo)
exo.remove("kris")
exo.remove("luhan")
exo.remove("tao")
print(exo)
exo.insert(-2, "xiumin")
print(exo)
print("Jumlah Member EXO: ", len(exo))