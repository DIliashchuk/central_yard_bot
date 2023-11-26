import sqlite3
import telebot
from telebot import types
import pandas as pd
from io import BytesIO
import requests
from price import price_grandmaster, price_master
from barber_info import Kozachuk_Andriy, Munno_Nikola, Sergiy_Zaika, Viktor_Kozlovskyi, Artem_Scherban, \
    Dmytro_Zhurovets, Denis_Isaenko
from appointment import book_staff, book_dates, services, finallys, book_time


token = '6979055272:AAHVUQ6wQbrlQuwd8Z5v1GuFy3IIF7Pb6lk'
bot = telebot.TeleBot(token)

flag = False
staff_category_map = {
    '227400': 10593304,
    '250724': 10593304,
    '869054': 10593304,
    '227395': 10593304,
    '194619': 10593304,
    '2119274': 1100495,
    '2119275': 1100495
}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Доброго дня, {message.from_user.first_name}!\n'
                                      f'Зліва знизу можете побачити меню зі всіма функціями\n⬇️')


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
    photo_1 = open('photo/Козачук + Мунно.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo_1)
    keyboard_1 = types.InlineKeyboardMarkup(row_width=2)
    button = types.InlineKeyboardButton("Козачук Андрій", callback_data='Kozachuk_Andriy')
    button_2 = types.InlineKeyboardButton("Мунно Нікола", callback_data='Munno_Nikola')
    keyboard_1.add(button, button_2)
    bot.send_message(message.chat.id, "Старший майстер:", reply_markup=keyboard_1)

    photo_2 = open('photo/Заїка + Козловский .jpeg', 'rb')
    bot.send_photo(message.chat.id, photo_2)
    keyboard_2 = types.InlineKeyboardMarkup(row_width=2)
    button_3 = types.InlineKeyboardButton("Заїка Cергій", callback_data='Sergiy_Zaika')
    button_4 = types.InlineKeyboardButton("Козловський Віктор", callback_data='Viktor_Kozlovskyi')
    keyboard_2.add(button_3, button_4)
    bot.send_message(message.chat.id, "Старший майстер:", reply_markup=keyboard_2)

    photo_3 = open('photo/Щербань.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo_3)
    keyboard_3 = types.InlineKeyboardMarkup(row_width=2)
    button_6 = types.InlineKeyboardButton("Артем Щербань", callback_data='Artem_Scherban')
    keyboard_3.add(button_6)
    bot.send_message(message.chat.id, "Старший майстер:", reply_markup=keyboard_3)

    photo_4 = open('photo/Журовець + Ісаєнко.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo_4)
    keyboard_4 = types.InlineKeyboardMarkup(row_width=2)
    button_7 = types.InlineKeyboardButton("Дмитро Жировець", callback_data='Dmytro_Zhurovets')
    button_8 = types.InlineKeyboardButton("Денис Ісаєнко", callback_data='Denis_Isaenko')
    keyboard_4.add(button_7, button_8)
    bot.send_message(message.chat.id, "Майстер:", reply_markup=keyboard_4)


@bot.message_handler(commands=['appointment'])
def check_flag(message):
    global flag
    my_personal_id = message.from_user.id
    conn = sqlite3.connect("register.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM registration")
    result = cursor.fetchall()
    db_user_ids = [row[0] for row in result]

    if my_personal_id in db_user_ids:
        flag = True
        make_appointment(message)
    else:
        registration(message)

    conn.close()


def registration(message):
    bot.send_message(message.chat.id, "Ви вперше зайшли до онлайн запису через нашого бота, просимо Вас "
                                      "заповнити інформацію\nДанну інформацію треба зповнити лише один раз, "
                                      "наступного разу система автоматично вас ідентифікує.\n\n"
                                      "Будь-ласка, введіть ваше ім'я (бажано повне): ")
    bot.register_next_step_handler(message, registration_name)


def registration_name(message):
    name = message.text
    if name.startswith('/'):
        bot.send_message(message.chat.id, 'Ви вийшли з реєстраціії.\n\nЗліва знизу можете побачити '
                                          'меню зі всіма функціями\n⬇️')
        return
    bot.send_message(message.chat.id, 'Будь-ласка, введіть ваш мобільний номер телефону: ')
    bot.register_next_step_handler(message, registration_phone, name)


def registration_phone(message, name):
    phone = message.text
    if phone.startswith('/'):
        bot.send_message(message.chat.id, 'Ви вийшли з реєстраціії.\n\nЗліва знизу можете побачити '
                                          'меню зі всіма функціями\n⬇️')
        return
    bot.send_message(message.chat.id, 'Будь-ласка, введіть вашу електронну пошту: ')
    bot.register_next_step_handler(message, registration_mail, name, phone)


def registration_mail(message, name, phone):
    mail = message.text
    if mail.startswith('/'):
        bot.send_message(message.chat.id, 'Ви вийшли з реєстраціії.\n\nЗліва знизу можете побачити '
                                          'меню зі всіма функціями\n⬇️')
        return
    personal_id = message.from_user.id
    conn = sqlite3.connect("register.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO registration (id, name, phone, email) VALUES (?, ?, ?, ?)",
                   (personal_id, name, phone, mail))

    conn.commit()
    conn.close()
    make_appointment(message)


def make_appointment(message):
    staff_list = book_staff()
    my_personal_id = message.from_user.id
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(name, callback_data=f'staff_id_{staff_id}_{my_personal_id}')
               for name, staff_id in staff_list.items()]
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, "Оберіть Барбера, до якого ви бажаєте записатись", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith('staff_id_'))
def handle_chosen_staff(call):
    staff_id = call.data.split('_')[-2]
    my_personal_id = call.data.split('_')[-1]
    staff_list = book_staff()
    chosen_staff = next((name for name, id_ in staff_list.items() if id_ == int(staff_id)), None)
    bot.send_message(call.message.chat.id, f"Обран Барбер ✂️: {chosen_staff}")
    book_services(call, staff_id, chosen_staff, my_personal_id)


def book_services(call, staff_id, chosen_staff, my_personal_id):
    booking_services = services(staff_category_map.get(staff_id))
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton(name, callback_data=f'service_id_{staff_id}_{service_id}_{my_personal_id}')
        for name, service_id in booking_services.items()
    ]
    keyboard.add(*buttons)

    bot.send_message(call.message.chat.id, "Оберіть послугу барбершопу", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith('service_id_'))
