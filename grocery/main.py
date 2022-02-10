import pandas as pd

def get_city(address):
    return address.split(',')[1].strip(" ")

def get_state(address):
    return address.split(',')[2].strip(" ")[0:2]

def calculated_quantity(number):
    return number * 1000

def load_dataset(dir: str):
    # load csv file
    d_grocery = pd.read_csv(dir)


    # check if dataset contain nan
    d_nan = d_grocery[d_grocery.isna().any(axis=1)]

    # remove nan from dataset
    d_grocery = d_grocery.dropna(how="all")
    # print(d_grocery)

    d_grocery = d_grocery[d_grocery["Order Date"].str[0:2] != 'Or']

    d_grocery["Quantity Ordered"] = pd.to_numeric(d_grocery["Quantity Ordered"])
    d_grocery["Price Each"] = pd.to_numeric(d_grocery["Price Each"])

    d_grocery["Month"] = d_grocery["Order Date"].str[0:2]
    d_grocery["Time"] = d_grocery["Order Date"].str[9:14]

    d_grocery["City"] = d_grocery["Purchase Address"].apply(lambda x: f"{get_city(x)} {get_state(x)}")

    d_grocery["Hasil Perkalian"] = d_grocery["Quantity Ordered"].apply(lambda x: f"{calculated_quantity(x)}")
    d_grocery["Hasil kali"] = d_grocery["Quantity Ordered"].apply(lambda x: x*1000)
    d_grocery["Total"] = d_grocery["Quantity Ordered"] * d_grocery["Price Each"]

    # print(d_grocery.keys())
    # print(d_grocery.head())
    # print(d_grocery[["City", "Purchase Address"]])
    # print(d_grocery[["Quantity Ordered", "Price Each", "total"]])

    return d_grocery

def main():
    dir_datset = "dataset/grocery_data.csv"
    load_dataset(dir_datset)

if __name__ == "__main__":
    main()