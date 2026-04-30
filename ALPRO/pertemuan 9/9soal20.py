lotre = [3, 7, 11, 42, 34, 49]
lotreyangditebak = [5, 9, 11, 42, 3, 49]
yangbenar = 0
for i in lotre:
    if i in lotreyangditebak:
        yangbenar += 1
print("Jumlah tebakan yang benar:", yangbenar)