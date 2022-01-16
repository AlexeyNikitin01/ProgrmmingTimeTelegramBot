import os
import logging
import datetime


import services


from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start","help"])
async def start_message(message: types.Message):
    await message.answer(
        "Бот для отчета времени программирования\n\n"
        "Добавить время: 5:30\n"
        "Первый парамет показывает часы, второй минуты\n"
        "Время за сегодня: /today \n"
        "Общее время: /total")


@dp.message_handler(commands=["total"])
async def total(message: types.Message):
    total_time = services._get_total_time()

    if total_time == datetime.timedelta(0):
        await message.answer("Ноль это тоже начало!")
    else:
        await message.answer(f"Ты на пути к успеху: {total_time}")


@dp.message_handler(commands=["today"])
async def today(message: types.Message):
    time_today = services._get_time_today()
    h, m = services._get_h_m_today()

    if time_today == datetime.timedelta(0):
        await message.answer("Ты сегодня еще не начал учиться!")
    else:
        await message.answer(f"Сегодня ты проделал хорошую работу: {h} час(а) {m} минут")


@dp.message_handler()
async def add_time_programming(message: types.Message):
    total_time = services._get_total_time()
    time_today = services._get_time_today()
    try:
        hours, minutes = services._get_parsed_time(message.text)
        delta = services._get_delta(hours, minutes)
        total_time += delta
        time_today += delta
        services._write_file_txt(time_today, total_time)
        if hours <= 12:
            await message.answer(f"Ты сейчас потрудился {hours} час(а) и {minutes} минут")
        else:
            await message.answer(f"Ты отработал сейчас??? {hours} час(а) и {minutes} минут. НЕ ВЕРЮ!")
    except ValueError as err:
        await message.answer("Ого я такого не ожидал(")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
