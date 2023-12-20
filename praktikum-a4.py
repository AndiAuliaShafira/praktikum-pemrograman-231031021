print('praktikum-a4\n')

nim   = ('2','3','1','0','3','1','0','2','1')
#nim2  = '231031021'
print(nim[1:3])
#print(nim2[1:3])
print()

#akses item
print(f'item indeks 0: {nim[0]}')
print(f'item indeks 4: {nim[4]}')
print(f'item indeks terakhir: {nim[len(nim)-1]}')
print()

#akses indeks negatif
print(f'item indeks terakhir: {nim[-1]}')
print(f'item indeks pertama: {nim[-len(nim)]}')
print(f'item indeks 6 [-3]: {nim[-3]}')
print(f'item indeks 4 [-5]: {nim[-5]}')
print(f'item indeks 7 [-2]: {nim[-2]}')
print()

#akses indeks batas
print(f'item indeks 1,2,...: \n {nim[1:]}')
print(f'item indeks 3,4,...: \n {nim[3:]}')
print(f'item indeks 0,1,2: \n {nim[:3]}')
print(f'item indeks 0,1,2,3: \n {nim[:4]}')
print(f'item indeks semua: \n {nim[:]}')
print(f'item indeks [:8]: \n {nim[:-1]}')
print(f'item indeks [:6]: \n {nim[:-3]}')
print()

#pengirisan
print(f'item indeks 1,2: \n {nim[1:3]}')
print(f'item indeks 2,3,4: \n {nim[2:5]}')
print(f'item indeks kosong: \n {nim[3:3]}')
print(f'item indeks [8:8] kosong: \n {nim[-1:-1]}')
print(f'item indeks [1:8]: \n {nim[1:-1]}')
print(f'item indeks [2:7]: \n {nim[2:-2]}')
print()

#latihan list
data = [['Andi Aulia Shafira',2023,'Aktif'],
        [90, 89, 93, 97],
        [20, 22],
        ['S1-Reguler','Ganjil']]

print('Nama: ', data[0])
print('Angkatan: ', data[1])
print('Status: ', data[2])
print()

print(f'Andi Aulia Shafira status kuliah:Aktif')
print(f'Data terbesar {data[0][0]} adalah: {max(data[1])}')
print(f'Data terkecil {data[0][0]} adalah: {min(data[1])}')
x_bar = sum(data[1])/len(data[1])
print(f'Rata-Rata Nilai {data[0][0]} adalah: {x_bar}')
print()

#latihan tuple
data = [('Andi Aulia Shafira',2023,'Aktif'),
        (90, 89, 93, 97),
        (20, 22),
        ('S1-Reguler','Ganjil')]

print(data[1])
print(data[-1])
print(data[1][1:-1])
print()

print(f'Jumlah nilai mahasiswa adalah:4')
print(f'Data terbesar {data[0]} adalah: {max(data[1])}')
print(f'Data terkecil {data[0]} adalah: {min(data[1])}')
x_bar = sum(data[1])/len(data[1])
print(f'Rata-Rata Nilai {data[0]} adalah: {x_bar}')
print()

#latihan nested list
data = [('Andi Aulia Shafira',2023,'Aktif'),
        (90, 89, 93, 97),
        (20, 22),
        ('S1-Reguler','Ganjil')]

print(data[0][0])
print(data[-1][0])
print(data[2][0:])
print()

print(f'Program pendidikan {data[0][0]}: {data[-1][0]}')
print(f'Angkatan: {data[0][1]}-{data[-1][1]}')
print(f'Jumlah nilai {data[0][0]} adalah: {len(data[1])}')
print(f'Data terbesar {data[0][0]} adalah: {max(data[1])}')
print(f'Data terkecil {data[0][0]} adalah: {min(data[1])}')
x_bar = sum(data[1])/len(data[1])
print(f'Rata-Rata Nilai {data[0][0]} adalah: {x_bar}')
print()

#tugas

data = [('Andi Aulia Shafira',2023,'Aktif'),
        (90, 89, 93, 97),
        (20, 22),
        ('S1-Reguler','Ganjil')]

matkul = ['matkul1','matkul2','matkul3','matkul4','matkul5','matkul6','matkul7','matkul8']
sks    = [2,2,2,2,3,3,3,3]

data.append(matkul)
data.append(sks)

data[4].append('matkul1')
data[5].append(2)
data[4].append('matkul2')
data[5].append(2)
data[4].append('matkul3')
data[5].append(2)
data[4].append('matkul4')
data[5].append(2)
data[4].append('matkul5')
data[5].append(3)
data[4].append('matkul6')
data[5].append(3)
data[4].append('matkul7')
data[5].append(3)
data[4].append('matkul8')
data[5].append(3)

print(data[0][0])
print(data[-1][0])
print(data[2][0:])

print(f'Program pendidikan {data[0][0]}: {data[-1][0]}')
print(f'Angkatan: {data[0][1]}-{data[-1][1]}')
print(f'Jumlah nilai {data[0][0]} adalah: {len(data[1])}')
print(f'Data terbesar {data[0][0]} adalah: {max(data[1])}')
print(f'Data terkecil {data[0][0]} adalah: {min(data[1])}')
x_bar = sum(data[1])/len(data[1])
print(f'Rata-Rata Nilai {data[0][0]} adalah: {x_bar}')
print()
