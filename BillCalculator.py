import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta

customersBills = {}

with open("input/restaurant-menu.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # Stored restaurant menu's data in python dictionary
    next(csv_reader, None)  # skip the headers
    menu = {rows[0]: rows[1] for rows in csv_reader}

with open("input/customer-order.csv", "r") as csv_file:
    orders = csv.DictReader(csv_file)

    for order in orders:
        # Calculating age
        date_of_birth = datetime.strptime(order["date_of_birth"], "%Y-%m-%d")
        purchase_date = datetime.strptime(order["purchase_date"], "%Y-%m-%d")
        age = relativedelta(purchase_date, date_of_birth).years

        isBirthday = (
            order["date_of_birth"].split("-")[1] == order["purchase_date"].split("-")[1]
        ) and (
            order["date_of_birth"].split("-")[2] == order["purchase_date"].split("-")[2]
        )

        discount = 0

        if age > 60 and isBirthday:
            # 30% discount
            discount = 0.3
        elif order["item"] == "pasta":
            # 20% discount
            discount = 0.2
        elif age < 25 and isBirthday:
            # 15% discount
            discount = 0.15
        elif isBirthday:
            # 5% discount
            discount = 0.05

        bill = int(menu[order["item"]]) * int(order["quantity"]) - (
            discount * int(menu[order["item"]]) * int(order["quantity"])
        )

        # Adding current bill with the customer's previous bills
        if order["customer_id"] in customersBills.keys():
            customersBills[order["customer_id"]] += bill
        else:
            customersBills[order["customer_id"]] = bill

with open("output/customer-bill.csv", "w") as csv_file:
    filednames = ["customer_id", "total_bill"]
    csv_writer = csv.DictWriter(csv_file, fieldnames=filednames)

    csv_writer.writeheader()

    for key in customersBills.keys():
        csv_file.write("%s,%.2f\n" % (key, customersBills[key]))
