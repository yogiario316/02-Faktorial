import os
import sys
import ctypes
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    try:
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:])
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        sys.exit()
    except Exception as e:
        print(f"Kesalahan: {e}")
        sys.exit()

nama = ["Kalkulator Faktorial", "digunakan untuk mempermudah menghitung faktorial", "by Yogi Ario"]

for i in nama:
    print(i)
print("\n")

print("Faktorial merupakan perkalian berurut dari bilangan yang dimulai dari satu sampai dengan bilangan ke-n. Adapun faktorial dari bilangan n adalah hasil perkalian dari bilangan bulat positif yang sama atau kurang dari n, Faktorial dalam matematika dilambangkan dalam bentuk (n!), dimana (n) merupakan angka yang wajib dihitung. Ciri dari faktorial adalah n selalu bilangan bulat positif.")
print("Metode faktorial memiliki pedoman atau kaidah dalam pengerjaannya. Cara menghitung faktorial dilakukan dengan mengalikan angka yang memiliki nilai di bawah (n) secara berurutan.")
print("Dengan demikian, rumus faktorial dapat ditulis sebagai n!= 1 x 2 x 3 x 4. … x n. Sebagai contoh 5! = 5x4x3x2x1 atau 5! = 1x2x3x4x5 = 120.")
print("\n")

def faktorial(n):
    if n <= 1:
        return 1
    else:
        return n * faktorial(n-1)

while True:
    try:
        input_angka = int(input("Masukkan angka: "))
        hasil = faktorial(input_angka)
        print(f"Hasil faktorial dari {input_angka} adalah {hasil}")
        
        ulang = input("Tekan 1 untuk mengulang program atau tekan sembarang tombol untuk keluar: ")
        if ulang != '1':
            break
    except ValueError:
        print("Input tidak valid. Masukkan angka bulat.")
