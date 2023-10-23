id = 1
name = "Huy"
city = "Helsinki"
sql = "SELECT robot.id, robot.name, robot.type, robot.pollutstat from robot,city"
moreSql = f"{sql} WHERE robot.location = city.id"
finalSql = f"{moreSql} AND city.name = '{city}'"
print(finalSql)

