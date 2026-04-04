pendapatan = float(input("Masukkan pendapatan Anda per bulan: "))
if pendapatan <= 60000000 and pendapatan > 0:
    print("pajaknya gol.1 adalah : ", pendapatan * 0.05)
elif pendapatan > 60000000 and pendapatan <= 250000000:
    print("pajaknya gol.2 adalah : ", pendapatan * 0.15)
elif pendapatan > 250000000 and pendapatan <= 500000000:
    print("pajaknya gol.3 adalah : ", pendapatan * 0.25)
elif pendapatan > 500000000:
    print("pajaknya gol.4 adalah : ", pendapatan * 0.30)