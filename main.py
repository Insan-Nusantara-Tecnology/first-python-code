"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengullang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('Ibu berkata, "Pergi ketoko"')
print('Budi Menjawab, "Baik, apa yang harus saya lakukan di toko"')
print('Ibu Menjawab, "Beli 1 botol susu, dan jika ada telur beli 6 telur"')
print('Maka budi berangkat ketoko')
print('Dan mulai berbelanja')
susu = input('apakah susu ada? ').lower()

if susu == 'ya':
    print('Budi membeli 1 botol susu')

    telur = input('apakah telur ada? ').lower()
    if telur == 'ya':
        print('Budi membeli 6 butir telur')
    else:
        print('Budi membeli 1 botol susu')
else:
    print('Budi tidak membeli apapun')

