#  Import Class User di Folder basic
from basic.users import User
from basic.model.arithmatics import Arithmetics

#  Import Functions di Folder basic
from basic.methodbase import biodata_list, biodata

def app():
    datas = [
        1, 2, 3, 4, 6, 7, 1, 3, 40, 100, 312, 3125, 64, 21
    ]

    # List
    data_nama = [
        ["adi", "hafiz", "bagus", "mahesa"],
        ["adi", "hafiz", "bagus", "mahesa"]
    ]

    # Tuple
    data_tuple = ("adi", "hafiz", "bagus", "mahesa")

    # Dictionary
    biodata = [
        {"nama": "bagus", "alamat": "depok"},
        {"nama": "mahesa", "alamat": "depok"},
        {"nama": "hafiz", "alamat": "depok"},
        {"nama": "adi", "alamat": "depok"}
    ]

    users = User(keys = 3, nama = "adi")
    result = users.pertambahan(datas)

    random_result = users.random_max(datas)

    
    return result, random_result

if __name__ == '__main__':
    result_pertambahan, result_random = app()
    # result_pertambahan = app()

    
    # for i, hasil in enumerate(result_pertambahan):
    #     print(hasil["kurang"])
        

    bio, bio_list = biodata()    


    # for i, baris in enumerate(bio):
        # print((i + 1), "|", baris["nama"], "|", baris["alamat"])

    #     for key in baris:
    #         print(key, "=", baris[key])

    # bioda = biodata_list()

    # for i, baris in enumerate(bioda):
    #     print((i + 1), "|", baris[0], "|", baris[1])

    for baris in result_random:
        print(baris)

    # for i in range(10):
    #     print(i)    
    # print("terimakasih")