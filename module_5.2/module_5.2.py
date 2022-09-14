import sqlite3
import csv

#  create a dataabsde
conn = sqlite3.connect("waec_data.db")
w = conn.cursor()

# # CREATE TABLE

w.execute( 
          """
          CREATE TABLE waec_table(
              Names TEXT,
              Mathematics INTEGER,
              English INTEGER,
              Civics Education INTEGER,
              Physics INTEGER,
              Chemistry INTEGER,
              Biology INTEGER,
              Further Mathematics INTEGER,
              Computer Science INTEGER,
              Economics INTEGER
          )
          """
)



#  open the csv file and read it using the csv module
with open('waec_scores.csv', "r") as score_file:
    waec_file = csv.reader(score_file)
    # insert the values of the read file into the sql table
    w.executemany("""
                  INSERT INTO waec_table VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, waec_file)
    
print('Executed successfully')   
conn.commit()

# item = w.execute(
# """
# SELECT Names, Mathematics
# FROM waec_table
# WHERE
# Mathematics= (SELECT MAX(Mathematics)) from waec_table);
# """
# )

# for row in item:
#     print(row)






# conn.close()




# Names, Mathematics, English, Civics Education, Physics, Chemistry, Biology, Further Mathematics, Computer Science, Economics










# Create a dummy csv file that holds information on WAEC scores of at least 20 students across 9 subjects. Give each student a name or an ID
# Use SQLite to load the csv file into a database you created.
# Answer the following questions:
# Which student scored the highest in maths
# Which student scored the lowest in english
# What is the average score of students in maths
# What is the average score of students in english
# Who is the best performing student across all nine subjects in terms of overall scores
# Who is the best performing student across all nine subjects in term of average scores
