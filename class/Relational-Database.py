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
    print(result)
    # if cursor.rowcount > 0:
    #     for row in result:
    #         print(f"Hello! Iam {row[2]} {row[1]}. My salary is {row[3]} euroes per month")
    return
def getEmployeesByLastname(lastName):
    sql = "SELECT ID, lastname, firstname, salary from employees"
    sql += " WHERE lastname = '" + lastName + "'"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()


    if cursor.rowcount > 0 :
        for row in result :
            print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euroes per month.")
    else:
        print("Does not find database with the input Last Name")
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

def updateSalary(id,newSalary):
    sql = "UPDATE employees SET salary="  + str(newSalary) + " Where id= " + str(id)
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    if cursor.rowcount == 1:
        print("Salary updated")
    else:
        print("ID does not exist")

# getTable()
# # last_name= input("Enter last name: "
# getAllEmployees()
lastName = input("Last name: ")

getEmployeesByLastname(lastName)

id = int(input("Enter id: "))
newSalary = float(input("Enter new salary: "))
updateSalary(id,newSalary)
# lastName = "Mynttinen"
# sql = "SELECT ID, lastname, firstnam, salary from employees"
# sql += "WHERE lastname = '" + lastName + "'"
# print(sql)