def handle_book_services(call):
    data_parts = call.data.split('_')
    staff_id, service_id, my_personal_id = data_parts[2:5]

    booking_services = services(staff_category_map.get(staff_id))
    service_name = next((name for name, id_ in booking_services.items() if id_ == int(service_id)), None)

    bot.send_message(call.message.chat.id, f"Ви обрали послугу: {service_name}")
    booking_dates(call, staff_id, service_id, my_personal_id, service_name)


def booking_dates(call, staff_id, service_id, my_personal_id, service_name):
    booking_date = book_dates(staff_id)
    if not booking_date:
        bot.send_message(call.message.chat.id, "Извините, нет доступных дат.")
        return
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    buttons = [
        types.InlineKeyboardButton(date, callback_data=f"date_{staff_id}_{date}_{my_personal_id}_{service_id}")
        for date in booking_date
    ]
    keyboard.add(*buttons)
    bot.send_message(call.message.chat.id, "Оберіть дату 📅", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith('date_'))
def handle_selected_date(call):
    print(call.data)
    selected_date = call.data.split('_')[-3]
    staff_id = call.data.split('_')[-4]
    my_personal_id = call.data.split('_')[-2]
    service_id = call.data.split('_')[-1]
    bot.send_message(call.message.chat.id, f"Обрана дата: {selected_date}")
    booking_times(call, selected_date, staff_id, my_personal_id, service_id)


