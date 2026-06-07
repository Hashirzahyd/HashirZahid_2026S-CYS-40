import sqlite3

def setup():
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL, quantity INTEGER, low_limit INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS suppliers (id INTEGER PRIMARY KEY, name TEXT, contact TEXT, email TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS movements (id INTEGER PRIMARY KEY, product TEXT, type TEXT, qty INTEGER, date TEXT)")
    cur.execute("SELECT * FROM users WHERE username='admin'")
    if not cur.fetchone():
        cur.execute("INSERT INTO users VALUES (NULL,'admin','admin123','Admin')")
        cur.execute("INSERT INTO users VALUES (NULL,'staff','staff123','Staff')")
    con.commit()
    con.close()

def check_login(u, p):
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (u, p))
    row = cur.fetchone()
    con.close()
    return row

def get_products():
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    con.close()
    return rows

def add_product(name, cat, price, qty, low):
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("INSERT INTO products VALUES (NULL,?,?,?,?,?)", (name, cat, price, qty, low))
    con.commit()
    con.close()

def update_product(pid, name, cat, price, qty, low):
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("UPDATE products SET name=?,category=?,price=?,quantity=?,low_limit=? WHERE id=?", (name, cat, price, qty, low, pid))
    con.commit()
    con.close()

def delete_product(pid):
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("DELETE FROM products WHERE id=?", (pid,))
    con.commit()
    con.close()

def get_low_stock():
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM products WHERE quantity <= low_limit")
    rows = cur.fetchall()
    con.close()
    return rows

def get_suppliers():
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM suppliers")
    rows = cur.fetchall()
    con.close()
    return rows

def add_supplier(name, contact, email):
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("INSERT INTO suppliers VALUES (NULL,?,?,?)", (name, contact, email))
    con.commit()
    con.close()

def get_movements():
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM movements")
    rows = cur.fetchall()
    con.close()
    return rows

def add_movement(product, mtype, qty, date):
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("INSERT INTO movements VALUES (NULL,?,?,?,?)", (product, mtype, qty, date))
    if mtype == "IN":
        cur.execute("UPDATE products SET quantity=quantity+? WHERE name=?", (qty, product))
    else:
        cur.execute("UPDATE products SET quantity=quantity-? WHERE name=?", (qty, product))
    con.commit()
    con.close()