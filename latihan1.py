import random

# Meminta input n dari user
n = int(input("Masukkan nilai N: "))

# Menggunakan for untuk iterasi sebanyak n kali
for i in range(n):
    # Generate random number antara 0 dan 0.5
    random_number = random.random() / 2  # membagi dengan 2 untuk memastikan angka < 0.5
    # Menampilkan output dengan format yang diminta
    print(f"data ke: {i+1} => {random_number}")

print("Selesai")
