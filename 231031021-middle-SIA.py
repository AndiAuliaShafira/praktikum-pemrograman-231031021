''' UTS
1. Buat variabel jenis list berikut.
    
    Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu hasil studi mahasiswa',
            'Nama Lengkap',
            'NIM',
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil',
            'aktif',
            'Tanggal-Bulan-Tahun Lahir']
#(NOTED: sesuaikan dengan data anda)


2. Buat variabel nested list berikut.

MK =   [['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [3,2,3,2,3,3,3,2],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.50,3.00,3.75,4.00,3.75,3.50,3.75,3.00]]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, dan Nilai)

3. Buat Kode dengan hasil runing seperti berikut.


            INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                           JURUSAN SAINS
                    KARTU HASIL STUDI MAHASISWA
                          GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : NIM
Program/Prodi   : S1/Sistem Informasi A
Tahun Masuk     : 2023-Ganjil
Status          : Aktif
|--|--   12   --|--             31            --|-- 7 --|--    13   --|
-----------------------------------------------------------------------
No. Kode        |           Mata Kuliah         |  SKS  | Nilai (0-4) |
-----------------------------------------------------------------------
1   22A1209     | Matkul1                       |   3   |         3.50|
2   22A1210     | Matkul2                       |   2   |         3.00|
3   22A1211     | Matkul3                       |   3   |         3.75|
4   22A1212     | Matkul4                       |   2   |         4.00|
5   22A1213     | Matkul5                       |   3   |         3.75|
6   22A1214     | Matkul6                       |   3   |         3.50|
7   22A1215     | Matkul7                       |   3   |         3.75|
8   22A1216     | Matkul8                       |   2   |         3.00|
-----------------------------------------------------------------------
                                       TOTAL SKS:   21
-----------------------------------------------------------------------
|---------------------------------71-----------------------------------|
Summary:
Jumlah Mata Kuliah : 8 Mata Kuliah
Nilai Tertinggi    : 4.00  (22A1212 - Matkul4)
Nilai Terendah     : 3.00  (22A1211 - Matkul2)
IP Kumulatif       : 3.00
                                   
                                               Parepare, 25 Oktober 2023



                                                 Andi Aulia Shafira      
                                                     ------------
'''



# Tulis Kode Jawaban di bawah!

Kuliah      = 'Institut Teknologi Bacharuddin Jusuf Habibie'
Tanda       = 'Parepare, 25 Oktober 2023'
Jurusan     = 'JURUSAN SAINS'
Kartu       = 'KARTU HASIL STUDI MAHASISWA'
Nama        = 'Andi Aulia Shafira'
NIM         = '231031021'
Program     = 'S1/Sistem Informasi A'
Tahun       = '2023-Ganjil'
Semester    = 'GANJIL 2023/2024'
Status      = 'aktif'
TTL         = '30-Maret-2005'
Total       = 'TOTAL SKS:   20'
nilai_mtk   = [85,89,87,91,90,98,78,90]

MK =   [['Agama Islam','Pancasila','Bahasa Indonesia','Wawasan Cinta INTEK dan IMTAQ','Pengantar pemrograman','Pengantar Teknologi Informasi','Kalkulus Dasar 1','Sains Terpadu'],
        [2,2,2,2,3,3,3,3],
        ['22B0211012','22B0211022','22B0211032','22B0211042','22B0211073','22B0211063','22B0211083','22B0211053'],
        [13.30,09.20,07.30,15.20,07.30,13.30,13.30,13.30]]

sp    = 70
print(Kuliah.upper().center(70))
print(Jurusan.center(70))
print(Kartu.center(70))
print(Semester.center(70))
print()

print(f'''
Nama Lengkap    \t:{Nama.title()}
NIM             \t:{NIM}
Program/Prodi   \t:{Program.title()}
Tahun Masuk     \t:{Tahun}
Status          \t:{Status}
           ''')

print('-'*71)
print('no.'+'|'+'Kode'.ljust(10)+'|'+'Mata Kuliah'.center(30)+'|'+'SKS'.center(5)+'|'+'Hari'.center(8)+'|'+'Jadwal'.center(10)+'|')
print('-'*71)
print('01.'+'|'+'22B0211012'.ljust(10)+'|'+'Agama Islam'.center(30)+'|'+'2'.center(5)+'|'+'Jumat'.center(8)+'|'+'13.30'.center(10)+'|')
print('02.'+'|'+'22B0211022'.ljust(10)+'|'+'Pancasila'.center(30)+'|'+'2'.center(5)+'|'+'Jumat'.center(8)+'|'+'09.20'.center(10)+'|')
print('03.'+'|'+'22B0211032'.ljust(10)+'|'+'Bahasa Indonesia'.center(30)+'|'+'2'.center(5)+'|'+'Kamis'.center(8)+'|'+'07.30'.center(10)+'|')
print('04.'+'|'+'22B0211042'.ljust(10)+'|'+'Wawasan Cinta INTEK dan IMTAQ'.center(30)+'|'+'2'.center(5)+'|'+'Kamis'.center(8)+'|'+'15.20'.center(10)+'|')
print('05.'+'|'+'22B0211073'.ljust(10)+'|'+'Pengantar pemrograman'.center(30)+'|'+'3'.center(5)+'|'+'Selasa'.center(8)+'|'+'07.30'.center(10)+'|')
print('06.'+'|'+'22B0211063'.ljust(10)+'|'+'Pengantar Teknologi Informasi'.center(30)+'|'+'3'.center(5)+'|'+'Kamis'.center(8)+'|'+'13.30'.center(10)+'|')
print('07.'+'|'+'22B0211083'.ljust(10)+'|'+'Kalkulus Dasar 1'.center(30)+'|'+'3'.center(5)+'|'+'Selasa'.center(8)+'|'+'13.30'.center(10)+'|')
print('08.'+'|'+'22B0211053'.ljust(10)+'|'+'Sains Terpadu'.center(30)+'|'+'3'.center(5)+'|'+'Rabu'.center(8)+'|'+'13.30'.center(10)+'|')
print('-'*71)
sp    = 75
print(Total.upper().center(70))
print('-'*71)
print('-'*71)
print()

print('Summary:')
print(f'Jumlah Mata Kuliah : 8 Mata Kuliah')


nilai_tertinggi = max(nilai_mtk)
nilai_terkecil  = min(nilai_mtk)
rata_rata       = sum(nilai_mtk) / len(nilai_mtk)

print('Nilai Tertinggi:',nilai_tertinggi)
print('Nilai Terendah:',nilai_terkecil)
print('IP Kumulatif:',rata_rata)

sp    = 80
print(Tanda.upper().center(80))
print('\n'*3)
print(Nama.upper().center(80))

