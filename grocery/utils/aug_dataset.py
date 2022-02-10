import pandas as pd
# from random import random, randrange
import random 

products_info = {
    'iPhone' : [700, 6],
    'Xiaomi Mi' : [500, 3],
    'Macbook Slim Laptop' : [1200, 1],
    'Xiaomi Note 8' : [129.99, 8],
    'Xiaomi Note 10' : [179.99, 6]
}
def  generate_name(seed, target = 300):
    name = []
    i = 0
    while i <= target:
        # random_first = randrange(len(seed))
        # first = seed[random_first]
        first = random.choice(seed)

        # random_second = randrange(len(seed))
        # second = seed[random_second]
        second = random.choice(seed)

        if first != second:
            # name.append(first + " " + second)
            name.append({"name": first + " " + second, "sex" : sex})
            i += 1

    return name

def generate_customer():
    name = pd.read_csv("../dataset/common_name.csv")
    # name = name[["Name1", "Name2"]]

    name_m = name["Name1"].tolist()
    name_f = name["Name2"].tolist()

    compiled_name_m = generate_name(seed = name_m, sex = "M")
    compiled_name_f = generate_name(seed = name_f, sex = "F")

    combined_names = compiled_name_m + compiled_name_f
    print(combined_names)

def data_products_info():
    d_grocery = pd.read_csv("../dataset/grocery_data.csv")
    d_grocery = d_grocery.dropna(how="all")
    d_grocery = d_grocery[d_grocery["Order ID"].str.isnumeric()]

    d_grocery["Quantity Ordered"] = pd.to_numeric(d_grocery["Quantity Ordered"])
    d_grocery["Price Each"] = pd.to_numeric(d_grocery["Price Each"])

    d_grocery_weight = pd.DataFrame()

    d_grocery_quantity = d_grocery.groupby(["Product"])[["Quantity Ordered"]].sum().reset_index()
    d_grocery_weight["Product"] = d_grocery_quantity[["Product"]]
    d_grocery_weight["Ratio"] = d_grocery_quantity[["Quantity Ordered"]].apply(lambda x: x/1000)
    d_grocery_weight["Price Each"] = d_grocery.groupby(["Product"])["Price Each"].unique().reset_index()["Price Each"]
    
    grocery_weight = {}
    for index, row in d_grocery_weight.iterrows():
        grocery_weight[row["Product"]] = [row["Price Each"][0], row["Ratio"]]

    print(grocery_weight)

def main():
    augmented_data = []

    len_product = len(products_info)
    products = list(products_info)

    for month in range(1, 13):
        selected_product = randrange(0, len_product)
        print(products[selected_product])

    print(augmented_data)

if __name__ == '__main__':
    data_products_info()