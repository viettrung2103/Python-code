import mysql.connector

## configure connection
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3300,
    database = "people",
    user = "root",
    password = "",
    autocommit = True,
)

def getAllEmployees():
    sql = "SELECT * FROM employees"

    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Hello! Iam {row[2]} {row[1]}. My salary is {row[3]} euroes per month")
    return
def getEmployeesByLastname(lastName):
    sql = "SELECT ID, lastname, firstname, salary from employees"
    sql += " WHERE lastname = '" + lastName + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0 :
        for row in result :
            print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euroes per month.")
    return



def getTable():
    sql = "SHOW tables"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall();
    if cursor.rowcount > 0:
        for row in result:
            print(row)
    return

# getTable()
# # last_name= input("Enter last name: "
# getAllEmployees()
getEmployeesByLastname("Mynttinen")

# lastName = "Mynttinen"
# sql = "SELECT ID, lastname, firstnam, salary from employees"
# sql += "WHERE lastname = '" + lastName + "'"
# print(sql)

