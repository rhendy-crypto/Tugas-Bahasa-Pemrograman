# Modal awal investasi
modal = 100000000  # 100 juta

# List untuk menyimpan keuntungan per bulan
laba_per_bulan = []

# Perhitungan untuk 8 bulan
for bulan in range(1, 9):
    if bulan <= 2:
        # Bulan 1-2: belum ada keuntungan
        laba = 0
    elif bulan <= 4:
        # Bulan 3-4: keuntungan 1%
        laba = modal * 0.01
    elif bulan <= 7:
        # Bulan 5-7: keuntungan meningkat 5%
        laba = modal * 0.05
    else:  # bulan 8
        # Bulan 8: keuntungan menurun menjadi 2%
        laba = modal * 0.02
    
    # Menampilkan laba per bulan
    print(f"laba bulan ke- {bulan} sebesar: {laba}")
    
    # Menyimpan laba ke dalam list
    laba_per_bulan.append(laba)

# Menghitung dan menampilkan total laba
total_laba = sum(laba_per_bulan)
print(f"Total laba adalah: {total_laba}")
