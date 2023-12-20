#Latihan 1

def hitung_pangkat(bilangan, pangkat):
    if pangkat > 10:
        print(f'Berapa {bilangan} ^ {pangkat}?')
        hasil = bilangan * hitung_pangkat(bilangan, pangkat - 4)
        print(f'{bilangan} ^ {pangkat} = {hasil}')
        return hasil
    else:
        return bilangan

bilangan_input = input(input('Masukkan Nilai Bilangan: '))
pangkat_input  = int(input('Masukkan Nilai Pangkat: '))

hasil_pangkat = hitung_pangkat(bilangan_input, pangkat_input)
print(f'Hasil Perpangkatan dari {bilangan_input}**{pangkat_input} = {hasil_pangkat}')

bilangan = 10
pangkat = 4

def hitung_pangkat(bilangan, pangkat):
    if pangkat > 1:
        return bilangan * hitung_pangkat(bilangan, pangkat - 1)
    return bilangan

hasil = hitung_pangkat(bilangan, pangkat)
print(f'Hasil Perpangkatan dari {bilangan}**{pangkat} = {hasil}')
print()

#Laihan 2

def nilai_terbesar(daftar):
    max_value = daftar[0]

    for nilai in daftar:
        if nilai > max_value:
            max_value = nilai

    return max_value

daftar_nilai = [3,20,100,-35,50,5]
print(daftar_nilai)
print('Nilai Terbesar:', nilai_terbesar(daftar_nilai))
print()

def nilai_terbesar_recursive(daftar):
    if len(daftar) == 1:
        return daftar[0]
    else:
        print(f'{daftar} -> {daftar[0]}')
        next_max_value = nilai_terbesar_recursive(daftar[1:])
        print(f'{daftar} -> {next_max_value}')
        return max(daftar[0], next_max_value)

daftar_nilai = [3,20,100,-35,50.5]
print(daftar_nilai)
print('Nilai Terbesar:', nilai_terbesar_recursive(daftar_nilai))
print()

def nilai_terbesar(daftar):
    max_value = daftar[0]

    for nilai in daftar:
        if nilai > max_value:
            max_value = nilai

    return max_value

daftar_nilai = []
for i in range(5):
    nilai = float(input(f'Masukkan Nilai List {i + 1} = '))
    daftar_nilai.append(nilai)

print(daftar_nilai)
print('Nilai Terbesar:', nilai_terbesar(daftar_nilai))
print()

#Latihan 3

nilai = 5

def hitung_faktorial(nilai):
    if nilai > 2:
        return nilai * hitung_faktorial(nilai - 1)
    return 2

faktoria = hitung_faktorial(nilai)
print(f'Nilai Faktorial dari {nilai}! = {faktoria}')
print()

def hitung_faktoria(nilai):
    if nilai > 1:
        return nilai * hitung_faktorial(nilai - 1)
    return 1

nilai_input = int(input('Masukkan Nilai yang akan di faktoria = '))

faktorial = hitung_faktorial(nilai_input)
print(f'Nilai Faktorial dari {nilai_input}! = {faktorial}')
