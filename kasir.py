
def garis(jum):
    print('=' * jum)

import datetime

today = datetime.date.today()
kasir = input("Input nama kasir : ")

garis(67)
print('      \t\t\t\t\t\t          Zibran Cell')
print('       \t\t\t\t  Perumahan Bukit CIleungsi Indah Blok A2 NO3, Rt 028 Rw 011, Klapanunggal')
print('  \t\t\t\t Telp. 0895-6357-29348 , zibranovsky.github.io')
print('     \t\t\t\t        MENJUAL BERBAGAI JENIS SMARTPHONE')
garis(67)

print(
    'OPPO K3\nKODE BARANG = 001\nBattre = 3765 mAh\nChipset = Snapdragon 710(10 nm)\n3/32 = Rp.3.300.000\n4/64 = Rp.3.500.000')
garis(67)
print(
    'OPPO RENO Z\nKODE BARANG = 002\nBattre = 3950 mAh\nChipset = Mediatek MT6779\n4/64 = Rp.4.000.000\n6/128 = Rp.4.500.000')
garis(67)
print(
    'OPPO A9X\nKODE BARANG = 003\nBattre = 4020 mAh\nChipset = Mediatek MT6779\n4/64 = Rp.3.800.000\n6/128 = Rp.4.100.000')
garis(67)
print('OPPO A9\nKODE BARANG = 004\nBattre = 5000 mAh\nChipset = Snapdragon 665\n4/64 = Rp.3.800.000')
garis(67)
print(
    'OPPO Find Y\nKODE BARANG = 005\nBattre = 4000 mAh\nChipset = Snapdragon 885\n6/64 = Rp.16.200.000\n8/128 = Rp.16.700.000')
garis(67)
print(
    'OPPO A3S\nKODE BARANG = 006\nBattre = 4230 mAh\nChipset = Snapdragon 450\n2/16 = Rp.2.000.000\n3/32 = Rp.2.200.000')
garis(67)
print(
    'OPPO R20\nKODE BARANG = 007\nBattre = 3400 mAh\nChipset = Snapdragon 670\n2/16 = Rp.2.150.000\n3/32 = Rp.2.350.000')
garis(67)
print(
    'OPPO RENO 5G\nKODE BARANG = 008\nBattre = 4065 mAh\nChipset = Snapdragon 855\n6/128 = Rp.14.200.000\n8/128 = Rp.14.700.000')
garis(67)
print(
    'OPPO RENO\nKODE BARANG = 009\nBattre = 3765 mAh\nChipset = Snapdragon 710\n4/64 = Rp.7.500.000\n6/128 = Rp.8.000.000')
garis(67)
print(
    'OPPO A1K\nKODE BARANG = 010\nBattre = 4000 mAh\nChipset = Mediatek MT6762\n2/16 = Rp.1.600.000\n3/32 = Rp.1.800.000')
garis(67)

nb = []
kd = []
jl = []
hr = []
tt = []
rm = []
jumlah_item = 0
diskon = 0

print('DATA PEMBELI\n')
nama = input('Nama Pembeli :')
nohp = input('No.HP Pembeli :')
almt = input('Masukan Alamat :')
jb = int(input('\nData Pesanan pelanggan :'))

