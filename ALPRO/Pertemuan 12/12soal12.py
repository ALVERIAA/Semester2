def fibonnaci(n):
    if n < 1:
        return None
    elif n < 3:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)
for i in range(1, 6):
    print(i, "->", fibonnaci(i))