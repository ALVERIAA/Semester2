def cek_segitiga(a, b, c):
    if a + b <= c:
        return False
    elif b + c <= a:
        return False
    elif a + c <= b:
        return False
    return True
print(cek_segitiga(1, 1, 1))
print(cek_segitiga(1, 1, 3))