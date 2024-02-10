import aiogram
import modules.bot_modules.objects.buttons.buttons as buttons

keyboard = aiogram.types.ReplyKeyboardMarkup(keyboard = [[buttons.button1, buttons.button2]])
keyboard2 = aiogram.types.ReplyKeyboardMarkup(keyboard = [[buttons.button3, buttons.button4]])
keyboard3 = aiogram.types.ReplyKeyboardMarkup(keyboard = [[buttons.button5, buttons.button6]])
keyboard4 = aiogram.types.ReplyKeyboardMarkup(keyboard = [[buttons.button7], [buttons.button8]])