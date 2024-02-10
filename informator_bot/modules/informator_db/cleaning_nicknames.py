import modules.informator_db.informator_db as database



database.cursor.execute("SELECT Nickname FROM Administrators")
list_nicknames = database.cursor.fetchall()




clear_list_nicknames = []

def cleaning_list_nicknames():
    for nickname in list_nicknames:
        nickname = f"{nickname}"
        clear_list_nicknames.append(nickname.split("('")[1].split("',)")[0])
        print(clear_list_nicknames)


print("\n \n")
cleaning_list_nicknames()
print("\n \n")

print(f"list nicknames : {list_nicknames}")
