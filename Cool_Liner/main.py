import pandas as pd

df = pd.read_csv('prices.csv', sep="^", names=[
    "sku", "ean", "car_model","car_years", "body_type", "product_group", "product_class", "product_properties", "german1", "german2", "german3", "dutch1", "dutch2",
    "dutch3", "french1", "french2", "french3", "wholesale", "niks6", "dealer", "niks7", "end_user", "niks8", "niks1", "niks2", "mpn", "price_group", "inkoop",
    "nto+kosten", "wholesale2", "dealer2", "end_user2", "ship_cat", "virtueel gewicht", "echt gewicht", "afmetingen", "niks3",
    "car_category", "car_sub_category", "car_category2", "car_make", "body_en", "body_de", "body_nl", "title_en", "title_de", "title_nl",
    "title_fr", "pic title", "niks4", "bol", "niks5", "related mats"
])

product_df = df[["sku", "ean", "product_group", "product_class", "product_properties", "related mats"]]
car_df = df[["car_model", "car_years", "car_category", "car_sub_category", "car_make", "body_en"]]
prices_df = df[["wholesale", "dealer", "end_user", "inkoop", "nto+kosten", "wholesale2", "dealer2", "end_user2", "price_group"]]
translations_df = df[["german1", "german2", "german3", "dutch1", "dutch2", "dutch3", "french1", "french2", "french3", "body_en", "body_de", "body_nl", "title_en", "title_de", "title_nl"]]
shipping_df = df[["ship_cat", "virtueel gewicht", "echt gewicht", "afmetingen"]]

product_df["product_properties"] = product_df["product_properties"].str.split(";")

print(product_df.dropna())