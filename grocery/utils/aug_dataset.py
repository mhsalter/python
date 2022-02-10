from math import prod
import sys
import pandas as pd
# from random import random, randrange
import random
from tqdm import tqdm

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

def load_seed_data(dir = "../dataset/grocery_data.csv"):
    d_grocery = pd.read_csv(dir)
    d_grocery = d_grocery.dropna(how="all")
    d_grocery = d_grocery[d_grocery["Order ID"].str.isnumeric()]

    d_grocery["Quantity Ordered"] = pd.to_numeric(d_grocery["Quantity Ordered"])
    d_grocery["Price Each"] = pd.to_numeric(d_grocery["Price Each"])
    d_grocery["Month"] = d_grocery["Order Date"].str[0:2]

    return d_grocery

def data_products_info(data_seed):
    
    d_grocery_weight = pd.DataFrame()

    d_grocery_quantity = data_seed.groupby(["Product"])[["Quantity Ordered"]].sum().reset_index()
    d_grocery_weight["Product"] = d_grocery_quantity[["Product"]]
    d_grocery_weight["Ratio"] = d_grocery_quantity[["Quantity Ordered"]].apply(lambda x: x/1000)
    d_grocery_weight["Price Each"] = data_seed.groupby(["Product"])["Price Each"].unique().reset_index()["Price Each"]
    
    grocery_weight = {}
    for index, row in d_grocery_weight.iterrows():
        grocery_weight[row["Product"]] = [row["Price Each"][0], row["Ratio"]]

    return grocery_weight

def ratio_item_monthly(data_seed):
    d_grocery_monthly = data_seed.groupby(["Month"])[["Quantity Ordered"]].sum().reset_index()
    total_order = d_grocery_monthly["Quantity Ordered"].sum()
    d_grocery_monthly["Ratio"] = d_grocery_monthly["Quantity Ordered"].apply(lambda x: x/total_order)
    
    return d_grocery_monthly

def ratio_product_monthly(data_seed):
    data_seed["Ordered Product"] = 1
    d_grocery_product = data_seed.groupby(["Month", "Order ID"])[["Ordered Product"]].sum().reset_index()
    
    # d_grocery_product = d_grocery_product.groupby(["Month"])[["Ordered Product"]].mean().reset_index()
    d_product_average = round(d_grocery_product.groupby(["Month"])[["Ordered Product"]].mean().reset_index())["Ordered Product"].tolist()
    d_product_max = d_grocery_product.groupby(["Month"]).max()["Ordered Product"].reset_index()["Ordered Product"].tolist()

    return d_product_average, d_product_max

def main(target_augmented_data = 5000):
    # augmented_data = []

    # len_product = len(products_info)
    # products = list(products_info)

    # for month in range(1, 13):
    #     selected_product = randrange(0, len_product)
    #     print(products[selected_product])

    # print(augmented_data)

    data_seed = load_seed_data()

    products = data_products_info(data_seed = data_seed)
    monthly_item_ratio = ratio_item_monthly(data_seed = data_seed)

    monthly_item_ratio["Target Item"] = round(monthly_item_ratio["Ratio"].apply(lambda x: target_augmented_data * x))
    item_ratio = monthly_item_ratio["Target Item"].tolist()

    product_average, product_max = ratio_product_monthly(data_seed = data_seed)

    product_list = [ p for p in products]
    product_weight = [ products[p][1] for p in products]
    
    final_data = []
    for i in tqdm(range(0, 12)):
        order_limiter = 0
        while order_limiter < int(item_ratio[i]):

            selected_ratio = random.randrange(product_average[i], product_max[i])

            for pr in range(int(selected_ratio)):
                product_choice = random.choices(product_list, product_weight)

                final_data.append({"Order ID": order_limiter + 1, "Month": i+1, "Product": product_choice})

            order_limiter += 1

    print(len(final_data))

if __name__ == '__main__':
    main()
