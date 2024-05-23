import csv
import datetime

modified_product_sales = []

product_data = {
    "P001": ["Wireless Headphones", 100],
    "P002": ["Laptop Backpack", 60],
    "P003": ["Bluetooth Speaker", 50],
    "P004": ["USB Flash Drive", 20],
    "P005": ["Mobile Phone Case", 15],
    "P006": ["Wireless Mouse", 30],
    "P007": ["Laptop Stand", 40],
    "P008": ["HDMI Cable", 15],
    "P009": ["Smartphone", 600],
    "P010": ["External Hard Drive", 100],
}

with open('product_sales.txt', 'r') as file:
    sales = file.readlines()
    header = ['current_date', 'sales_id', 'product_id', 'name', 'price']
    modified_product_sales.append(header)
    sales_id = 1
    todayDate = datetime.date.today().strftime('%m/%d/%Y')

    for sale in sales:
        line = [todayDate, sales_id, sale.strip()] + product_data[sale.strip()]
        modified_product_sales.append(line)
        sales_id += 1

with open('modified_sales.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerows(modified_product_sales)
