import mysql.connector
link = mysql.connector.connect(host="localhost", user="root", passwd="root", raise_on_warnings=True,
                               database="duplicate_emails")
db_cursor = link.cursor()

# db_cursor.execute("CREATE DATABASE duplicate_emails")

# db_cursor.execute("CREATE TABLE Person(id INT NOT NULL AUTO_INCREMENT, email VARCHAR(255) NOT NULL, PRIMARY KEY(id))")

# db_cursor.execute("INSERT INTO Person(email) VALUES('a@b.com'), ('c@d.com'), ('a@b.com')")

db_cursor.execute("SELECT email FROM Person GROUP BY email HAVING COUNT(email) > 1")

if __name__ == "__main__":
    for db in db_cursor:
        print(db)
