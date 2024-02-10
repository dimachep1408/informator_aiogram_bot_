import aiogram
import asyncio
import aiogram.filters
import modules.informator_db.informator_db as database
import modules.informator_db.cleaning_nicknames
import modules.informator_db.cleaning_passwords
import modules

import sqlite3
import tracemalloc
tracemalloc.start()



reg_list2 = []



@modules.dispatcher.message(aiogram.filters.CommandStart())
async def start(message : aiogram.types.Message):
    await message.answer(text = "hello world!", reply_markup= modules.keyboard)
    modules.chat_list.append(message.chat.id)
    print(message.chat.id)

    modules.users_Nicknames_list.append(message.from_user.username)


@modules.dispatcher.message()
async def administrator(message : aiogram.types.Message):

    if modules.flag_reg[-1] == "YES":
        await message.answer(text = "Ви увійшли!", reply_markup = modules.keyboard4)
    
    if message.text == "Вихід з акаунту":
        modules.flag_reg.append("NO!")
        
        if modules.flag_reg[-1] != "NO!":
            await message.answer(text = "hello World!", reply_markup = modules.keyboard)

    if message.text == "Клієнт":
        await message.answer(text = "войти или зарегистрироватся", reply_markup= modules.keyboard2)

    
    if message.text == "Адміністратор":
        await message.answer(text = "войти или зарегистрироватся", reply_markup= modules.keyboard2)

    if message.text == "Реєстрація як адміністатор":
        await message.answer(text = "Напишить \n gmail, nickname, password, phone number")
        await message.answer(text = "Пример: \n dima@email.com, DmitriyChep, 123321, +380123456991 ")
        modules.flag.append("sign up")

    if message.text == "Реєстрація як клієнт":
        await message.answer(text = "Напишить \n gmail, nickname, password, phone number")
        await message.answer(text = "Пример: \n dima@email.com, DmitriyChep, 123321, +380123456991 ")
        modules.flag_client.append("sign up")

    if message.text == "Авторизація як адмінітсратор":
        await message.answer(text = "Напишить \n Nickname, password")
        await message.answer(text = "Пример: \n DmitriyChep, 123321 ")
        modules.flag.append("sign in")

    if message.text == "Авторизація як клієнт":
        await message.answer(text = "Напишить \n Nickname, password")
        await message.answer(text = "Пример: \n DmitriyChep, 123321 ")
        modules.flag_client.append("sign in")

    if message.text not in modules.trash_messages_list and modules.flag[-1] == "sign in":
        login = message.text.split(",")
        print(login)
        nickname_login = login[0]
        password_login = login[1]
        print("\n")

        print("", nickname_login)
        print("", password_login)

        print(nickname_login.strip() == modules.clear_list_nicknames[-1].strip())
        print(password_login.strip() == modules.clear_list_passwords[-1].strip())

        

        print("\n")
            
        for nickname in modules.clear_list_nicknames:

            if nickname_login.strip() == nickname.strip():
                login_flag_nickname = True
                print("nice!")
            else:
                login_flag_nickname = False
                print("nope!")
        
        for password in modules.clear_list_passwords:

            if password_login.strip() == password.strip():
                login_flag_password = True
                print("nice!!!")
            else:
                login_flag_password = False
                print("nope!!!")

        if login_flag_nickname == True and login_flag_password == True:

            modules.flag_reg.append("YES") 
            print("YES")
            await message.answer(text = "Ви успішно зареєструвались!")
        else:
            await message.answer(text = "Не знайдено")
            


        
    if message.text not in modules.trash_messages_list and modules.flag[-1] == "sign up":
        try:
            modules.trash_messages_list.append(message.text)
            reg_list = message.text.split(",")


            
            inline_button_accept = aiogram.types.InlineKeyboardButton(text= f"Підтвердити реєстрацію {modules.users_Nicknames_list[-1]}", callback_data= "enter_reg")
            inline_button_reject = aiogram.types.InlineKeyboardButton(text = f"Відхилити реєстрацію {modules.users_Nicknames_list[-1]}", callback_data= "reject_reg")
            inline_keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard= [[inline_button_accept],[inline_button_reject]])

            if len(reg_list) == 4:
                email = reg_list[0].strip()
                nickname = reg_list[1].strip()
                password = reg_list[2].strip()
                phone_number = reg_list[3].strip()

                if '@' in email and '.' in email:
                    reg_list2.extend([email, nickname, password, phone_number])

                    await modules.bot.send_message(chat_id=-4155243696, text=f"Пользователь {modules.users_Nicknames_list[-1]} хочет зарегистрироваться", reply_markup=inline_keyboard)

                    print(f"list trash: {modules.trash_messages_list}")
                else:
                    raise ValueError("Некорректный email")

            else:
                raise ValueError("Необходимо ввести ровно 4 значения")

        except (ValueError, IndexError) as e:
            await message.answer(text="Помилка:")
            await message.answer(text="Напишите\nemail, nickname, password, phone number")
            await message.answer(text="Пример:\ndima@email.com, DmitriyChep, 123321, +380123456991 ")
            print(f"Error: {e}")


    if message.text not in modules.trash_messages_list and modules.flag_client[-1] == "sign up":
        try:
            modules.trash_messages_list.append(message.text)
            reg_list = message.text.split(",")
            print(reg_list)

            
            inline_button_accept = aiogram.types.InlineKeyboardButton(text= f"Підтвердити реєстрацію {modules.users_Nicknames_list[-1]}", callback_data= "enter_reg")
            inline_button_reject = aiogram.types.InlineKeyboardButton(text = f"Відхилити реєстрацію {modules.users_Nicknames_list[-1]}", callback_data= "reject_reg")

            inline_keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard= [[inline_button_accept],[inline_button_reject]])

            if len(reg_list) == 4:
                email = reg_list[0].strip()
                nickname = reg_list[1].strip()
                password = reg_list[2].strip()
                phone_number = reg_list[3].strip()

                if '@' in email and '.' in email:
                    reg_list2.extend([email, nickname, password, phone_number])


                    print(f"list trash: {modules.trash_messages_list}")
                else:
                    raise ValueError("Некорректный email")

            else:
                raise ValueError("Необходимо ввести ровно 4 значения")
            

        except (ValueError, IndexError) as e:
            await message.answer(text="Помилка:")
            await message.answer(text="Напишите\nemail, nickname, password, phone number")
            await message.answer(text="Пример:\ndima@email.com, DmitriyChep, 123321, +380123456991 ")
            print(f"Error: {e}")

@modules.dispatcher.callback_query()
async def accept_reg(callback : aiogram.types.CallbackQuery):
    
    if "enter_reg" in callback.data:
        database.cursor.execute(f"INSERT INTO Administrators(Email, Nickname, Password,Phone_number) VALUES ('{reg_list2[0]}', '{reg_list2[1]}', '{reg_list2[2]}', '{reg_list2[3]}')")
        await modules.bot.send_message(chat_id= modules.chat_list[-1], text = "Вас було зареєстровано, далі треба увійти")
        database.connection.commit()
        database.connection.cursor()

    if "reject_reg" in callback.data:
        await modules.bot.send_message(chat_id= modules.chat_list[-1], text = "Вашу реєстрацію було відхилено")


    # print(message.text)
    # print(" ")

                


        
         


        
async def main():
    await modules.dispatcher.start_polling(modules.bot)

if __name__ == "__main__":
    asyncio.run(main())