for i in range(jb):
    print('Pembelian ke-' + str(i + 1))
    kd.append(input('Masukan Kode Barang :'))
    jl.append(int(input('Masukan Jumlah Beli :')))
    if kd[i] == '001':
        nb.append('OPPO k3')
        rm.append(input('Masukan RAM :'))
        if rm[i] == '3':
            hr.append(3300000)
        elif rm[i] == '4':
            hr.append(3500000)
        else:
            print('salah')

    elif kd[i] == '002':
        nb.append('OPPO RENO Z')
        rm.append(input('Masukan RAM :'))
        if rm[i] == '4':
            hr.append(4000000)
        elif rm[i] == '6':
            hr.append(4500000)
        else:
            print('salah')

    elif kd[i] == '003':
        nb.append('OPPO A9X')
        rm.append(input('Masukan RAM :'))
        if rm[i] == '4':
            hr.append(3800000)
        elif rm[i] == '6':
            hr.append(4100000)
        else:
            print('salah')

    elif kd[i] == '004':
        nb.append('OPPO A9')
        rm.append(input('Masukan RAM :'))
        if rm[i] == '4':
            hr.append(3800000)
        else:
            print('salah')

    elif kd[i] == '005':
        nb.append('OPPO FIND Y')
        rm.append(input('Masukan RAM :'))
        if rm[i] == '6':
            hr.append(16200000)
        elif rm[i] == '8':
            hr.append(16700000)
        else:
            print('salah')

    elif kd[i] == '006':
        nb.append('OPPO A3S')
        rm.append(input('Masukan RAM :'))
        if rm[i] == '2':
            hr.append(2000000)
        elif rm[i] == '3':
            hr.append(2200000)
        else:
            print('salah')

    elif kd[i] == '007':
        nb.append('OPPO R20')
        rm.append(input('Masukan RAM :'))
        if rm[i] == '2':
            hr.append(2150000)
        elif rm[i] == '3':
            hr.append(2350000)
        else:
            print('salah')

    elif kd[i] == '008':
        nb.append('OPPO 5G')
        rm.append(input('Masukan RAM :'))
        if rm[i] == '6':
            hr.append(14200000)
        elif rm[i] == '8':
            hr.append(14700000)
        else:
            print('salah')

    elif kd[i] == '009':
        nb.append('OPPO RENO')
        rm.append(input('Masukan RAM :'))
        if rm[i] == '4':
            hr.append(7500000)
        elif rm[i] == '6':
            hr.append(8000000)
        else:
            print('salah')


    elif kd[i] == '010':
        nb.append('OPPO A1K')
        rm.append(input('Masukan RAM :'))
        if rm[i] == '2':
            hr.append(1600000)
        elif rm[i] == '3':
            hr.append(1800000)
        else:
            print('salah')

    else:
        print('Kode Salah')

print('\n\n')
garis(67)
print('      \t\t\t      PENJUALAN SMARTPHONE GALAXY CELL')
print('       \t\t\t  Jl.KH.Zainul Arifin 19-19A , Jakarta Pusat')
print('  \t\t   Telp. 021 - 8878639 , galaxycell.co.id/IG:@galaxysell21')
print('     \t\t\t        MENJUAL BERBAGAI JENIS SMARTPHONE')
garis(67)
print('INVOICE PENJUALAN')
print('Tanggal :', today)
print('Kasir   : {}'.format(kasir))
print('\nNAMA PEMBELI    :', nama)
print('NO TELP PEMBELI :', nohp)
print('ALAMAT PEMBELI  :', almt)
print('DETAIL BARANG   :')
# print('\n')
print('-' * 86)
print('KODE BARANG  |  NAMA BARANG  |  RAM  |     HARGA    |  JUMLAH BARANG |     TOTAL')
print('-' * 86)

for i in range(jb):
    jumlah_item = jumlah_item + jl[i]
    tt.append(hr[i] * jl[i])

jumlah_byr = 0
for i in range(jb):
    jumlah_byr = jumlah_byr + tt[i]

if jumlah_item > 2:
    diskon = jumlah_byr * 0.1
else:
    diskon = 0

for i in range(jb):
    print('{:>5}'.format(kd[i]), '{:>19}'.format(nb[i]), '{:>8}'.format(rm[i]),
          '{:>16}'.format('Rp.{:,.0f}'.format(hr[i])), '{:>10}'.format(jl[i]),
          '{:>22}'.format('Rp.{:,.0f}'.format(tt[i])))
print('-' * 86)

print('TOTAL HARGA\t\t\t\t :Rp.{:,.0f}'.format(jumlah_byr))
print('Jumlah barang yg dibeli \t\t : {}'.format(jumlah_item))
print('DISKON    \t \t  \t\t :Rp.{:,.0f}'.format(diskon))
jumlah_byr = jumlah_byr - diskon
print('TOTAL BAYAR \t  \t  \t  \t :Rp.{:,.0f}'.format(jumlah_byr))
bayar = (int(input('PEMBAYARAN \t\t\t\t :Rp.')))
kembalian = bayar - jumlah_byr
print('JUMLAH KEMBALIAN \t\t\t :Rp.{:,.0f}'.format(kembalian))
print('-' * 86)
print('***** DISKON 10% UNTUK SETIAP PEMBELIAN LEBIH DARI 2 ITEM ******')
print('************ TERIMA KASIH **************')