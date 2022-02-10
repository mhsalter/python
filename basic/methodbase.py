keys = 10
    
def perkalian(data):
    result = []
    for i, baris in enumerate(data):
        result.append(baris * keys)
    return result

def pembagian(data):
    result = [] 
    for i, baris in enumerate(data):
        result.append(baris / keys)
    return result

def biodata():
    biodata = [
        {"nama": "bagus", "alamat": "depok"},
        {"nama": "mahesa", "alamat": "depok"},
        {"nama": "hafiz", "alamat": "depok"},
        {"nama": "adi", "alamat": "depok"}
    ]

    biodata_list = [
        ["bagus", "depok"],
        ["mahesa", "depok"],
        ["hafiz", "depok"],
        ["adi", "depok"]
    ]

    return biodata, biodata_list


def biodata_list():
    biodata_list = [
        ["bagus", "depok"],
        ["mahesa", "depok"],
        ["hafiz", "depok"],
        ["adi", "depok"]
    ]
    return biodata_list