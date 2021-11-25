kalimat_awal = input("Masukkan kalimat awal: ")
kata_sisipan = input("Masukkan kata untuk disisipan: ")
indeks = int(input("Masukkan indeks: ")) - 1
hasil = f"{kalimat_awal[:indeks]}{kata_sisipan}{kalimat_awal[indeks:]}"

print(hasil)
