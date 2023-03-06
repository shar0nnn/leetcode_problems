import mysql.connector

link = mysql.connector.connect(host="localhost", user="root", passwd="root", raise_on_warnings=True,
                               database="customers_who_never_order")
db_cursor = link.cursor()

# db_cursor.execute("CREATE DATABASE customers_who_never_order")

# db_cursor.execute("CREATE TABLE Customers("
#                   "id INT NOT NULL AUTO_INCREMENT, name VARCHAR(255), PRIMARY KEY(id))")
#
# db_cursor.execute("CREATE TABLE Orders("
#                   "id INT NOT NULL AUTO_INCREMENT, customerID INT NOT NULL, "
#                   "PRIMARY KEY(id), FOREIGN KEY(customerID) REFERENCES customers(id))")

# db_cursor.execute(
#     "INSERT INTO customers(name) VALUES('Joe'), ('Henry'), ('Sam'), ('Max')")
# db_cursor.execute(
#     "INSERT INTO orders(customerID) VALUES(3), (1)")

db_cursor.execute("SELECT customers.name AS Customers FROM customers"
                  " WHERE customers.id not in (SELECT orders.customerID FROM orders)")

if __name__ == "__main__":
    for db in db_cursor:
        print(db)
