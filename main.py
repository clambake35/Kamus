"""
meme_dict = {
    "cringe": "Sesuatu yang sangat aneh atau memalukan",
    "lol": "Tanggapan umum terhadap sesuatu yang lucu",
    "rofl": "Tanggapan terhadap lelucon",
    "sheesh": "Sedikit ketidaksetujuan",
    "creepy": "Menakutkan, tidak menyenangkan",
    "aggro": "Untuk menjadi agresif/marah"
}

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ").lower()

if word in meme_dict:
    print(meme_dict[word])
else:
    print("Kata yang dicari tidak ada")
""" 
meme_dict = {
    "cringe": "Sesuatu yang sangat aneh atau memalukan",
    "lol": "Tanggapan umum terhadap sesuatu yang lucu",
    "rofl": "Tanggapan terhadap lelucon",
    "sheesh": "Sedikit ketidaksetujuan",
    "creepy": "Menakutkan, tidak menyenangkan",
    "aggro": "Untuk menjadi agresif/marah"
}

while True:
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ").lower()
    if word == 'n':
        print("Permainan berahkir")
        break
    elif word in meme_dict:
        print(meme_dict[word])
    else:
        print("Kata yang dicari tidak ada")










        
