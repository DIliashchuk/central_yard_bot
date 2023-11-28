import telebot
from telebot import types

token = '6979055272:AAHVUQ6wQbrlQuwd8Z5v1GuFy3IIF7Pb6lk'
bot = telebot.TeleBot(token)


def Kozachuk_Andriy(call):
    photo = open('photo/ANDREY KOZACHUK.jpeg', 'rb')
    bot.send_photo(call.message.chat.id, photo)
    bot.send_message(call.message.chat.id, 'Усім Привіт!\nМене звати Андрій і я більше ніж 5 років роблю справжні '
                                           'чоловічі зачіски.\nНе буду приховувати, я дуже кохаю свою роботу, для '
                                           'мене це перш за все простір для творчості.\nЯ обожнюю нові знайомства та '
                                           'спілкування з цікавими людьми.\nПриходь - познайомимось! Буду '
                                           'чекати саме на тебе\n\nМій Instagram: '
                                           'https://instagram.com/kez_barber\n\nДавай не вагайся, буду не '
                                           'Андрійом, а Кезом для тебе :)\n\nЗапис тут - /appointment')
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton("Прайс ✂️ Прайс ✂️ Прайс ✂️", callback_data='price_grandmaster')
    keyboard.add(button)
    bot.send_message(call.message.chat.id, 'Цікавлять ціни? Клацай сюди ⬇️', reply_markup=keyboard)


def Munno_Nikola(call):
    photo = open('photo/MUNNO NIKOLA.jpeg', 'rb')
    bot.send_photo(call.message.chat.id, photo)
    bot.send_message(call.message.chat.id, "Усім Привіт!\nМене звуть Нікола, і від юності мене зачаровувала вміння "
                                           "створювати красу простими рухами. Навіть у дитинстві, я віддавав "
                                           "перевагу дивитися на зачіски професійних футболістів, а не на гру "
                                           "вражаючись цим як мистецтвом. Це було просто дивовижно! Якщо ти "
                                           "спортсмен, в мене є кілька варіантів зачіски для тебе, щоб виділитися "
                                           "на полі. А якщо спорт - це не твоє, давайте створимо образ, "
                                           "який вражатиме щодня, у буденному житті."
                                           "\n\nМій "
                                           'Instagram: https://instagram.com/munnonikola/\n\nЗалюбки зроблю '
                                           'тобі топ зачіску :)\n\nЗапис тут - /appointment')
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton("Прайс ✂️ Прайс ✂️ Прайс ✂️", callback_data='price_grandmaster')
    keyboard.add(button)
    bot.send_message(call.message.chat.id, 'Цікавлять ціни? Клацай сюди ⬇️', reply_markup=keyboard)


def Sergiy_Zaika(call):
    photo = open('photo/SERGEY ZAIKA.jpeg', 'rb')
    bot.send_photo(call.message.chat.id, photo)
    bot.send_message(call.message.chat.id, "Усім Привіт!\nМене звуть Сергій. \nУ своїй роботі я руками творю красу, "
                                           "яка перетворює вас, надаючи стиль і самовираження. Якщо ви хочете "
                                           "виглядати як професійний спортсмен або знаменитість, або вам "
                                           "просто потрібен оновлений образ, я допоможу вам з цим.\n\n"
                                           "Мій Instagram: https://instagram.com/_iamf"
                                           "reesoul/\n\nРозуміюсь на твоїх потребах, тож давай зробимо красиво :)"
                                           "\n\nЗапис тут - /appointment")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton("Прайс ✂️ Прайс ✂️ Прайс ✂️", callback_data='price_grandmaster')
    keyboard.add(button)
    bot.send_message(call.message.chat.id, 'Цікавлять ціни? Клацай сюди ⬇️', reply_markup=keyboard)


def Viktor_Kozlovskyi(call):
    photo = open('photo/VICTOR KOZLOVSKY.jpeg', 'rb')
    bot.send_photo(call.message.chat.id, photo)
    bot.send_message(call.message.chat.id, "Усім Привіт!\nМене звуть Віктор. \nЯ - барбер з багаторічним досвідом. "
                                           "Моя мета - зробити ваш вигляд виразнішим і красивішим. Чи хочете ви "
                                           "стрижку, яка підкреслить вашу індивідуальність або вибухніть "
                                           "креативністю - я допоможу вам створити образ, який вам подобається.\n\n"
                                           "Мій Instagram: https://instagram.com/kozlovskyi"
                                           "_viktor/\n\n Ти знаэшь де я тебе чекаю :)\n\nЗапис тут - /appointment")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton("Прайс ✂️ Прайс ✂️ Прайс ✂️", callback_data='price_grandmaster')
    keyboard.add(button)
    bot.send_message(call.message.chat.id, 'Цікавлять ціни? Клацай сюди ⬇️', reply_markup=keyboard)


def Artem_Scherban(call):
    photo = open('photo/ARTYOM SHCHERBAN.jpeg', 'rb')
    bot.send_photo(call.message.chat.id, photo)
    bot.send_message(call.message.chat.id, "Усім Привіт! \nМене звати Артем. \nЯ - барбер з досвідом та відчуттям "
                                           "стилю. Якщо вам потрібна якісна стрижка чи креативне втілення задуму, "
                                           "я завжди готовий до творчого спілкування. Надам вам комфорт і креативність "
                                           "в кожній деталі вашого образу.\n\n"
                                           "Мій Instagram: https://instagram.com/temaa__5/"
                                           "\n\nЗапис тут - /appointment")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton("Прайс ✂️ Прайс ✂️ Прайс ✂️", callback_data='price_grandmaster')
    keyboard.add(button)
    bot.send_message(call.message.chat.id, 'Цікавлять ціни? Клацай сюди ⬇️', reply_markup=keyboard)


def Dmytro_Zhurovets(call):
    photo = open('photo/DMYYRO ZHUROVETS.jpeg', 'rb')
    bot.send_photo(call.message.chat.id, photo)
    bot.send_message(call.message.chat.id, "Усім Привіт! \nМене звати Дмитро. \nЯ - барбер із великим бажанням "
                                           "створювати стильні образи. Моє завдання - зробити кожного клієнта "
                                           "задоволеним своїм виглядом та допомогти вам відчувати себе комфортно "
                                           "і впевнено.\n\n"
                                           "Мій Instagram: https://instagram.com/mr.zghurovets/"
                                           "\n\nЗапис тут - /appointment")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton("Прайс ✂️ Прайс ✂️ Прайс ✂️", callback_data='price_master')
    keyboard.add(button)
    bot.send_message(call.message.chat.id, 'Цікавлять ціни? Клацай сюди ⬇️', reply_markup=keyboard)


def Denis_Isaenko(call):
    photo = open('photo/DENYS ISAENKO.jpeg', 'rb')
    bot.send_photo(call.message.chat.id, photo)
    bot.send_message(call.message.chat.id, "Усім Привіт! \nМене звати Денис.\nЯ - барбер з великим бажанням зробити"
                                           "кожного клієнта щасливим. Моя мета - забезпечити вам відчуття комфорту "
                                           "та задоволення від кожного візиту до мене. Чи це стрижка, чи це гоління, "
                                           "я завжди тут, щоб задовольнити ваші потреби.\n\n"
                                           "Мій Instagram: https://instagram.com/_______dddddddddd________/"
                                           "\n\nЗапис тут - /appointment")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton("Прайс ✂️ Прайс ✂️ Прайс ✂️", callback_data='price_master')
    keyboard.add(button)
    bot.send_message(call.message.chat.id, 'Цікавлять ціни? Клацай сюди ⬇️', reply_markup=keyboard)
