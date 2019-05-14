import sys

def perhitungan(key, data): #Algortima KSA
    S = list(range(256))
    j = 0

    for i in list(range(256)):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]
	#Algoritma PGRA
    j = 0
    y = 0
    out = []

    for char in data:
        j = (j + 1) % 256
        y = (y + S[j]) % 256
        S[j], S[y] = S[y], S[j]
		#Dienkripsikan menjadi unicode
        if version == 2:
            out.append(unichr(ord(char) ^ S[(S[j] + S[y]) % 256]))

    return ''.join(out)

if __name__ == '__main__':
    if sys.version_info.major == 2: #Memunculkan Typenya
        version = 2

    plaintext = 'kriptografi'
    key = 'tugas'

    #Proses Enkripsi
    enkripsi = perhitungan(key, plaintext)
    print('enkripsi: ' + enkripsi)
    print(type(enkripsi))

    #Proses deskripsi
    deskripsi = perhitungan(key, enkripsi)
    print('deskripsi: ' + deskripsi)
    print(type(deskripsi))