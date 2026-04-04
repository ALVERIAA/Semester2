a = int(input("masukan nilai matematika : "))
b = int(input("masukan nilai bahasa inggris : "))
c = int(input("masukan nilai iPS : "))

nilai_terbesar = max(a, b, c)
if nilai_terbesar == a:
    print("nilai terbesar adalah matematika", nilai_terbesar)
elif nilai_terbesar == b:
    print("nilai terbesar adalah bahasa inggris", nilai_terbesar)
else:
    print("nilai terbesar adalah iPS", nilai_terbesar)

