#1 (kurung kurawal )
import sys

himpunan: set[str] = {"tidak", "bisa", "main", "bola"}
print(himpunan)
print(type(himpunan))
print("ukuran memori: ",  sys.getsizeof(himpunan))

#2 (set())
sambung: set[str] = set(["dan", "lalu", "kemudian"])
print(sambung)
print(type(sambung))
print("ukuran memori: ",  sys.getsizeof(sambung))

#pembuktian terkait tidak memiliki sistem indexing
#print(katasambung[-1])

#menghapus elemen pada set
sambung.remove("kemudian")
print(sambung)
himpunan.discard("tidak")
print(himpunan)

#menambahkan elemen pada set
himpunan.add("mungkin")
print(himpunan)
himpunan.update(["pasti", "mungkin",])
print(himpunan)

#mengubah elemen pada set
himpunan.remove("mungkin")
himpunan.add("mungkin")
print(himpunan)

#operasi pada set
set1: set[int] = {1, 2, 3, 4}
set2: set[int] = {3, 4, 5, 6}

#union(gabungan)
print(set1|set2)
#intersection(irisan)
print(set1&set2)
#difference(selisih)
print(set1-set2)
#symmetric difference(selisih simetris/beda setangkup)
print(set1^set2)
#cartesian product(hasil kali kartesius)
print({(a, b) for a in set1 for b in set2})