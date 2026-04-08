# Membuat Struktur Data Dictionary
userLogin = {"name":"sahrul", "age":30, "Role":"Admin"}
print(type(userLogin))

# Mengakses Data
print(f"Nama Akun : {userLogin['name']}")
print(f"Umur Akun : {userLogin['age']} Tahun")
print(f"Role Akun : {userLogin['Role']}")

# Akses data seluruh
print(userLogin.items())
print(userLogin.keys())
print(userLogin.values())

# Menambah Data kedalam dictionary big-O O(1)
userLogin["email"] = "contoh@mail.com"
print(userLogin)

# menghapus data big-O O(1)
userLogin.pop("email")
print(userLogin)

# Mengubah data kedalam dictionary big-O O(1)
userLogin["Role"] = "User"
print(userLogin)

# Nested Dictionary
dbUser= {"user1": {"name":"bejo", "age":30, "Role":"Admin"}, 
"user2": {"name":"rehan", "age":25, "Role":"User"}, 
"user3": {"name":"akhdan", "age":28, "Role":"Guest"}}

print(dbUser)
# Akses value base key
print(dbUser["user1"])

# Melakukan Pencarian data di Dictionary Big-O O(1)
findWord = input("Masukkan Kata yang ingin dicari : ")
if findWord in dbUser:
    print("Data ditemukan")
    print(dbUser[findWord])
else:
    print("Data tidak ditemukan")