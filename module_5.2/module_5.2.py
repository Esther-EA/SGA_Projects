import sqlite3
import csv

# create a database
conn = sqlite3.connect("waec_data.db")
w = conn.cursor()

# create a table format
# table = """CREATE TABLE waec_table (
#   Names TEXT,
#   Mathematics INTEGER,
#   English INTEGER,
#   Civics INTEGER,
#   Physics INTEGER,
#   Chemistry INTEGER,
#   Biology INTEGER,
#   Literature INTEGER,
#   Computer INTEGER,
#   Economics INTEGER
#   )
#   """
# # Create actual table
# w.execute(table)

# w.execute('drop table waec_table')

# open the csv file and read it using the csv module
# with open('waec_scores.csv', 'r') as score_file:
#   waec_file = csv.reader(score_file)
#   next(waec_file)#insert the values of the read file into the sql table 
#   w.executemany("""
#                 INSERT INTO waec_table VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#                 """, waec_file)

# print('success!!!')


# query = w.execute("SELECT * FROM waec_table")
# rows = w.fetchall()
# print(f"Names\t\tMathematics, English, Civics Education, Physics, Chemistry, Biology, Further Mathematics, Computer Science, Economics")
# for row in rows:
#   Names, Mathematics, English, Civics, Physics, Chemistry, Biology, Literature, Computer, Economics = row
#   print(f"{Names:10}\t{Mathematics}\t{English:10}\t{Civics}\t{Physics}\t{Chemistry:5}\t{Biology:5}\t{Literature:5}\t{Computer:10}\t{Economics}") 



# Which student scored the highest in maths
# item = w.execute(
# """
# SELECT Names,
# MAX(Mathematics) AS MAXIMUM
# FROM waec_table;
# """
# )

# for row in item:
#     print(row)
    
# Which student scored the lowest in english
# item = w.execute(
# """
# SELECT Names,
# MIN(English) AS MINIMUM
# FROM waec_table;
# """
# )

# for row in item:
#     print(row)


# What is the average score of students in maths
# item = w.execute(
# """
# SELECT 
# AVG(Mathematics) AS AVERAGE
# FROM waec_table;
# """
# )

# for row in item:
#     print(row)
    
    
    
# What is the average score of students in english
# item = w.execute(
# """
# SELECT 
# AVG(English) AS AVERAGE
# FROM waec_table;
# """
# )

# for row in item:
#     print(row)
    
# Who is the best performing student across all nine subjects in terms of overall scores
item = w.execute(
"""
SELECT *
AVG(*) AS AVERAGE
FROM waec_table;
"""
)

for row in item:
    print(row)

# Who is the best performing student across all nine subjects in term of average scores







conn.commit()