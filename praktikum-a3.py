print('praktikum-a3\n')

nama  = 'Andi Aulia Shafira'
nim   = '231031021'
meet  = 'praktikum 3'
prodi = 'Sistem Informasi A'
gmail = 'zaitun.99zt@ith.ac.id'

nama  = 'Andi Aulia Shafira'
nim   = '231031021'
prodi = 'Sistem Informasi A'
ttl   = 'pinrang, 30 maret 2005'
alamat= 'jl. soreang'
asal  = 'pinrang'
hobi  = 'membaca buku cerita'
tinggi= '163'

sp    = 40
print('-'*sp)
print(nama.upper().center(40))
print(nim.center(40))
print('\n'*2)
print(meet.capitalize().rjust(40))
print(prodi.title().rjust(40))
print(gmail.rjust(40))
print('-'*sp)



print(f'Halo, nama saya {nama.title()} dengan NIM {nim} dari Prodi {prodi.title()}, ini adalah file {meet.capitalize()}, Terima kasih.\n')

print(f'''Biodata saya
Nama       \t:{nama.title()}
NIM        \t:{nim}
Prodi      \t:{prodi.title()}
TTL        \t:{ttl}
Alamat     \t:{alamat}
Asal       \t:{asal}
Hobi       \t:{hobi}
Tinggi     \t:{tinggi} cm
           ''')

stat = 'Newton Frankel Issac'
up   = stat.upper()
print(up)
up = up.split() # up menjadi list 3 item
print(up)
print(up[2][0],up[0],up[1]) #N SIR ISSAC
print('F SIR ISSAC NEWTON')

print(up[2],up[0][0],up[1][0])
print('NEWTON S I')

print()

stat2 = '&sir$ @issac# *newton.'
up2  = stat2.upper()
print(up2)
up2  = up2.split()
print(up2)
print(up2[0][1:-1],up2[1][1:-1],up2[2][1:-1])
print(up2[0].strip('&$'),up2[1].strip('@#'),up2[2].strip('*,'))
print('SIR ISSAC NEWTON')

print('Tugas Praktikum 3'.center(40))
nama = 'Andi Aulia Shafira'
nim  = '231031021'
prodi= 'Sistem Informasi A'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi}''')


'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outpunya sesuai'''
print()

str1 = 'duFort Frankel Von Neumann'
a = str1.upper()
b = a.strip('NEUMANN')
c = ('NEUMANN ')
d = c+b
print(d)
#output: NEUMANN DUFORT FRANKEL VON

str2 = 'duFort Frankel Von Neumann'
a = str2.lower()
print(a[0:1]+a[2:3]+a[15:16],a[19:])
#output: dfv neumann

str3 = 'duFort Frankel Von Neumann'
b=str3.upper()
print(b[0:7],b[2:3],b[15:16],b[10:11])
#output: DUFORT F V N

str4 = 'duFOrt Frankel Von Neumann'
c = str4.lower()
d = c.replace('f','F',1)
print(d[19:20].upper(),d[0:6],d[7:8],d[15:16])
#output: N duFort f v

str5 = 'DuFort Frankel Von Neumann'
a = str5.upper()
b = a.strip('NEUMANN')
c = ('NEUMANN ')
d = b.lower()
print(c+ d[0:1],d[2:3],d[15:16])
#output: NEUMANN d f v

str6 = 'duFort Frankel Von Neumann'
a = str6.upper()
b = a.strip('NEUMANN')
c = ('NEUMANN ')
print(c+b[0:1],b[2:3],b[15:16])
#output: NEUMANN DFV

str7 = '@duFort Frankel Von Neumann$'
a=str7.strip('@,$')
b = a.replace('Neumann','NEUMANN')
print(b)
#output: duFort Frankel Von NEUMANN

str8 = '#duFort@Frankel@Von@Neumann$'
a = str8.strip('#,$')
b = a.replace('@',' ')
print(b)
#output: duFort Frankel Von Neumann

str9 = '@duFort@#^Frankel*#(Von(#(Neumann$'
a = str9.replace('@#^',' ').replace('*#(', ' ').replace('(#(',' ').strip('@,$')
print(a)
#output: duFort Frankel Von Neumann

str10 = '@DUFort@!^FraNkel!1(VoN(!(NeuMann^'
a = str10.replace('@!^', ' ').replace('!1(', ' ').replace('(!(', ' ').strip('@,^')
b = a.lower()
c = b.title()
d = c.replace('D','d').replace('f','F')
print(d)
#output: duFort Frankel Von Neumann
print()
