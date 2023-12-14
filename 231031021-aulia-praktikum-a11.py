#Latihan 4

nilai = 5

def hitung_faktorial(nilai):
    if nilai > 2:
        return nilai * hitung_faktorial(nilai - 1)
    return 2

faktorial = hitung_faktorial(nilai)
print(f'Nilai Faktorial dari {nilai}! = {faktorial}')
print()

def hitung_faktorial(nilai):
    if nilai > 2:
        return nilai * hitung_faktorial(nilai - 1)
    return 2

nilai_input = int(input('Masukkan Nilai yang akan di faktorial = '))

faktorial = hitung_faktorial(nilai_input)
print(f'Nilai Faktorial dari {nilai_input}! = {faktorial}')
print()

#Latihan 5

def faktorial(nilai):
    if nilai <= 1:
        return 1
    else:
        return nilai * faktorial(nilai - 1)
    
for i in range (11):
    print('%2d ! = %d' % (i, faktorial(i)))
print()

def faktorial(nilai):
    if nilai <= 1:
        return 1
    else:
        return nilai * faktorial(nilai - 1)
    
nilai_input = int(input('Masukkan Nilai: '))

for i in range(nilai_input + 1):
    print(f'{i} ! = {faktorial(i)}')
print()

#Latihan 6

def fibonacci(n):
    if n < 0:
        print('Tidak ada bilangan yang bernilai negatif')
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

hasil = fibonacci(20)
print('Fibonacci(%d) = %d' % (20, hasil))
print()

def fibonacci(n):
    if n < 0:
        print('Tidak ada bilangan yang bernilai negatif')
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

nilai_input = int(input('Masukkan sebuah bilangan: '))

hasil = fibonacci(nilai_input)
print(f'Fibonacci({nilai_input}) = {hasil}')
