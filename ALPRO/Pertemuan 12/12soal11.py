def faktorial(n):
    if n < 0:
        return None
    elif n < 2:
        return 1
    return n * faktorial(n - 1)
n = int(input("Masukkan nilai yang ingin di faktorialkan: "))
print(n, "! = ", faktorial(n))