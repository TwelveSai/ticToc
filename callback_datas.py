class Mydialog(StatesGroup):
    otvet = State()  # Will be represented in storage as 'Mydialog:otvet'

#Здесь мы начинаем общение с клиентом и включаем состояния
@dp.message_handler()
async def cmd_dialog(message: types.Message):
    await Mydialog.otvet.set()  # вот мы указали начало работы состояний (states)

    await message.reply("Человечишка, напиши мне свое жалкое мнение")


    
@dp.message_handler()
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
   # await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
    await message.reply('Устанавливаю связь с сервером...')




    
def check_sub_channel(chat_member):
   
    if chat_member['status'] != 'left':
        return True
    else:
        return False
