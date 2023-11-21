import telebot
from telebot import types
import pandas as pd
from io import BytesIO
import requests
from price import price_grandmaster, price_master
from barber_info import Kozachuk_Andriy, Munno_Nikola, Sergiy_Zaika, Viktor_Kozlovskyi, Artem_Scherban, \
    Dmytro_Zhurovets, Denis_Isaenko
from appointment import book_staff, book_dates

token = '6979055272:AAHVUQ6wQbrlQuwd8Z5v1GuFy3IIF7Pb6lk'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Доброго дня, {message.from_user.first_name}!\n'
                                      f'Зліва знизу можете побачити меню з усіма командами\n⬇️')


@bot.message_handler(commands=['price'])
def price(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton("Вартість стрижки Cтаршогу Майстру", callback_data='price_grandmaster')
    button_2 = types.InlineKeyboardButton("Вартість стрижки Майстру", callback_data='price_master')
    keyboard.add(button, button_2)
    bot.send_message(message.chat.id, "Дізнатись вартість💵\n\n<u><b>Старший Мастер:</b></u>\nМунно Нікола\n"
                                      "Козловський Віктор\nАртем Щербань\nСергій Заїка\nКозачук Андрій"
                                      "\n\n<u><b>Майстер</b></u>:\nДенис Ісаєнко\nДмитро Жировець\n\n"
                                      "Ви можете подивитись більш делатальну \nінформацію про барберів у меню \n"
                                      "команд 'Інфомарція про барбера' \nабо натисніть - /barber_info",
                     reply_markup=keyboard, parse_mode='HTML')


@bot.message_handler(commands=['barber_info'])
def barber_info(message):
    photo_1 = open('photo/Козачук + Мунно.jpg', 'rb')
    bot.send_photo(message.chat.id, photo_1)
    keyboard_1 = types.InlineKeyboardMarkup(row_width=2)
    button = types.InlineKeyboardButton("Козачук Андрій", callback_data='Kozachuk_Andriy')
    button_2 = types.InlineKeyboardButton("Мунно Нікола", callback_data='Munno_Nikola')
    keyboard_1.add(button, button_2)
    bot.send_message(message.chat.id, "Старший майстер:", reply_markup=keyboard_1)

    photo_2 = open('photo/Заїка + Козловский .jpg', 'rb')
    bot.send_photo(message.chat.id, photo_2)
    keyboard_2 = types.InlineKeyboardMarkup(row_width=2)
    button_3 = types.InlineKeyboardButton("Заїка Cергій", callback_data='Sergiy_Zaika')
    button_4 = types.InlineKeyboardButton("Козловський Віктор", callback_data='Viktor_Kozlovskyi')
    keyboard_2.add(button_3, button_4)
    bot.send_message(message.chat.id, "Старший майстер:", reply_markup=keyboard_2)

    photo_3 = open('photo/Щербань.jpg', 'rb')
    bot.send_photo(message.chat.id, photo_3)
    keyboard_3 = types.InlineKeyboardMarkup(row_width=2)
    button_6 = types.InlineKeyboardButton("Артем Щербань", callback_data='Artem_Scherban')
    keyboard_3.add(button_6)
    bot.send_message(message.chat.id, "Старший майстер:", reply_markup=keyboard_3)

    photo_4 = open('photo/Журовець + Ісаєнко.jpg', 'rb')
    bot.send_photo(message.chat.id, photo_4)
    keyboard_4 = types.InlineKeyboardMarkup(row_width=2)
    button_7 = types.InlineKeyboardButton("Дмитро Жировець", callback_data='Dmytro_Zhurovets')
    button_8 = types.InlineKeyboardButton("Денис Ісаєнко", callback_data='Denis_Isaenko')
    keyboard_4.add(button_7, button_8)
    bot.send_message(message.chat.id, "Майстер:", reply_markup=keyboard_4)


@bot.message_handler(commands=['appointment'])
def make_appointment(message):
    staff_list = book_staff()
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(name, callback_data=f'staff_id_{staff_id}') for name, staff_id in
               staff_list.items()]
    keyboard.add(*buttons)

    bot.send_message(message.chat.id, "Выберите сотрудника", reply_markup=keyboard)

    bot.register_next_step_handler(message, handle_chosen_staff)


@bot.callback_query_handler(func=lambda call: call.data.startswith('staff_id_'))
def handle_chosen_staff(call):
    staff_list = book_staff()
    staff_id = call.data.split('_')[-1]
    chosen_staff = next((name for name, id_ in staff_list.items() if id_ == int(staff_id)), None)
    bot.send_message(call.message.chat.id, f"Выбран сотрудник: {chosen_staff}, ID: {staff_id}")
    booking_dates(call, staff_id)


