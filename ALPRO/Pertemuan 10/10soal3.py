tersedia = 0
kamar = [[[False for k in range(20)] for j in range(15)] for i in range(3)]
kamar[1][9][13] = True
kamar[0][4][1] = False
for no_kamar in range(20):
    if not kamar[2][14][no_kamar]:
        tersedia += 1
print(f"Kamar yang tersedia: {tersedia}")