import mysql.connector

link = mysql.connector.connect(host="localhost", user="root", passwd="root", raise_on_warnings=True,
                               database="combine_two_tables")
db_cursor = link.cursor()

# db_cursor.execute("CREATE DATABASE combine_two_tables")

# db_cursor.execute("CREATE TABLE Person("
#                   "personID INT NOT NULL AUTO_INCREMENT, lastName VARCHAR(255),"
#                   " firstName VARCHAR(255), PRIMARY KEY(personID))")

# db_cursor.execute("CREATE TABLE Address("
#                   "addressID INT NOT NULL AUTO_INCREMENT, personID INT NOT NULL,"
#                   " city VARCHAR(255), state VARCHAR(255), PRIMARY KEY(addressID))")

# db_cursor.execute(
#     "INSERT INTO combine_two_tables.Person(lastName, firstName) VALUES('Wang', 'Allen'), ('Alice', 'Bob')")
# db_cursor.execute(
#     "INSERT INTO combine_two_tables.Address(personID, city, state) VALUES(2, 'New York City', 'New York'),"
#     "(3, 'Leetcode', 'California')")

db_cursor.execute(
    "SELECT person.firstName, person.lastName, address.city, address.state FROM person LEFT JOIN address"
    " ON address.personID = person.personID")

if __name__ == "__main__":
    for db in db_cursor:
        print(db)
