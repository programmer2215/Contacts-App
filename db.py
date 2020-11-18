import sqlite3

con = sqlite3.connect('contacts.sqlite')
cur = con.cursor()

fields = {'FirstName': 0, 'LastName': 1, 'Gender': 2, 'Phone': 3, 'Email': 4, 'Address':5}

def create_table():
    cur.execute('''CREATE TABLE ContactList ( 
        FirstName VARCHAR(64), 
        LastName VARCHAR(64), 
        Gender VARCHAR(32), 
        Phone INT, 
        Email VARCHAR(64), 
        Address VARCHAR(255) )''')

def create_record(a,b,c,d,e,f):
    try:
        cur.execute('INSERT INTO ContactList VALUES(?, ?, ?, ?, ?, ?)', (a,b,c,d,e,f))
        con.commit()
    except sqlite3.OperationalError:
        create_table()
        create_record(a,b,c,d,e,f)

def limit_duplication(record):
    a = []
    sql = 'SELECT * FROM Contactlist'
    for i in cur.execute(sql):
        for j in record:
            if j == str(i[record.index(j)]):
                a.append(True)
            else: a.append(False)
        
        if a.count(True) == 5:
            return True
        else:
            a.clear()
    if len(a) == 0:
        return False

def sort_element(elem):
    return elem[0]

def view_contact(reference_var, field, sort):
    global fields
    results = []
    data = 'SELECT * FROM ContactList'
    if field == 'Phone':
        reference_var = int(reference_var)
    if field == 'Address':
        for row in cur.execute(data):
            if reference_var in row[(fields[field])]:
                results.append(row)
    else:
        for row in cur.execute(data):
            if row[(fields[field])] == reference_var:
                results.append(row)
    if sort == 'A-Z':
        results = sorted(results, key=sort_element, reverse=False)
    elif sort == 'Z-A':
        results = sorted(results, key=sort_element, reverse=True)

    return results
