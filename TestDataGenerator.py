import random
import csv

item_num = 100 #Num of data to generate
menu_intems = ['cake', 'pasta', 'rice'] #Menu Items List

with open("input/customer-order.csv", "w") as overwrt:
    #Change Field Names Here
    fields = ["customer_id", "date_of_birth", "item", "quantity", "purchase_date"]
    csv_writer = csv.DictWriter(overwrt, fieldnames=fields)
    csv_writer.writeheader()

    for x in range(item_num):
        cus_id = x+1
        dob = f'{random.randint(1955,2000)}-{random.randint(1,12):02}-{random.randint(1,28):02}'
        item_name = random.choice(menu_intems)
        quantity = random.randint(1,5)
        purchase_date = f'{random.randint(2019,2020)}-{random.randint(1,12):02}-{random.randint(1,28):02}'

        overwrt.write("%d,%s,%s,%d,%s\n" % (cus_id,dob,item_name,quantity,purchase_date))
print('Successfully Generated Random Data')