from aiogram import Bot, Dispatcher, executor, types
import pyqrcode
bot = Bot(token='5752122444:AAEP43-IqUs3H9BmJn2AdS45vZ24_JAwunA')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def welcome(message: types.Message):
    await  message.reply("Hi my name is QRR and I am here to switch anytext u send me to a qr code.")

dp.message_handler(commands=['logo'])
async def logo(message: types.message):
    await message.answer_photo('https://images7.alphacoders.com/617/thumbbig-617964.webp')


@dp.message_handler()
async def qr(message: types.Message):
    text = pyqrcode.create(message.text)
    text.png('code.png', scale=5)
    await bot.send_photo(chat_id=message.chat.id, photo=open('code.png', 'rb'))


executor.start_polling(dp)



