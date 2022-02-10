from random import random

class User:
    # Class

    def __init__(self, keys: int, nama):
        self.keys = keys
        self.nama = nama
        # Class Constructor

    def pertambahan(self, data):
        result = []
        for i, item in enumerate(data):
            hasil_tambah = item + self.keys
            hasil_kurang = item - self.keys

            result.append({"tambah": hasil_tambah, "kurang": hasil_kurang})
            # print(i, "hasil = ", hasil)

        return result

    def pembagian(self, data):
        
        result = []
        for i, baris in enumerate(data):
            result.append(baris / self.keys)
        return result

    def random_max(self, data):
        result = []
        maxs = 0

        for i, baris in enumerate(data):
            # hit = random() * baris
            result.append(baris)

            if baris > maxs:
                maxs = baris

        print("Nilai maksimum : ", maxs)

        return result