def booking_times(call, selected_date, staff_id, my_personal_id, service_id):
    book_list = book_time(staff_id, selected_date)
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    buttons = [
        types.InlineKeyboardButton(time, callback_data=f'time_{staff_id}_{selected_date}_{time}_{my_personal_id}_'
                                                       f'{service_id}')
        for time in book_list
    ]
    keyboard.add(*buttons)
    bot.send_message(call.message.chat.id, "Оберіть час ⏰", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith('time_'))
def handle_selected_time(call):
    data_parts = call.data.split('_')
    selected_time = data_parts[-3]
    staff_id = data_parts[-5]
    selected_date = data_parts[-4]
    my_personal_id = call.data.split('_')[-2]
    service_id = call.data.split('_')[-1]
    bot.send_message(call.message.chat.id, f"Обран час: {selected_time}")
    finally_info_book(call, staff_id, selected_date, selected_time, my_personal_id, service_id)


def finally_info_book(call, staff_id, selected_date, selected_time, my_personal_id, service_id):
    staff_list = book_staff()
    chosen_staff = next((name for name, id_ in staff_list.items() if id_ == int(staff_id)), None)
    booking_services = services(staff_category_map.get(staff_id))
    service_name = next((name for name, id_ in booking_services.items() if id_ == int(service_id)), None)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = types.InlineKeyboardButton('Підтвердити запис', callback_data=f'book_yes_{staff_id}_{service_id}_'
                                                                            f'{selected_date}_{my_personal_id}_'
                                                                            f'{selected_time}')
    buttons_1 = types.InlineKeyboardButton('Скасувати записа', callback_data='book_no')
    keyboard.add(buttons, buttons_1)
    bot.send_message(call.message.chat.id, f"Перевірте данні для запису:\n\nВи обрали барбера: {chosen_staff}\n"
                                           f"Ви обрали дату візиту: {selected_date}\nВи обрали час: {selected_time}\n"
                                           f"Ви обрали послугу: {service_name}\n\nЯкщо все вірно,"
                                           f" просимо нажати Так для підтвердження", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith('book_yes'))
def booking_yes(call):
    staff_id = call.data.split('_')[-5]
    service_id = call.data.split('_')[-4]
    selected_date = call.data.split('_')[-3]
    my_personal_id = call.data.split('_')[-2]
    selected_time = call.data.split('_')[-1]
    conn = sqlite3.connect("register.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, phone, email FROM registration WHERE id = ?", (my_personal_id,))
    user_info = cursor.fetchone()
    name, phone, email = user_info
    success = finallys(service_id, staff_id, selected_date, selected_time, name, phone, email)
    if success:
        bot.send_message(call.message.chat.id, "Запис пройшов успішно! ")
    else:
        bot.send_message(call.message.chat.id, "Вибачте, сталась помилка, спробуйте ще раз або зателефонуйте "
                                               "до нашего барбера: \n+38(068)46-46-46-0\n\nСкоріш за все ця помилка "
                                               "звя'язана з тим, що йде конфлікт часу, тому уточнюйте час за телефоном "
                                               "або спробуйте обрати інший час")

    conn.close()


@bot.callback_query_handler(func=lambda call: call.data.startswith('book_no'))
def booking_no(call):
    bot.send_message(call.message.chat.id, 'Ви відмінили запис\nЗліва знизу можете побачити меню зі всіма '
                                           'функціями\n⬇️')
    return


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
        bot.send_message(call.message.chat.id, f"<u><b>Ви обрали послугу:</b></u> {haircut}\n<u><b>Вартісь "
                                               f"складає:</b></u>  {price} грн.\n<u><b>Тривалість стрижки:</b></u> "
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
        bot.send_message(call.message.chat.id, f"<u><b>Ви обрали послугу:</b></u> {haircut}\n<u><b>Вартісь "
                                               f"складає:</b></u> {price} грн.\n<u><b>Тривалість стрижки:</b></u> "
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