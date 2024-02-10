import aiogram 
import modules.__settings__ as b_settings


inline_button_accept = aiogram.types.InlineKeyboardButton(text= f"Підтвердити реєстрацію ", callback_data= "enter_reg")
inline_button_reject = aiogram.types.InlineKeyboardButton(text = f"Відхилити реєстрацію ", callback_data= "reject_reg")