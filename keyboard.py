

from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup





ask = InlineKeyboardMarkup(row_width=1)

keyButton = InlineKeyboardButton('Подкючение Вконтакте', callback_data='button1')
keyButton2 = InlineKeyboardButton('Подкючение Инстаграмма', callback_data='button2')
keyButton3 = InlineKeyboardButton('Продолжить', callback_data='button3')

ask.add(keyButton, keyButton2)




inkb  = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Продолжить', callback_data='www'))

inkb2  = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Продолжить', callback_data='sss'))

inkb3  = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Узнать место в очереди', callback_data='ooo'))

inkb4  = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Продолжить', callback_data='button4'))

#inline_btn_1 = InlineKeyboardButton('Подкючение гостей', callback_data='button1')
#inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

#inline_btn_2 = InlineKeyboardButton('Подкючение уведомлений', callback_data='button2')
#inline_kb2 = InlineKeyboardMarkup().add(inline_btn_2)





