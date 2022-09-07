import sqlite3

conn = sqlite3.connect("inventory_data.db")

# #create a cursor object
cursor = conn.cursor()

# # Create a dummy inventory dataset 
# cursor.execute(
#     """
#     CREATE TABLE inventory_data(
#     Inventory_name TEXT,
#     Price INTEGER,
#     Quantity INTEGER,
#     Id_number INTEGER
#     )
#     """
# )

# # # #insert data
# inventory_data = [
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
# INSERT INTO inventory_data
# VALUES (?, ?, ?, ?)
# """,
# inventory_data
# )

# conn.commit()

# items to restock and sufficient from the highest to lowest

item = cursor.execute(
"""
SELECT inventory_name, Price, Quantity,
CASE
WHEN Quantity <= '15' THEN 'Restock'
ELSE 'Available' 
END
FROM inventory_data
WHERE Quantity IS NOT NULL
ORDER BY Price DESC

"""
)

for row in item:
    print(row)
    

