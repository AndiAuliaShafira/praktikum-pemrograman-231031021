print('231031021-aulia-praktikum-a7\n')

max_attempts = 3
password = 's123a'
attempts = 0

while attempts < max_attempts:
    input_password = input('Masukkan Password: ')

    if input_password == password:
        print('Selamat Anda Login!')
        break
    else:
        ettempts += 1
        remaining_attempts = max_attempts - attempts
        print(f'password Salah!\nKesempatan anda tersisa {remaining_attempts} kali')

        if remaining_attempts == 0:
            print('Anda kehabisan kesempatan')
            break

 #========PENJELASAN========#
#Program menggunakan loop 'while' untuk  meminta pengguna memasukkan password.
#jika password benar, program mencetak "selamat anda login!" dan menghentikan loop
#Jika password salah, program mencetak pesan kesalahan dan penampilkan sisa kesempatan.
#Jika sisa kesempatan habis, programan memberikan pesan bahwa pengguna kehabisan kesempatan
