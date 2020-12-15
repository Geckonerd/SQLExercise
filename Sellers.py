import sqlite3

connection = sqlite3.connect('Sellers.db')
cursor = connection.cursor()

#cursor.execute("CREATE TABLE sellers (name text, phone text, product text, quantity integer, price real)")

option = None
while option != "Q":
    print("S) Show Sellers")
    print("F) Find Seller")
    print("A) Add Seller")
    print("E) Edit Seller Details")
    print("R) Remove Seller")
    print("Q) Quit the Program")
    option = input("> ")
    print()
    if option == "S":
        cursor.execute("SELECT * FROM sellers")
        print("{:>9} {:>11} {:>14} {:>12} {:>9}".format("Name", "Phone", "Product", "Quantity", "Price"))
        for seller in cursor.fetchall():
            print("{:>10} {:>10} {:>10} {:>10} {:>10}".format(seller[0], seller[1], seller[2], seller[3], seller[4]))

    elif option == "F":
        search = input("Enter name: ")
        print("{:>9} {:>11} {:>14} {:>12} {:>9}".format("Name", "Phone", "Product", "Quantity", "Price"))
        values = (search, )
        cursor.execute("SELECT * FROM sellers WHERE name = ?", values)
        for seller in cursor.fetchall():
            print("{:>10} {:>10} {:>10} {:>10} {:>10}".format(seller[0], seller[1], seller[2], seller[3], seller[4]))

    elif option == "A":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        product = input("Enter product: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        seller = (name, phone, product, quantity, price)
        cursor.execute("INSERT INTO sellers VALUES (?,?,?,?,?)", seller)
        connection.commit()

    elif option == "E":
        name = input("name: ")

        print("Q) Edit product quantity")
        print("P) Edit product price")
        detail = input("> ")
        if detail == "Q":
            quantity = input("new quantity: ")
            values = (quantity, name)
            cursor.execute("UPDATE sellers SET quantity = ? WHERE name = ?", values)
            connection.commit()
        elif detail == "P":
            price = input("new price: ")
            values = (price, name)
            cursor.execute("UPDATE sellers SET price = ? WHERE name = ?", values)
            connection.commit()
        else:
            pass

    elif option == "R":
        name = input("name: ")
        seller = (name, )
        cursor.execute("DELETE FROM sellers WHERE name = ?", seller)
        connection.commit()

    print()
connection.close()