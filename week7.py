# list_a = [1,2,3]
# print(list_a[0])
# print(list_a[1])
# print(list_a[2])

# tuple_a = 10, 20, 30
# print(tuple_a[0])
# print(tuple_a[1])
# print(tuple_a[2])

# set_b = {15, 16, 17}
# print(set_b[0])
# print(set_b[1])
# print(set_b[2])

# list_a = [1, 2, 3]
# print(f'sebelum : {list_a}')

# list_a[1] = 99

# print(f'sesudah : {list_a}')

# list_a = [1]
# set_a = {1, 39}

# print('[Sebelum]')
# print(f'set \t {set_a}')

# list_a.append(10)
# list_a.append(50)

# set_a.add(50)
# set_a.add(100)

# print('[Sesudah]')
# print(f'list \t {list_a}')
# print(f'set \t {set_a}')

# list_a = [1,2,3,4]
# set_a = {1,2,3,4}

# print('[sebelum]')
# print(f'list \t {list_a}')
# print(f'set \t {set_a}')
# list_a.remove(2)
# list_a.remove(4)
# set_a.remove(2)
# set_a.remove(4)
# print('[sesudah]')
# print(f'list \t {list_a}')
# print(f'set \t {set_a}')
# set_a = {1,2,3}
# for item in set_a:
#     print(item)

artikel = {
    'judul' : 'AA',
    'judul' : 'BB'
}
print(artikel.get('judul'))

# mahasiswa = {
#     'nama' : 'Landis Fabri',
#     'asal' : 'Indonesia'
# }

# print(f'Nama Awal : {mahasiswa.get('nama')}')
# mahasiswa['nama'] = 'Andi Mukhlis'
# print(f'Setelah diubah : {mahasiswa.get('nama')}')

# mahasiswa = {
#     'nama' : 'Landis Fabri',
#     'asal' : 'Indonesia'
# }

# print(f'Hobi : {mahasiswa.get('hobi')}')
# mahasiswa['hobi'] = 'Mancing'
# print(f'hobi dari {mahasiswa.get('nama')} adalah {mahasiswa.get('hobi')}')

# mahasiswa = {
#     'nama' : 'Abdul Wahid',
#     'usia' : 18,
#     'asal' : 'Indonesia'
# }

# del mahasiswa['nama']
# mahasiswa.pop('usia')
# mahasiswa.pop('asal')

# pesan_singkat = {
#     'isi' : 'ISI PESAN INI HANYA BISA DIBACA SEKALI SAJA'
# }
# isi_pesan = pesan_singkat.pop('isi')
# print(f'isi pesan {pesan_singkat.get('isi')}')
# print(f'isi pesan = {isi_pesan}')

# # OPERATOR KEANGGOTAAN
# siswa = {
#     'nama' : 'Renza Ilhami',
# }

# print('Apakah variabel siswa memiliki key nama?')
# print('nama' in siswa)

# print('\n apakah variabel siswa TIDAK memiliki key usia?')
# print('usia' not in siswa)

# sekolah = {
#     'nama' : 'Sekolah Dasar Negri Surabaya 1',
#     'jenjang' : 'Sekolah dasar',
#     'akreditasi' : 'A'
# }
# print(f'Jumlah atribut variabel sekolah adalah ; {len(sekolah)}')