def Liter100km_ke_mpg(liter):
    mil = 100 * 1000 / 1609.344 # konversi 100 km ke mil
    galon = liter / 3.785411784 # konversi liter ke galon
    return mil / galon

def mpg_ke_Liter100km(mil):
    km100 = mil * 1609.344 / 1000 # konversi mil ke 100 km
    liter = 1 * 3.785411784 # 1 galon ke liter
    return liter / km100

print(Liter100km_ke_mpg(3.9))
print(Liter100km_ke_mpg(7.5))
print(Liter100km_ke_mpg(10.))
print(mpg_ke_Liter100km(60.3))
print(mpg_ke_Liter100km(31.4))
print(mpg_ke_Liter100km(23.5))