import pandas as pd

df = pd.read_csv("prices.csv", sep="^", header=None).dropna(how="all", axis=1)
df.columns = [
    "sku", "ean", "car_model","car_years", "body_type", "product_group", "product_class", "product_properties", "german1", "german2", "german3", "dutch1", "dutch2",
    "dutch3", "french1", "french2", "french3", "wholesale", "dealer", "end_user", "mpn", "price_group", "inkoop",
    "nto+kosten", "wholesale2", "dealer2", "end_user2", "ship_cat", "virtueel gewicht", "echt gewicht", "afmetingen",
    "car_make", "car_sub_category", "car_category", "make_nogmaals", "body_en", "body_de", "body_nl", "body_fr", "title_en", "title_de", "title_nl",
    "title_fr", "pic title", "bol", "related_mats"
]
df = df.dropna(subset=["sku"])

product_df = df[["sku", "ean", "product_group", "product_class", "product_properties", "related_mats"]]
car_df = df[["car_model", "car_years", "car_category", "car_sub_category", "car_make",]]
prices_df = df[["wholesale", "dealer", "end_user", "inkoop", "nto+kosten", "wholesale2", "dealer2", "end_user2", "price_group"]]
translations_df = df[["german1", "german2", "german3", "dutch1", "dutch2", "dutch3", "french1", "french2", "french3", "body_en", "body_de", "body_nl", "title_en", "title_de", "title_nl"]]
shipping_df = df[["ship_cat", "virtueel gewicht", "echt gewicht", "afmetingen"]]

product_df["product_properties"] = product_df["product_properties"].str.split(";")


car_df["car_years"] = car_df["car_years"].str.replace(">", "").str.split("-")
# car_df = car_df.drop("car_category", axis=1)
car_df = car_df.drop("car_sub_category", axis=1)
car_df = car_df.drop("car_category", axis=1)

print(df)



