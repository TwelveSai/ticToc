# class Mydialog(StatesGroup):
#     otvet = State()
#
#
# @dp.message_handler()
# async def cmd_dialog(message: types.Message):
#     await Mydialog.otvet.set()
#
#     await message.reply("Человечишка, напиши мне свое жалкое мнение")
#
#
#
# @dp.message_handler()
# async def send_welcome(message: types.Message):
#
#     await message.reply('Устанавливаю связь с сервером...')
#
#
#
#
#
# def check_sub_channel(chat_member):
#
#     if chat_member['status'] != 'left':
#         return True
#     else:
#         return False
