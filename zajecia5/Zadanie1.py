import sqlite3

def show_laptops(cursor):
    print("\n \na)")

    cursor.execute("select * from sales where product = 'Laptop'")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

def show_between_dates(cursor):
    print("\n \nb)")

    cursor.execute("select * from sales "
                   "where date = '2025-05-07'"
                   "OR date = '2025-05-08'")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

def show_above_200_price(cursor):
    print("\n \nc)")

    cursor.execute("select * from sales "
                   "where price > '200'")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

def show_grouped_by_product(cursor):
    print("\n \nd)")

    cursor.execute("select product, SUM(price) from sales "
                   "group by product")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

def show_grouped_by_date(cursor):
    print("\n \ne)")

    cursor.execute("select date, SUM(quantity) from sales "
                   "group by date "
                   "order by SUM(quantity) desc "
                   "limit 1")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

show_laptops(cursor)
show_between_dates(cursor)
show_above_200_price(cursor)
show_grouped_by_product(cursor)
show_grouped_by_date(cursor)

conn.close()