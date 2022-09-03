#import sqlite3
import sqlite3
#check
print('Successful!')

conn = sqlite3.connect('SGA_1_3_learners.db')
# #check
print("Opened database successfully") ; print(type(conn))

#create a cursor object
SGA = conn.cursor()

# create a table
# SGA.execute(
#     """ 
#     CREATE TABLE SGA_learners(
#      first_name TEXT,
#      last_name TEXT,
#      email TEXT,
#      course TEXT
#      )
#      """
# )

# # #check
# print('Table created successfully')


# SGA.execute(
#     """
#     INSERT INTO SGA_learners
#     VALUES('Temitope', 'Bamidele', 'temitopebamidele@stutern.edu', 'data science')
#     """
# )

# #check
# print('one record has been added')

#Insert all the learners in your group together with their available details into the database
Stutern_learners = [ 
    ('Lawrence', 'Ane', 'lawrenceane@stutern.edu', 'data science'),
    ('Kafayat', 'Ibrahim', 'kafayatibrahim@stutern.edu', 'data science'),
    ('Tina', 'Uyateide', 'Tinauyateide@stutern.edu', 'data science'),
    ('Deborah', 'Olorunnishola', 'Deboraholorunnishola@stutern.edu', 'data science'),
    ('Kehinde', 'Orolade', 'Kehindeorolade@stutern.edu', 'data science'),
    ('Theresa', 'Karamor', 'Theresakaramor@stutern.edu', 'data science'),
    ('Faith', 'Amure', 'faithamure@stutern.edu', 'data science'),
    ('Adisa', 'Abubakar', 'adisaabubakar@stutern.edu', 'data science'),
    ('Prince', 'Ekeocha', 'princeekeocha@stutern.edu', 'data science'),
    ('Ihuoma', 'Eke', 'ihuomaeke@stutern.edu', 'data science'),
    ('Omowunmi', 'Awoniran', 'omowunmiawoniran@stutern.edu', 'data science'),
    ('Binta', 'Umar', 'bintaumar@stutern.edu', 'data science'),
    ('Ade', 'Afolabi', 'adeafolabi@stutern.edu', 'data science'),
    ('Idowu', 'Adesanya', 'idowuadesanya@stutern.edu', 'data science'),
    ('Romotallah', 'Jubril', 'romotallahjubril@stutern.edu', 'data science'),
    ('Mariam', 'Adeoti', 'mariamadeoti@stutern.edu', 'data science'),
    ('Christian', 'Uzondu', 'christianuzondu@stutern.edu', 'data science'), 
    ('Adedoyin', 'Abass', 'adedoyinabass@stutern.edu', 'data science'),
    ('Joyce', 'Ezeonwu', 'joyceezeonwu@stutern.edu', 'data science'),
    ('Rahidat', 'sikiru', 'rahidatsikiru@stutern.edu', 'data science'),
    ('Angela', 'Emmanuel', 'angelaemmanuel@stutern.edu', 'data science'),
    ('Cynthia', 'Awiya', 'cynthiaawiya@stutern.edu', 'data science'),
    ('Sheriff', 'Olaitan', 'sheriffolaitan@stutern.edu', 'data science'),
    ('Placidus', 'Ali', 'placidusali@stutern.edu', 'data science'),
    ('Victoria', 'Chukwuno', 'victoriachukwuno@stutern.edu', 'data science'),
    ('Eniola', 'Osadare', 'eniolaosadare@stutern.edu', 'data science'),
    ('Stephen', 'Ogungbile', 'stephenogungbile@stutern.edu', 'data science'),
    ('Ganiyat', 'Shittu', 'ganiyatshittu@stutern.edu', 'data science'),
    ('Praise', 'Emmanuel', 'praiseemmanuel@stutern.edu', 'data science')
    ]

SGA.executemany(
"""
INSERT INTO SGA_learners
VALUES (?, ?, ?, ?)

""",
Stutern_learners
)

# # check
# print('Inserted multiple records')

#QUERY
SGA.execute(
"""
SELECT * FROM SGA_learners

"""
)

#fetchall rows in the table
items = SGA.fetchall()

#format outputs to display in a tabular form
print("first_name"+ "\t Surname"+ "\t e-mail" "\t\t\t\t Course \n" f"{'.' * 90}")

#loop through the items
for item in items:
    first_name, last_name, email, course = item
    print(f"{first_name:16}{last_name:16}{email}\t\t{course}")
    
#print confirmation message
print("Command executed successfully...")

#commit database and table
conn.commit()

#close the connection to the table
conn.close()