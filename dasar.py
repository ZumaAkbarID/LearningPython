harga = 10000

print('Toko Pensil')
print('')
print('Harga 1 pensil ' + str(harga))
print('')
jumlah_beli = input('Mau berapa pensil?: ')
jumlah = int(jumlah_beli)
total_harga = jumlah * harga
print('Harganya ' + str(total_harga))
uangnya = input('Silahkan bayar: ')
uang = int(uangnya)
if uang > total_harga :
    print('Silahkan ini ' + str(jumlah) + ' pensil Anda')
    print('Kembailan Anda ' + str(uang - total_harga))
    print('Terima Kasih :)')
elif uang == total_harga :
    print('Silahkan ini ' + str(jumlah) + ' pensil Anda')
    print('Uang anda pas, Terima Kasih :)')
else :
    print('Oh, mohon maaf sepertinya uang anda kurang, harga belanja anda ' + str(total_harga))