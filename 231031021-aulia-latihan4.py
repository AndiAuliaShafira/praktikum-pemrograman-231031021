print('231031021-aulia-latihan4\n')

pendapatan = int(input('Masukkan besaran pendapatan: '))

if pendapatan <= 1000:
    persentase = 5
elif pendapatan <= 5000:
    persentase = 10
else:
    persentase = 15

bonus = pendapatan * (persentase/100)

total = pendapatan + bonus

print('Pendapatan:', pendapatan)
print('persentase:', str(persentase) + '%')
print('Bonus:', bonus)
print('Jumlah Total:', total)
