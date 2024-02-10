import modules.informator_db.informator_db as database

database.cursor.execute("SELECT Password FROM Administrators")
list_passwords = database.cursor.fetchall()


clear_list_passwords = []

def cleaning_list_passwords():
    for password in list_passwords:
        password = f"{password}"
        clear_list_passwords.append(password.split("('")[1].split("',)")[0])
        print(clear_list_passwords)




print("\n \n")
cleaning_list_passwords()
print("\n \n")

print(f"list passwords {list_passwords}")

