import logging

import random
import time
from aiogram import Bot, Dispatcher, executor, types
import keyboard as kb

from aiogram.dispatcher.filters.state import State, StatesGroup


API_TOKEN = ''

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


#import config as cfg
from aiogram import Bot, executor, types
from aiogram.dispatcher import Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
#scheduler = AsyncIOScheduler()


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, validate_token=True)
dp = Dispatcher(bot, storage=MemoryStorage())
scheduler = AsyncIOScheduler()
scheduler.start()


class Form(StatesGroup):
    name = State()


@dp.message_handler(commands=['url'])
async def start(message: types.Message):
    """Conversation entrypoint"""

    # Set state
    await Form.name.set()
    await message.reply("Отправьте ссылку на вашу страницу")


# You can use state='*' if you want to handle all states
@dp.message_handler(state='*', commands=['cancel'])
async def cancel_handler(message: types.Message, state: FSMContext):
    """Allow user to cancel action via /cancel command"""

    current_state = await state.get_state()
    if current_state is None:
        # User is not in any state, ignoring
        return

    # Cancel state and inform user about it
    await state.finish()
    await message.reply('Cancelled.')


@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    """Process user name"""

    # Finish our conversation
    await state.finish()
    await message.reply(f"Чтобы подключить функцию просмотра гостей на,\n{message.text} нажми на кнопку ниже!", reply_markup=kb.inkb2)
    #time.sleep(60) # <-- Here we get the name








#reply_markup=kb.inline_kb1


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
   # await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
    await message.reply('Привет! Этот бот поможет тебе подключить функцию\nпросмотра гостей на свой профиль в Инстаграм\Вконтакте, а также\nподключить уведомления о действиях пользователей\nЖмина кнопку ниже, чтобы продолжить',reply_markup=kb.ask )
    #time.sleep(60)
    




@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите теперь команду /url', reply_markup=kb.inkb)
    #time.sleep(60)


@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите теперь команду /url', reply_markup=kb.inkb)
    #time.sleep(60)





CHAT_ID  = '@STAFF'

NOTSUB = 'Вы не подписались'

@dp.callback_query_handler(lambda c: c.data == 'sss')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
   # if check_sub_channel(await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user)):
    await bot.send_message(callback_query.from_user.id, 'Для установки обновление с функцией просмотра гостей тебе необходимо подписаться на каналы спонсоров:\nhttps://t.me/lolz_guru\n\nhttps://t.me/lolz_guru\n\nhttps://t.me/lolz_guru\nЭто каналы наших спонсоров, благодаря ним наш бот бесплатный! ',reply_markup=kb.inkb4 )
   # else:
    #    await  bot.send_message(message.from_user.id, NOTSUB)
    







#команда на уведомление
@dp.message_handler(commands='test')
async def test_commands(message  : types.Message):
    await message.answer('Инлайн кнопка', reply_markup=kb.inkb)






    # Finish conversation



@dp.callback_query_handler(text='button4')
async def www_call(callback : types.CallbackQuery):
    #await callback.message.answer('Нажата инлайн кнопка')
    await callback.answer('ANTI-SPAM\nНажмините ок для подверждения,  что вы человек', show_alert=True)
    #time.sleep(60)
    await callback.message.edit_text("Проверяем подписку.")
    time.sleep(2)
    await callback.message.edit_text("Подключаемся к базе данных..")
    time.sleep(4)
    await callback.message.edit_text("Изменяем конфигурацию вашей страницы...")
    time.sleep(6)
    await callback.message.edit_text("Сохроняем изменения....")
    time.sleep(9)
    await callback.message.edit_text("Введите команду /pos для  завершения")







#текст в уведомление
@dp.callback_query_handler(text='www')
async def www_call(callback : types.CallbackQuery):
    #await callback.message.answer('Нажата инлайн кнопка')
    await callback.answer('Введите теперь команду /url', show_alert=True)






@dp.message_handler(commands='pos')
async def send_msg(message: types.Message):
    await message.answer("сейчас ты 172 в очерди на подключение, нажми на кнопку что-бы узнать своё место в очереди",reply_markup=kb.inkb3)
   #msg = 
   #date = datetime.now() + timedelta(minutes=1)
    #scheduler.add_job(edit_msg, "date", run_date=date, kwargs={"message": msg})
    #await asyncio.sleep(5)





@dp.message_handler()
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
   # await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
    await message.reply('Хмхмхмхм.... Введи команду /start')
    
#for check in range(100, 10, -2):
    #async def edit_msg(message: types.Message):
       # await message.edit_text(f'Вы {check}  в очереди.')


@dp.callback_query_handler(text='ooo')
async def www_call(callback : types.CallbackQuery):
    #await callback.message.answer('Нажата инлайн кнопка')



        while True:
            a = random.randrange(25,172,7)
           
            await callback.answer(f'Вы  уже {a}  в очереди.\nТайм-аут на кнопке 120 секунд' , show_alert=True)
            time.sleep(120)
            #await message.answer("сейчас ты  94 в очерди на подключение, нажми на кнопку что-бы узнать своё место в очереди",reply_markup=kb.inkb3)

            






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



