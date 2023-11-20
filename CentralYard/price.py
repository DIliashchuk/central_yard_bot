import telebot
from telebot import types
import pandas as pd
from io import BytesIO
import requests

token = '6979055272:AAHVUQ6wQbrlQuwd8Z5v1GuFy3IIF7Pb6lk'
bot = telebot.TeleBot(token)


def price_grandmaster(call):
    excel_link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRn9BG_Jqr6ouernSlnZGlKbV3159ZChYI_d_' \
                 'MlK-P0EkWVMxW5q-J5deHY5V-y3hQ-7_9DoGgLByLE/pub?output=xlsx'
    sheet_name = 'Grandmaster'
    response = requests.get(excel_link)
    excel_data = response.content
    df = pd.read_excel(BytesIO(excel_data), sheet_name=sheet_name)
    buttons_per_row = 1
    keyboard = types.InlineKeyboardMarkup(row_width=buttons_per_row)
    buttons = []

    for idx, row in df.iterrows():
        haircut_price = f"{row['Стрижка']}"
        callback_data = f'grand_master_price_{idx}'
        button = types.InlineKeyboardButton(haircut_price, callback_data=callback_data)
        buttons.append(button)

    for i in range(0, len(buttons), buttons_per_row):
        keyboard.add(*buttons[i:i + buttons_per_row])

    bot.send_message(call.message.chat.id, "Оберіть послугу:", reply_markup=keyboard)


def price_master(call):
    excel_link = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRn9BG_Jqr6ouernSlnZGlKbV3159ZChYI_d_' \
                 'MlK-P0EkWVMxW5q-J5deHY5V-y3hQ-7_9DoGgLByLE/pub?output=xlsx'
    sheet_name = 'Master'
    response = requests.get(excel_link)
    excel_data = response.content
    df = pd.read_excel(BytesIO(excel_data), sheet_name=sheet_name)
    buttons_per_row = 1
    keyboard = types.InlineKeyboardMarkup(row_width=buttons_per_row)
    buttons = []

    for idx, row in df.iterrows():
        haircut_price = f"{row['Стрижка']}"
        callback_data = f'master_price_{idx}'
        button = types.InlineKeyboardButton(haircut_price, callback_data=callback_data)
        buttons.append(button)

    for i in range(0, len(buttons), buttons_per_row):
        keyboard.add(*buttons[i:i + buttons_per_row])

    bot.send_message(call.message.chat.id, "Оберіть послугу:", reply_markup=keyboard)
