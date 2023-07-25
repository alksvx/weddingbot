import time
import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def starter(message):
    user_id, first_name, last_name = message.from_user.username, message.from_user.first_name, message.from_user.last_name
    bot.send_message(message.chat.id,
                     f'Привет, {first_name} {last_name}!\n Мы будем очень рады видеть тебя на нашей свадьбе✨')
    pic = open('invitation.png', 'rb')
    time.sleep(1)
    bot.send_photo(message.chat.id, pic)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Приду👍")
    markup.row(btn1)
    btn2 = types.KeyboardButton("Не приду👎")
    markup.row(btn2)
    bot.send_message(message.chat.id,
                     'Пожалуйста, подтверди свое присутствие до 19 июня 2023г.\n Если твои планы изменятся, просим, предупредить нас заранее😊',
                     reply_markup=markup)

    bot.register_next_step_handler(message, on_click)


def on_click(message):


    if message.text == 'Приду👍':
        # ЗАПОЛНЯЕМ БД ACCEPTION
        user_id, first_name, last_name = message.from_user.username, message.from_user.first_name, message.from_user.last_name
        conn = sqlite3.connect('wed.sql')
        cur = conn.cursor()
        presence = message.text
        cur.execute('INSERT INTO acception (user_id, name, surname, presence) VALUES (?, ?, ?, ?)',
                    (user_id, first_name, last_name, presence))
        conn.commit()
        poll_drinks = types.ReplyKeyboardMarkup()
        wine = types.KeyboardButton("Белое/красное вино")  # добавить тег в БД
        poll_drinks.row(wine)
        vodka = types.KeyboardButton("Водка")  # добавить тег в БД
        poll_drinks.row(vodka)
        cognac = types.KeyboardButton("Коньяк")  # добавить тег в БД
        poll_drinks.row(cognac)
        whiskey = types.KeyboardButton("Виски")  # добавить тег в БД
        poll_drinks.row(whiskey)
        alcohol_free = types.KeyboardButton("Безалкогольные напитки")  # добавить тег в БД
        poll_drinks.row(alcohol_free)
        bot.send_message(message.chat.id,
                         'Мы очень рады, что ты придешь! Пройди, пожалуйста, небольшой опрос',
                         reply_markup=types.ReplyKeyboardRemove())
        time.sleep(1)
        bot.send_message(message.chat.id, 'Уточни свои предпочтения в алкоголе', reply_markup=poll_drinks)

        bot.register_next_step_handler(message, food)

    elif message.text == "Не приду👎":
        bot.send_message(message.chat.id,
                         'Нам очень жаль, что ты не сможешь разделить с нами этот день, но мы будем рады встретиться с тобой в любое другое время.\n Если у тебя все-таки получится по присутствовать на нашем мероприятии, дай нам знать😉\n Будем ждать',
                         reply_markup=types.ReplyKeyboardRemove())

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Приду👍")
        markup.row(btn1)
        btn2 = types.KeyboardButton("Не приду👎")
        markup.row(btn2)
        bot.send_message(message.chat.id,
                         'Пожалуйста, выбери корректный вариант', reply_markup=markup)

        bot.register_next_step_handler(message, on_click)





