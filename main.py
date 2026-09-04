nilai = int(input("Masukkan nilai ujian matematika: "))

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")

elif nilai >= 75:
    print("Siswa dinyatakan lulus")

else:
    print("Siswa harus mengikuti ujian perbaikan")
