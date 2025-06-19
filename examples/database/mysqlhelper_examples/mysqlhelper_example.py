from hilbertlib.database.mysqlhelper import MySQLHelper

db = MySQLHelper(user="root", password="yourpassword")

db.create_database("school")
db.use_database("school")

db.create_table("students", {
    "id": "INT AUTO_INCREMENT PRIMARY KEY",
    "name": "VARCHAR(100)",
    "grade": "INT"
})

db.insert_data("students", {"name": "Kentlee", "grade": 8})
db.insert_data("students", {"name": "Claire", "grade": 9})

results = db.query("SELECT * FROM students")
for row in results:
    print(row)

db.export_to_csv("students", "students.csv")

db.help()