print('231031021-aulia-praktikum-a6\n')

a = True

while a:
    pilih = input('Pilihan')
    if pilih == 'ya':
        print('Selamat Datang')
    elif pilih == 'tidak':
        print('Sampai Jumpa')
        break
    else:
        print('Pilihan tidak valid. Program terus berjalan.')

 #========PENJELASAN========#
#Programan menggunakan loop 'while' yang akan berjalan selama nilai 'a'' adalah True.
#Menggunakan 'input' untuk meminta pengguna memasukkan pilihan.
#Jika pilihan adalah 'ya' atau 'tidak' program akan mencetak pesan dan kemudian menghentikan loop dengan 'break'.
#Jika pilihan tidak valid, program mencetak pesan dan tetap berjalan.
#Hasil running kode ini akan memberikan pesan "Selamat Datang" jika pilihan adalah 'Ya' "Samapai Jumpa" jika
#Pilihan adalah 'Tidak' dan tetap berjalan jika pilihan tidak valid.
