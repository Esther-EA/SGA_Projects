import sqlite3

conn = sqlite3.connect("inventory_dataset.db")

# #create a cursor object
cursor = conn.cursor()

# # Create a dummy inventory dataset 
# cursor.execute(
#     """
#     CREATE TABLE inventory_data2(
#     Inventory_name TEXT,
#     Price INTEGER,
#     Quantity INTEGER,
#     Id_number INTEGER
#     )
#     """
# )

# # # # #insert data
# inventory_data2 = [
#     ('marker', '2000', '24', '1011'),
#     ('staple pin', '1900', '10', '1014'),
#     ('pen', '5800', '116', '1148'),
#     ('Tissues', '4600', '96', '1829'),
#     ('books', '9000', '108', '1123'),
#     ('stapler', '18000', '12', '1348'),
#     ('A4 paper', '11000', '10', '1927'),
#     ('ink/ toner cartridges', '31600', '2', '1134'),
#     ('file folders', '18000', '2500', '1228'),
#     ('calculator', '16000', '5', '1112'),
#     ('stamp pad', '7000', '12', '1040'),
#     ('perforator', '12000', '10', '1156'),
#     ('scissors', '7200', '24', '1156'),
#     ('pencil', '2380', '114', '1192')
#     ]

# cursor.executemany(
# """
# INSERT INTO inventory_data2
# VALUES (?, ?, ?, ?)
# """,
# inventory_data2
# )

# conn.commit()


# • Calculate the amount the business owner invested in the procurement of the items.
item = cursor.execute(
"""   
SELECT 
SUM(Price) AS Total
FROM inventory_data2;
"""
)

for row in item:
    print(row)

# • Calculate the average quantity of items in stock.
item = cursor.execute(
"""
SELECT 
AVG(Quantity) AS AVERAGE
FROM inventory_data2;
"""
)

for row in item:
    print(row)

# • Determine the item with the least quantity in stock
item = cursor.execute(
"""
SELECT 
MIN(Quantity) AS MINIMUM
FROM inventory_data2;
"""
)

for row in item:
    print(row)

# • Determine the item with the most quantity in stock 
item = cursor.execute(
"""
SELECT 
MAX(Quantity) AS MAXIMUM
FROM inventory_data2;
"""
)

for row in item:
    print(row)