def booking_dates(call, staff_id):
    booking_date = book_dates()
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    buttons = [
        types.InlineKeyboardButton(date, callback_data=f"date_{date}") for date in booking_date
    ]

    keyboard.add(*buttons)
    bot.send_message(call.message.chat.id, "Выберите дату", reply_markup=keyboard)
    bot.register_next_step_handler(call, handle_booking_dates, staff_id)


@bot.callback_query_handler(func=lambda call: call.data.startswith('date_'))
def handle_booking_dates(call, staff_id):
    selected_date = call.data.split('_')[-1]  # Получаем выбранную дату из callback_data

    bot.send_message(call.message.chat_id, f"Выбранная дата: {selected_date}")







@bot.message_handler(commands=['contact'])
def contact(message):
    bot.send_message(message.chat.id, "Шановний клієнт!\nМи знаходимось за адресою: м.КиЇв, вул.Хрещатик "
                                      "46Б\n\nКонтактний номер телефону: +38 (068) 46-46-46-0\n\n"
                                      "Геолокація: https://maps.app.goo.gl/kWHjA4NDz7Y3kfJz6")


@bot.message_handler(commands=['social_media'])
def social_media(message):
    bot.send_message(message.chat.id, "Приєднуйся до наших соціальних мереж та слідкуй за новинами, "
                                      "трендами та цікавими пропозиціями від наших хлопців #centralyard\n\n<u><b>Наш "
                                      "Website:</b></u> https://centralyard.com.ua/\n\n<u><b>Наш Instagram:</b></u> "
                                      "https://www.instagram.com/central.yard46/\n\n<u><b>Наш TikTok:</b></u> "
                                      "https://www.tiktok.com/@centralyardbarber\n\nШвидше долучайся "
                                      "та отримуй максимум задоволення від наших талановитих барберів",
                     parse_mode='HTML')


@bot.callback_query_handler(func=lambda call: call.data.startswith('grand_master_price_'))
def handle_price_grandmaster(call):
    index = int(call.data.split('_')[-1])
    excel_link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRn9BG_Jqr6ouernSlnZGlKbV3159ZChYI_d_' \
                 'MlK-P0EkWVMxW5q-J5deHY5V-y3hQ-7_9DoGgLByLE/pub?output=xlsx'
    sheet_name = 'Grandmaster'
    response = requests.get(excel_link)
    excel_data = response.content
    df = pd.read_excel(BytesIO(excel_data), sheet_name=sheet_name)
    if index < len(df):
        row = df.iloc[index]
        haircut = row['Стрижка']
        price = row['Ціна']
        worktime = row['Тривалість']
        bot.send_message(call.message.chat.id, f"<u><b>Ви обрали:</b></u> {haircut}\n<u><b>Вартісь складає:</b></u> "
                                               f"{price} грн.\n<u><b>Тривалість стрижки:</b></u> "
                                               f"{worktime}", parse_mode='HTML')
    else:
        bot.send_message(call.message.chat.id, "Помилка: Немає інформації для цього індексу")


@bot.callback_query_handler(func=lambda call: call.data.startswith('master_price_'))
def handle_price_grandmaster(call):
    index = int(call.data.split('_')[-1])
    excel_link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRn9BG_Jqr6ouernSlnZGlKbV3159ZChYI_d_' \
                 'MlK-P0EkWVMxW5q-J5deHY5V-y3hQ-7_9DoGgLByLE/pub?output=xlsx'
    sheet_name = 'Master'
    response = requests.get(excel_link)
    excel_data = response.content
    df = pd.read_excel(BytesIO(excel_data), sheet_name=sheet_name)
    if index < len(df):
        row = df.iloc[index]
        haircut = row['Стрижка']
        price = row['Ціна']
        worktime = row['Тривалість']
        bot.send_message(call.message.chat.id, f"<u><b>Ви обрали:</b></u> {haircut}\n<u><b>Вартісь складає:</b></u> "
                                               f"{price} грн.\n<u><b>Тривалість стрижки:</b></u> "
                                               f"{worktime}", parse_mode='HTML')
    else:
        bot.send_message(call.message.chat.id, "Помилка: Немає інформації для цього індексу")


functions = {
    'price_grandmaster': price_grandmaster,
    'price_master': price_master,
    'Kozachuk_Andriy': Kozachuk_Andriy,
    'Munno_Nikola': Munno_Nikola,
    'Sergiy_Zaika': Sergiy_Zaika,
    'Viktor_Kozlovskyi': Viktor_Kozlovskyi,
    'Artem_Scherban': Artem_Scherban,
    'Dmytro_Zhurovets': Dmytro_Zhurovets,
    'Denis_Isaenko': Denis_Isaenko,
    'barber_info': barber_info
}


@bot.callback_query_handler(func=lambda call: True)
def handle_action(call):
    if call.data in functions:
        function_to_run = functions[call.data]
        function_to_run(call)


bot.polling(none_stop=True, interval=0)