bilangan = 10
print(bilangan)

def return_bilangan():
    global bilangan
    bilangan = 20
    return bilangan
print(return_bilangan())
print(bilangan)