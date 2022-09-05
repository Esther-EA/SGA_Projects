#import sqlite3
import sqlite3

#check
print('Successful!')

conn = sqlite3.connect('SGA_database')
# #check
print("Opened database successfully") ; print(type(conn))

#create a cursor object
gs = conn.cursor()

# #create a table
# gs.execute(
#     """ 
#     CREATE TABLE SGA_data(
#      first_name TEXT,
#      last_name TEXT,
#      email TEXT
#      )
#      """
# )

# # # #check
# print('Table created successfully')

# Insert all the learners in your group together with their available details into the database
# SGA_data= [ 
#     ('Lawrence', 'Ane', 'lawrenceane@stutern.edu'),
#     ('Kafayat', 'Ibrahim', 'kafayatibrahim@stutern.edu' ),
#     ('Tina', 'Uyateide', 'Tinauyateide@stutern.edu'),
#     ('Deborah', 'Olorunnishola', 'Deboraholorunnishola@stutern.edu'),
#     ('Kehinde', 'Orolade', 'Kehindeorolade@stutern.edu'),
#     ('Theresa', 'Karamor', 'Theresakaramor@stutern.edu'),
#     ('Faith', 'Amure', 'faithamure@stutern.edu'),
#     ('Adisa', 'Abubakar', 'adisaabubakar@stutern.edu'),
#     ('Prince', 'Ekeocha', 'princeekeocha@stutern.edu'),
#     ('Ihuoma', 'Eke', 'ihuomaeke@stutern.edu'),
#     ('Omowunmi', 'Awoniran', 'omowunmiawoniran@stutern.edu'),
#     ('Binta', 'Umar', 'bintaumar@stutern.edu')
#     ]

# gs.executemany(
# """
# INSERT INTO SGA_data
# VALUES (?, ?, ?)

# """,
# SGA_data
# )

# conn.commit

# check
# print('Inserted multiple records')

# # #QUERY
gs.execute(
"""
SELECT * FROM students_info

"""
)

# #fetchall rows in the table
items = gs.fetchall()

#format outputs to display in a tabular form
print("first_name"+ "\t Surname"+ "\t\t e-mail"+ "\t\t course \n" f"{'.' * 80}")

# # #loop through the items
for item in items:
    first_name, last_name, email, course = item
    print(f"{first_name:16}{last_name:16}{email:10}{course}")

conn.commit()

# Alter table Statement
# change name of my table
# gs.execute('ALTER TABLE SGA_data RENAME TO students_info')
# conn.commit()

# check
# print('alter successful')

# # Alter column name:
# gs.execute('ALTER TABLE students_info ADD COLUMN course')
# conn.commit()
# # #check
# print('column added')

# UPDATE STATEMENT
gs.execute("""UPDATE students_info SET course = 'Data Science' """)
conn.commit

# # # check
# # print("course info set")

# conn.close()