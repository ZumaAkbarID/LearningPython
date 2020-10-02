input_dompet = input('Berapa uang yang Anda bawa?: ')

dompet = int(input_dompet)

print('Toko Buku')
print('\n')
print('=====================')
rak_buku = {'kecil': 2000, 'sedang': 5000, 'besar': 7000}
for buku in rak_buku :
    print('Harga buku ' + buku + ' adalah ' + str(rak_buku[buku]))
    print('------')
    
    input_count = input('Mau berapa buku ukuran ' + buku + '?: ')
    count = int(input_count)
    total_harga = count * rak_buku[buku]

    print('Anda akan membeli ' + str(input_count) + ' buku ukuran ' + buku)
    print('Total harga ' + str(total_harga))

    if dompet >= total_harga :
        print('Anda berhasil membeli ' + str(input_count) + ' buku ukuran ' + buku)
        print('\n')
        dompet -= total_harga
        print('Sekarang uang Anda tersisa ' + str(dompet))
        print('\n')
        if dompet == 0 :
            print('Maaf, uang Anda tidak mencukupi')
            break
    else :
        print('Maaf, uang Anda tidak mencukupi')
        