def food(message):

    if message.text == "Белое/красное вино":
        conn = sqlite3.connect('wed.sql')
        cur = conn.cursor()
        user_id, first_name, last_name, drink = message.from_user.username, message.from_user.first_name, message.from_user.last_name, message.text
        cur.execute('INSERT INTO drinks (user_id, name, surname, drinks) VALUES (?, ?, ?, ?)',
                    (user_id, first_name, last_name, drink))
        conn.commit()
        food1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        meat = types.KeyboardButton("Мясо")
        food1.row(meat)
        fish = types.KeyboardButton("Рыба")
        food1.row(fish)
        bot.send_message(message.chat.id, 'Уточни свои предпочтения в еде', reply_markup=food1)
        bot.register_next_step_handler(message, db)

    elif message.text == "Водка":
        conn = sqlite3.connect('wed.sql')
        cur = conn.cursor()
        user_id, first_name, last_name, drink = message.from_user.username, message.from_user.first_name, message.from_user.last_name, message.text
        cur.execute('INSERT INTO drinks (user_id, name, surname, drinks) VALUES (?, ?, ?, ?)',
                    (user_id, first_name, last_name, drink))
        conn.commit()
        food1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        meat = types.KeyboardButton("Мясо")
        food1.row(meat)
        fish = types.KeyboardButton("Рыба")
        food1.row(fish)
        bot.send_message(message.chat.id, 'Уточни свои предпочтения в еде', reply_markup=food1)
        bot.register_next_step_handler(message, db)

    elif message.text == "Коньяк":
        conn = sqlite3.connect('wed.sql')
        cur = conn.cursor()
        user_id, first_name, last_name, drink = message.from_user.username, message.from_user.first_name, message.from_user.last_name, message.text
        cur.execute('INSERT INTO drinks (user_id, name, surname, drinks) VALUES (?, ?, ?, ?)',
                    (user_id, first_name, last_name, drink))
        conn.commit()
        food1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        meat = types.KeyboardButton("Мясо")
        food1.row(meat)
        fish = types.KeyboardButton("Рыба")
        food1.row(fish)
        bot.send_message(message.chat.id, 'Уточни свои предпочтения в еде', reply_markup=food1)
        bot.register_next_step_handler(message, db)

    elif message.text == "Виски":
        conn = sqlite3.connect('wed.sql')
        cur = conn.cursor()
        user_id, first_name, last_name, drink = message.from_user.username, message.from_user.first_name, message.from_user.last_name, message.text
        cur.execute('INSERT INTO drinks (user_id, name, surname, drinks) VALUES (?, ?, ?, ?)',
                    (user_id, first_name, last_name, drink))
        conn.commit()
        food1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        meat = types.KeyboardButton("Мясо")
        food1.row(meat)
        fish = types.KeyboardButton("Рыба")
        food1.row(fish)
        bot.send_message(message.chat.id, 'Уточни свои предпочтения в еде', reply_markup=food1)
        bot.register_next_step_handler(message, db)

    elif message.text == "Безалкогольные напитки":
        conn = sqlite3.connect('wed.sql')
        cur = conn.cursor()
        user_id, first_name, last_name, drink = message.from_user.username, message.from_user.first_name, message.from_user.last_name, message.text
        cur.execute('INSERT INTO drinks (user_id, name, surname, drinks) VALUES (?, ?, ?, ?)',
                    (user_id, first_name, last_name, drink))
        conn.commit()
        food1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        meat = types.KeyboardButton("Мясо")
        food1.row(meat)
        fish = types.KeyboardButton("Рыба")
        food1.row(fish)
        bot.send_message(message.chat.id, 'Уточни свои предпочтения в еде', reply_markup=food1)
        bot.register_next_step_handler(message, db)

    else:
        poll_drinks = types.ReplyKeyboardMarkup()
        wine = types.KeyboardButton("Белое/красное вино")  # добавить тег в БД
        poll_drinks.row(wine)
        vodka = types.KeyboardButton("Водка")  # добавить тег в БД
        poll_drinks.row(vodka)
        cognac = types.KeyboardButton("Коньяк")  # добавить тег в БД
        poll_drinks.row(cognac)
        whiskey = types.KeyboardButton("Виски")  # добавить тег в БД
        poll_drinks.row(whiskey)
        alcohol_free = types.KeyboardButton("Безалкогольные напитки")  # добавить тег в БД
        poll_drinks.row(alcohol_free)
        bot.send_message(message.chat.id, 'Пожалуйста, выбери корректный вариант', reply_markup=poll_drinks)

        bot.register_next_step_handler(message, food)





