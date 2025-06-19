from hilbertlib.database.hilbertbasicdb import HilbertBasicDB

db = HilbertBasicDB()

db.create_table("users", {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "username": "TEXT",
    "age": "INTEGER"
})

db.insert("users", {"username": "Kentlee", "age": 14})
db.insert("users", {"username": "Claire", "age": 15})

results = db.query("SELECT * FROM users")
for row in results:
    print(row)

db.update("users", {"age": 16}, "username = ?", ("Claire",))

db.delete("users", "username = ?", ("Kentlee",))

db.close()
