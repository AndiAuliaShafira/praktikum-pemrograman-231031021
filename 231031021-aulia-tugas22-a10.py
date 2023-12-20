print('231031021-aulia-tugas2\n')

print('TUGAS 2\n')

def tambah_waktu(waktu1, waktuk2):
    total_detik = waktu1 + waktu2
    jam = total_detik // 3600
    sisa_detik = total_detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60
    return jam, menit

jam1 = int(input('Masukkan jam pertama: '))
menit1 = int(input('Masukkan menit pertama: '))

jam2 = int(input('Masukkan jam kedua: '))
menit2 = int(input(',Masukkan Menit kedua: '))

total_jam, total_menit= tambah_waktu((jam * 3600 + menit1 * 60),
                                     (jam2 * 3600 + menit * 60))

print(f'Waktu sekarang menunjukkan pukul {total_jam}:{total_menit}')

def tambah_waktu(waktu1, waktuk2):
    total_detik = waktu1 + waktu2
    jam = selisih_detik // 3600
    sisa_detik = selisih_detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60
    return jam, menit

jam1 = int(input('Masukkan jam pertama: '))
menit1 = int(input('Masukkan menit pertama: '))

jam2 = int(input('Masukkan jam kedua: '))
menit2 = int(input(',Masukkan Menit kedua: '))

selisih_jam, selisih_menit= selisih_waktu((jam1 * 3600 + menit1 * 60),
                                          (jam2 * 3600 + menit2 * 60))

print(f'Waktu sekarang menunjukkan pukul {selisih_jam}:{selisish_menit}')