def db(message):
    if message.text == "Мясо":
        conn = sqlite3.connect('wed.sql')
        cur = conn.cursor()
        user_id, first_name, last_name, food = message.from_user.username, message.from_user.first_name, message.from_user.last_name, message.text
        cur.execute('INSERT INTO food (user_id, name, surname, food) VALUES (?, ?, ?, ?)',
                    (user_id, first_name, last_name, food))
        conn.commit()

        menubtn = types.InlineKeyboardMarkup()
        menubtn1 = types.InlineKeyboardButton("Меню✅", callback_data='menu')
        menubtn.row(menubtn1)
        bot.send_message(message.chat.id,
                         'Спасибо за прохождение опроса.\nБудем тебя ждать 🤍', reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, 'Нажми на кнопку "Меню✅", чтобы узнать подробности мероприятия.',
                         reply_markup=menubtn)

    elif message.text == "Рыба":
        conn = sqlite3.connect('wed.sql')
        cur = conn.cursor()
        user_id, first_name, last_name, food = message.from_user.username, message.from_user.first_name, message.from_user.last_name, message.text
        cur.execute('INSERT INTO food (user_id, name, surname, food) VALUES (?, ?, ?, ?)',
                    (user_id, first_name, last_name, food))
        conn.commit()

        menubtn = types.InlineKeyboardMarkup()
        menubtn1 = types.InlineKeyboardButton("Меню✅", callback_data='menu')
        menubtn.row(menubtn1)
        bot.send_message(message.chat.id,
                         'Спасибо за прохождение опроса.\nБудем тебя ждать 🤍',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, 'Нажми на кнопку "Меню✅", чтобы узнать подробности мероприятия.',
                         reply_markup=menubtn)

    else:
        food1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        meat = types.KeyboardButton("Мясо")
        food1.row(meat)
        fish = types.KeyboardButton("Рыба")
        food1.row(fish)
        bot.send_message(message.chat.id, 'Пожалуйста, выбери корректный вариант', reply_markup=food1)
        bot.register_next_step_handler(message, db)



@bot.callback_query_handler(func=lambda callback: True)
def menu(callback):
    if callback.data == "menu":
        menu = types.InlineKeyboardMarkup()
        address = types.InlineKeyboardButton("Схема проезда", callback_data='address')
        menu.row(address)
        dresscode = types.InlineKeyboardButton("Дресс-код", callback_data='dresscode')
        menu.row(dresscode)
        timetable = types.InlineKeyboardButton("Расписание", callback_data='timetable')
        menu.row(timetable)
        music = types.InlineKeyboardButton("Заказать музыку", callback_data='music')
        menu.row(music)
        bot.send_message(callback.message.chat.id, 'Выбери любую категорию ниже', reply_markup=menu)

    elif callback.data == "address":
        back = types.InlineKeyboardMarkup()
        backbtn = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
        back.row(backbtn)
        bot.send_message(callback.message.chat.id,
                         '📍БербатовЪ\n Адрес: Молодёжная ул., 4А, село Ленино\n https://yandex.ru/maps/9/lipetsk/?ll=39.481968%2C52.524955&mode=poi&poi%5Bpoint%5D=39.481154%2C52.524884&poi%5Buri%5D=ymapsbm1%3A%2F%2Forg%3Foid%3D76397524392&z=18.21',
                         reply_markup=back)


    elif callback.data == "dresscode":
        back = types.InlineKeyboardMarkup()
        backbtn = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
        back.row(backbtn)
        pic = open('dresscode.png', 'rb')
        bot.send_photo(callback.message.chat.id, pic, reply_markup=back)


    elif callback.data == "timetable":
        back = types.InlineKeyboardMarkup()
        backbtn = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
        back.row(backbtn)
        pic = open('timetable.png', 'rb')
        bot.send_photo(callback.message.chat.id, pic, reply_markup=back)


    elif callback.data == "music":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Продолжить', callback_data='continue')
        markup.row(btn1)
        btn2 = types.InlineKeyboardButton('Отменить', callback_data='menu')
        markup.row(btn2)
        bot.send_message(callback.message.chat.id, "Нажми 'Продолжить', если ты хочешь заказать песню, которую хотел бы услышать на нашей свадьбе!\n Нажми 'Отменить', чтобы вернуться в меню",
                         reply_markup=markup)

    elif callback.data == 'continue':
        bot.send_message(callback.message.chat.id, "Напиши в ответном сообщении исполнителя и название песни⬇")
        bot.register_next_step_handler(callback.message, dbmusic)



def dbmusic(message):
    # ЗАПОЛНЯЕМ БД music

    conn = sqlite3.connect('wed.sql')
    cur = conn.cursor()
    user_id, first_name, last_name, music = message.from_user.username, message.from_user.first_name, message.from_user.last_name, message.text
    cur.execute('INSERT INTO music (user_id, name, surname, music) VALUES (?, ?, ?, ?)',
                (user_id, first_name, last_name, music))
    conn.commit()

    bot.send_message(781732345, music)
    back = types.InlineKeyboardMarkup()
    backbtn = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
    back.row(backbtn)
    bot.send_message(message.chat.id,
                     'Спасибо. Добавлено в плейлист💿', reply_markup=back)


bot.polling(none_stop=True)


