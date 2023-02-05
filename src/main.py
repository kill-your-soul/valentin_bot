# coding: UTF-8

import os
import random
import logging
from vkbottle.bot import Bot, Message
from var import predictions, months


bot = Bot(os.environ["TOKEN"])
logging.basicConfig(level=logging.INFO)



@bot.on.private_message(text=["Начать", "начать"])
async def start(m: Message):
    await m.answer(
        "Приветствую! Я бот от команды [https://vk.com/orgcomsut|ORG.COM].\nСмотри, что я умею делать:\n1. Введите «хочу предсказание» и я отправлю твоё предсказание на ближайший месяц и ты узнаешь, что ждёт тебя в личной жизни!\n2. Введите «совместимость *имя* и *имя*», чтобы узнать на сколько ты и твоя вторая половинка подходите друг другу; ❤\n3. Введите «когда я...», чтобы узнать точную дату когда это произойдёт.\n\nСкорее присылай мне команды и я уверен, что некоторые вещи тебя приятно удивят!\n\nЛюбите и будьте добрее к друг другу. ❤",
        dont_parse_links=True,
    )


@bot.on.private_message(
    text=[
        "совместимость <first_name> и <second_name>",
        "Совместимость <first_name> и <second_name>",
    ]
)
async def lol(m: Message):
    await m.answer(f"Ваша совместимость «{random.randint(30, 100)}%»")


@bot.on.private_message(text=["когда я <some_text>", "Когда я <some_text>"])
async def rand_date(m: Message):
    year = random.randint(2022, 2075)
    if year == 2022:
        month = random.randint(3, 12)
    month = random.randint(1, 12)
    day = random.randint(1, 31)
    await m.answer(f"Это произойдёт «{day} {months[month]} {year}»")


@bot.on.private_message(text=["хочу предсказание", "Хочу предсказание"])
async def predict(m: Message):
    await m.answer(random.choice(predictions))


if __name__ == "__main__":
    bot.run_forever()
