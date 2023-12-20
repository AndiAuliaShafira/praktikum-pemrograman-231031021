print('231031021-aulia-tugas\n')

kesempatan = 3
password_benar = 'password123'

while kesempatan > 0:
    username_input = input('masukkan username: ')
    password_input = input('masukkan username: ')

if username_input == 'user123' and password_input == password_bener:
    print(f'Login berhasil!')
else:
    kesempatan -= 1
    print(f'Login gagal. kesempatan tersisa: {kesempatan}')

if kesempatan == 0:
    print('Akun diblokir. Silakan hubungan administrator.')
    exit()
