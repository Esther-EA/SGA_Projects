import sqlite3
import csv

# create a database
conn = sqlite3.connect("waec_data.db")
w = conn.cursor()

# create a table format
table = """CREATE TABLE waec_table (
  'Names TEXT',
  'Mathematics INTEGER',
  'English INTEGER',
  'Civics INTEGER',
  'Physics INTEGER',
  'Chemistry INTEGER',
  'Biology INTEGER',
  'Literature INTEGER',
  'Computer INTEGER',
  'Economics INTEGER'
  )
  """
# Create actual table
w.execute(table)


# # open the csv file and read it using the csv module
with open('waec_scores.csv', 'r') as score_file:
  waec_file = csv.reader(score_file)
  next(waec_file)#insert the values of the read file into the sql table 
  w.executemany("""
                INSERT INTO waec_table VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, waec_file)

print('success!!!')


query = w.execute("SELECT * FROM waec_table")
rows = w.fetchall()
print(f"Names\t\tMathematics, English, Civics Education, Physics, Chemistry, Biology, Further Mathematics, Computer Science, Economics")
for row in rows:
  Names, Mathematics, English, Civics, Physics, Chemistry, Biology, Literature, Computer, Economics = row
  print(f"{Names:10}\t{Mathematics}\t{English:10}\t{Civics}\t{Physics}\t{Chemistry:5}\t{Biology:5}\t{Literature:5}\t{Computer:10}\t{Economics}") 

conn.commit()

