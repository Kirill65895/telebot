import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def startWork(message):
    tid = message.chat.id
    bot.send_message(tid, "Привет я Ботинок")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Меню" or message.text == "меню":
        bot.send_message(message.from_user.id,
                         "Привет, " + message.chat.first_name + "!")
        keyboardMenu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_z1 = telebot.types.KeyboardButton(text="Задание 1")
        key_z2 = telebot.types.KeyboardButton(text="Задание 2")
        key_z3 = telebot.types.KeyboardButton(text="Задание 3")
        key_z4 = telebot.types.KeyboardButton(text="Задание 4")
        key_z5 = telebot.types.KeyboardButton(text="Задание 5")

        keyboardMenu.add(key_z1, key_z2, key_z3, key_z4, key_z5)
        bot.send_message(message.from_user.id,
                         text='Меню',
                         reply_markup=keyboardMenu)

    if message.text == "Задание 1":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_test = telebot.types.KeyboardButton(text="Тестирование")
        key_web = telebot.types.KeyboardButton(text="Web")
        key_prog = telebot.types.KeyboardButton(text="Программирование")
        key_back = telebot.types.KeyboardButton(text="Назад")

        keyboard.add(key_test, key_web, key_prog)
        keyboard.add(key_back)

        bot.send_message(message.from_user.id,
                         text='Меню',
                         reply_markup=keyboard)

    if message.text == "Тестирование":
        bot.send_message(message.from_user.id, "Задание 1")
        bot.send_message(message.from_user.id, "Тестирование")

        bot.send_message(
            message.from_user.id,
            "https://neiros.ru/blog/code/testirovanie-i-7-osnovnykh-etapov-ego-provedeniya/"
        )
        bot.send_message(
            message.from_user.id,
            "https://blog.skillfactory.ru/testirovanie-chto-takoe/")
        bot.send_message(
            message.from_user.id,
            "https://tquality.ru/blog/vidy-testirovaniya-programmnogo-obespecheniya/"
        )

    if message.text == "Web":
        bot.send_message(message.from_user.id, "Задание 1")
        bot.send_message(message.from_user.id, "Web")

        bot.send_message(
            message.from_user.id,
            "https://skyeng.ru/magazine/wiki/it-industriya/chto-takoe-veb/")
        bot.send_message(message.from_user.id,
                         "https://lpgenerator.ru/blog/chto-takoe-web-20/")
        bot.send_message(
            message.from_user.id,
            "https://habr.com/ru/companies/geekbrains/articles/277957/")

    if message.text == "Программирование":
        bot.send_message(message.from_user.id, "Задание 1")
        bot.send_message(message.from_user.id, "Программирование")

        bot.send_message(
            message.from_user.id,
            "https://blog.skillfactory.ru/glossary/programmirovanie-eto/")
        bot.send_message(
            message.from_user.id,
            "https://skyeng.ru/magazine/wiki/it-industriya/chto-takoe-programmirovanie/"
        )
        bot.send_message(
            message.from_user.id,
            "https://practicum.yandex.ru/blog/s-chego-nachat-izuchenie-programmirovaniya/"
        )

    if message.text == "Назад":
        keyboardMenu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_z1 = telebot.types.KeyboardButton(text="Задание 1")
        key_z2 = telebot.types.KeyboardButton(text="Задание 2")
        key_z3 = telebot.types.KeyboardButton(text="Задание 3")
        key_z4 = telebot.types.KeyboardButton(text="Задание 4")
        key_z5 = telebot.types.KeyboardButton(text="Задание 5")

        keyboardMenu.add(key_z1, key_z2, key_z3, key_z4, key_z5)
        bot.send_message(message.from_user.id,
                         text='Меню',
                         reply_markup=keyboardMenu)

    if message.text == "Задание 2":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_zgol = telebot.types.KeyboardButton(text="Голосовое")
        key_back = telebot.types.KeyboardButton(text="Назад")

        keyboard.add(key_zgol)
        keyboard.add(key_back)

        bot.send_message(message.from_user.id,
                         text='Задание 2',
                         reply_markup=keyboard)

    if message.text == "Голосовое":
        bot.send_message(message.from_user.id, "Отправь голосовое сообщение!")

        @bot.message_handler(content_types=['voice'])
        def get_voice_messages(message):
            if (message.voice):
                bot.send_message(
                    message.from_user.id, message.chat.first_name + " " +
                    "Я глухой, можно погромче )))")

    if message.text == "Задание 3":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_zdialog = telebot.types.KeyboardButton(text="Диалог")
        key_back = telebot.types.KeyboardButton(text="Назад")

        keyboard.add(key_zdialog)
        keyboard.add(key_back)

        bot.send_message(message.from_user.id,
                         text='Задание 3',
                         reply_markup=keyboard)

    if message.text == "Диалог":
        bot.send_message(message.from_user.id, "Привет как тебя зовут?")
    if message.text == "Кирилл":
        bot.send_message(message.from_user.id,
                         "Привет Кирилл, а сколько тебе лет?")
    if message.text == "18":
        bot.send_message(message.from_user.id,
                         "Ого это круто, чем любишь заниматься?")
    if message.text == "Настольным теннисом":
        bot.send_message(message.from_user.id, "Это очень крутой вид спорта.")
    if message.text == "Пока":
        bot.send_message(message.from_user.id, "До встречи!")
        keyboardMenu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_z1 = telebot.types.KeyboardButton(text="Задание 1")
        key_z2 = telebot.types.KeyboardButton(text="Задание 2")
        key_z3 = telebot.types.KeyboardButton(text="Задание 3")
        key_z4 = telebot.types.KeyboardButton(text="Задание 4")
        key_z5 = telebot.types.KeyboardButton(text="Задание 5")

        keyboardMenu.add(key_z1, key_z2, key_z3, key_z4, key_z5)
        bot.send_message(message.from_user.id,
                         text='Меню',
                         reply_markup=keyboardMenu)

    if message.text == "Задание 4":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_zdel = telebot.types.KeyboardButton(text="Закрыть")
        key_back = telebot.types.KeyboardButton(text="Назад")

        keyboard.add(key_zdel)
        keyboard.add(key_back)

        bot.send_message(message.from_user.id,
                         text='Задание 4',
                         reply_markup=keyboard)

    if message.text == "Закрыть":
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id,
                         "Клавиатура убрана.",
                         reply_markup=markup)

    if message.text == "Задание 5":
        bot.send_message(message.from_user.id, "Не сделал")


bot.polling(none_stop=True, interval=0)
