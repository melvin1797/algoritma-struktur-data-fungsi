def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print ("Luas segitiga: %f" %luas)

luas_segitiga(4, 6)

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume

sisi = 6
print ("Luas Persegi:", luas_persegi(sisi))
print ("volume Persegi:",  volume_persegi(sisi))



