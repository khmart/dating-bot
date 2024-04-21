import telebot
import random
import json
import datetime
from telebot.types import LabeledPrice, ShippingOption
from flask import Flask, request



bot = telebot.TeleBot('your_token')
provider_token = 'test:test'

bot.set_webhook()


# token = '1487009834:AAHK9IRhhoMqgrfWTVM2Dj47jG9A_ZkV78s'
# secret = '2a746qx5-19d4-4ab6-b83f-o360c1251f17'
# url = 'https://MaraGul.pythonanywhere.com/' + secret
#
# bot = telebot.TeleBot(token, threaded=False)
# bot.remove_webhook()
# bot.set_webhook(url=url)
#
# app = Flask(__name__)
#
# @app.route('/'+secret, methods=['POST'])
# def webhook():
#     update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
#     bot.process_new_updates([update])
#     #return 'Hello from Flask!'
#     return 'ok', 200

prices = [LabeledPrice(label='Цена', amount=10000), LabeledPrice('Комиссия', 0)]

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row('Начать')

keyboard_main = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_main.row('Познакомиться')
keyboard_main.row('Отношения без обязательств')
keyboard_main.row('Спонсорство')
# keyboard_main.row('Донаты')

key_stop = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
key_stop.row('остановить')

key_sex = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
key_sex.row('Парень', 'Девушка')
key_sex.row('остановить')

key_sex2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
key_sex2.row('Парня', 'Девушку')
key_sex2.row('остановить')

key_18 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
key_18.row('Да, потверждаю', 'Мне нет 18')

key_step = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
key_step.row('Искать дальше', 'Покинуть чат')

key_feedback = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
key_feedback.row('Не нравится, не буду пользоваться')
key_feedback.row('Мне нравится, воспользуюсь еще')
key_feedback.row('Не нашел, но все равно прикольно')
key_feedback.row('Не знаю')


reg_user = {}
pay_user = {}
free_user = {}

user_choice = {}
user_name_spisok = {}
user_age = {}
user_city = {}
user_sex = {}
user_sex_s = {}
user_status = {}
user_session = {}
user_about = {}
para = {}
chetchik_poisk = {}
chetchik_find = {}
feedback_user = {}

# with open('free_user_list.txt', 'r') as f:
#     try:
#         free_user = json.load(f)
#     # if the file is empty the ValueError will be thrown
#     except ValueError:
#         pass

# with open('pay_user.txt', 'r') as f:
#     try:
#         pay_user = json.load(f,parse_int=True)
#     # if the file is empty the ValueError will be thrown
#     except ValueError:
#         pass
#
# with open('reg_list.txt', 'r') as f:
#     try:
#         reg_user = json.load(f)
#     # if the file is empty the ValueError will be thrown
#     except ValueError:
#         pass


@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, 'Кнопка НАЧАТЬ - запустить бота.', reply_markup=keyboard)
    get_free(message.chat.id)

@bot.message_handler(content_types=['photo'])
def get_photo_messages(message):
    if message.from_user.id in reg_user or str(message.from_user.id) in reg_user:
        if message.from_user.id in user_status:
            if user_status[message.from_user.id] == True:
                if message.from_user.id in para:
                    # photo_id = message.photo.file_id
                    # file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
                    # downloaded_file = bot.download_file(file_info.file_path)
                    # imageFile = '/tmp/photo.jpg'
                    # img = open(downloaded_file, 'rb')
                    bot.send_photo(para[message.from_user.id], message.photo[len(message.photo) - 1].file_id)
                    # bot.send_photo(para[message.from_user.id], bot.get_user_profile_photos(para[message.from_user.id]))
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.message_handler(content_types=['voice'])
def get_voice_messages(message):
    if message.from_user.id in reg_user or str(message.from_user.id) in reg_user:
        if message.from_user.id in user_status:
            if user_status[message.from_user.id] == True:
                if message.from_user.id in para:
                    bot.send_voice(para[message.from_user.id],  message.voice.file_id)

        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.message_handler(content_types=['video'])
def get_video_messages(message):
    if message.from_user.id in reg_user or str(message.from_user.id) in reg_user:
        if message.from_user.id in user_status:
            if user_status[message.from_user.id] == True:
                if message.from_user.id in para:
                    bot.send_video(para[message.from_user.id],  message.video.file_id)

        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.message_handler(content_types=['sticker'])
def get_stiker_messages(message):
    if message.from_user.id in reg_user or str(message.from_user.id) in reg_user:
        if message.from_user.id in user_status:
            if user_status[message.from_user.id] == True:
                if message.from_user.id in para:
                    bot.send_sticker(para[message.from_user.id], message.sticker.file_id)

        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text.lower() == 'начать' and message.text != None:
        bot.send_message(message.from_user.id, 'Начнем искать', reply_markup=keyboard_main)
        reg_user[str(message.from_user.id)] = {'first_name': message.from_user.first_name}
        reg_user[str(message.from_user.id)]['last_name'] = message.from_user.last_name
        reg_user[str(message.from_user.id)]['username'] = message.from_user.username
        with open('reg_list.txt', 'w') as f:
            json.dump(reg_user, f)
    elif message.text.lower() == 'познакомиться':
        registracia_user(message)
        # get_free(message.from_user.id)
        bot.send_message(message.from_user.id, 'Здесь можно познакомиться, общаться и договориться о встрече')
        bot.send_message(message.from_user.id, 'Укажите ваше ИМЯ', reply_markup=key_stop)
        user_choice[message.from_user.id] = {'choice': 'meeting'}
        bot.register_next_step_handler(message, get_name_user)
    elif message.text.lower() == 'отношения без обязательств':
        registracia_user(message)
        # get_free(message.from_user.id)
        active_free(message.from_user.id)
        # if message.from_user.id in pay_user or message.from_user.id in free_user or str(message.from_user.id) in pay_user or str(message.from_user.id) in free_user:
        bot.send_message(message.from_user.id, 'Найди партнера для быстрых встреч')
        # bot.send_message(message.from_user.id, 'Укажите ваше ИМЯ')
        # user_choice[message.from_user.id] = {'choice': 'sex'}
        # bot.register_next_step_handler(message, get_name_user)
        bot.send_message(message.from_user.id, 'Вы потверждаете, что вам больше 18 лет?', reply_markup=key_18)
        bot.register_next_step_handler(message, get_user_sex)
        # else:
        #     bot.send_message(message.from_user.id, 'Срок действия бесплатного доступа закончился, доступно для платных пользователей')

    elif message.text.lower() == 'спонсорство':
        registracia_user(message)
        # get_free(message.from_user.id)
        active_free(message.from_user.id)
        # if message.from_user.id in pay_user or message.from_user.id in free_user or str(message.from_user.id) in pay_user or str(message.from_user.id) in free_user:
        bot.send_message(message.from_user.id, 'Попробуй найти спонсора')
        # bot.send_message(message.from_user.id, 'Укажите ваше ИМЯ')
        # user_choice[message.from_user.id] = {'choice': 'money'}
        # bot.register_next_step_handler(message, get_name_user)
        bot.send_message(message.from_user.id, 'Вы потверждаете, что вам больше 18 лет?', reply_markup=key_18)
        bot.register_next_step_handler(message, get_user_money)
        # else:
        #     bot.send_message(message.from_user.id, 'Срок действия бесплатного доступа закончился, доступно для платных пользователей')
    elif message.text.lower() == 'донаты':
        bot.send_message(message.chat.id,
                         "Сейчас вы получите счет."
                         " Тестовая оплата."
                         " Используйте этот номер карты : `4242 4242 4242 4242`", parse_mode='Markdown')
        bot.send_invoice(
            chat_id=message.chat.id,
            title='Покупка премиум подписки',
            description='Вы совершите транзакцию.',
            invoice_payload='true',
            provider_token=provider_token,
            start_parameter='true',
            currency='rub',
            prices=prices)

    elif message.text.lower() == 'искать дальше':
        if message.from_user.id in user_status:
            if message.from_user.id in para:
                user_id = para[message.from_user.id]
                del para[message.from_user.id]
                del para[user_id]
                user_session[user_id] = False
                bot.send_message(user_id,
                                 "Пользователь " + user_name_spisok[message.from_user.id]['name'].upper() + " покинул(а) чат.")
            user_session[message.from_user.id] = False
            def_start(message.from_user.id)
        else:
            bot.send_message(message.from_user.id, 'Нужно выбрать категорию поиска', reply_markup=keyboard_main)
    elif message.text.lower() == 'покинуть чат':
        # delete_user(message.from_user.id)
        if message.from_user.id in user_status:
            if message.from_user.id in para:
                user_id = para[message.from_user.id]
                del para[message.from_user.id]
                del para[user_id]
                user_session[user_id] = False
                bot.send_message(user_id,
                                 "Пользователь " + user_name_spisok[message.from_user.id]['name'] + " покинул(а) чат.")
            user_session[message.from_user.id] = False
            user_status[message.from_user.id] = False
            bot.send_message(message.from_user.id, "Вы остановили поиск", reply_markup=keyboard_main)
            delete_user(message.from_user.id)
            bot.send_message(message.from_user.id, 'Оцените бота', reply_markup=key_feedback)
            bot.register_next_step_handler(message, feedback)
        else:
            bot.send_message(message.from_user.id, 'Нужно выбрать категорию поиска', reply_markup=keyboard_main)
    elif message.text.lower() == "/help":
        bot.send_message(message.from_user.id, "Введите /start - чтобы запустить бот")
        bot.send_message(message.from_user.id, "Это чат бот предназначен для общения и нахождения новых знакомств.")
        bot.send_message(message.from_user.id, "Выбери одну из 3х целей общения. \nЗаполни свои данные и бот рамдомно подберет пару. \nИСКАТЬ ДАЛЬШЕ - выбрать следующего собеседника. \nПОКИНУТЬ ЧАТ - выйти из чата или прекратить поиск собеседника ")

    else:
        if message.from_user.id in reg_user or str(message.from_user.id) in reg_user:
            if message.from_user.id in user_status:
                if user_status[message.from_user.id] == True:
                    if message.from_user.id in para:
                        bot.send_message(para[message.from_user.id], message.text)
            else:
                bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.message_handler(content_types=['text'])
def get_name_user(message):
    if message.text.lower() == 'остановить':
        delete_user(message.from_user.id)
        bot.send_message(message.from_user.id, 'Выберите следующее', reply_markup=keyboard_main)
    else:
        name = message.text.lower()
        user_name_spisok[message.from_user.id] = {'name':name}
        bot.send_message(message.from_user.id, 'Сколько вам лет?', reply_markup=key_stop)
        bot.register_next_step_handler(message, get_age_user)

@bot.message_handler(content_types=['text'])
def get_age_user(message):
    if message.text.lower() == 'остановить':
        delete_user(message.from_user.id)
        bot.send_message(message.from_user.id, 'Выберите следующее', reply_markup=keyboard_main)
    else:
        age = message.text.lower()

        try:
            age_num = int(age)
            if int(age_num):
                if age_num >= 18:
                    user_age[message.from_user.id] = {'age': age}
                    bot.send_message(message.from_user.id, 'Укажите город', reply_markup=key_stop)
                    bot.register_next_step_handler(message, get_city_user)

                else:
                    if user_choice[message.from_user.id]['choice'] == 'meeting':
                        if age_num >= 14:
                            user_age[message.from_user.id] = {'age': age}
                            bot.send_message(message.from_user.id, 'Укажите город', reply_markup=key_stop)
                            bot.register_next_step_handler(message, get_city_user)
                        else:
                            bot.send_message(message.from_user.id,
                                            'Вам не исполнилось 14 лет, к сожалению вам нельзя пользоваться данной категорией',
                                            reply_markup=keyboard_main)
                    elif user_choice[message.from_user.id]['choice'] == 'sex' or user_choice[message.from_user.id]['choice'] == 'money':
                        if age_num >= 18:
                            user_age[message.from_user.id] = {'age': age}
                            bot.send_message(message.from_user.id, 'Укажите город', reply_markup=key_stop)
                            bot.register_next_step_handler(message, get_city_user)
                        else:
                            bot.send_message(message.from_user.id,
                                            'Вам не исполнилось 18 лет, к сожалению вам нельзя пользоваться данной категорией',
                                            reply_markup=keyboard_main)
            else:
                bot.send_message(message.from_user.id, 'Вы неверно указали возраст, введите еще раз ваш возраст',
                                 reply_markup=key_stop)
                bot.register_next_step_handler(message, get_age_user)
        except ValueError:
            bot.send_message(message.from_user.id, 'Вы неверно указали возраст, введите еще раз ваш возраст', reply_markup=key_stop)
            bot.register_next_step_handler(message, get_age_user)


@bot.message_handler(content_types=['text'])
def get_city_user(message):
    if message.text.lower() == 'остановить':
        delete_user(message.from_user.id)
        bot.send_message(message.from_user.id, 'Выберите следующее', reply_markup=keyboard_main)
    else:
        city = message.text.lower()
        user_city[message.from_user.id] = {'city': city}
        bot.send_message(message.from_user.id, 'Укажите ваш пол', reply_markup=key_sex)
        bot.register_next_step_handler(message, get_sex_user)

@bot.message_handler(content_types=['text'])
def get_sex_user(message):
    if message.text.lower() == 'остановить':
        delete_user(message.from_user.id)
        bot.send_message(message.from_user.id, 'Выберите следующее', reply_markup=keyboard_main)
    elif message.text.lower() == 'парень':
        sex = message.text.lower()
        user_sex[message.from_user.id] = {'sex': sex}
        bot.send_message(message.from_user.id, 'Кого ищем?', reply_markup=key_sex2)
        bot.register_next_step_handler(message, get_sex_user_s)
    elif message.text.lower() == 'девушка':
        sex = message.text.lower()
        user_sex[message.from_user.id] = {'sex': sex}
        bot.send_message(message.from_user.id, 'Кого ищем?', reply_markup=key_sex2)
        bot.register_next_step_handler(message, get_sex_user_s)
    else:
        bot.send_message(message.from_user.id, 'Укажите ваш пол', reply_markup=key_sex)
        bot.register_next_step_handler(message, get_sex_user)


@bot.message_handler(content_types=['text'])
def get_sex_user_s(message):
    if message.text.lower() == 'остановить':
        delete_user(message.from_user.id)
        bot.send_message(message.from_user.id, 'Выберите следующее', reply_markup=keyboard_main)
    elif message.text.lower() == 'парня':
        sex = 'парень'
        user_sex_s[message.from_user.id] = {'sex': sex}
        user_status[message.from_user.id] = True
        user_session[message.from_user.id] = False
        if str(datetime.datetime.now().date()) in chetchik_poisk:
            chetchik_poisk[str(datetime.datetime.now().date())] = chetchik_poisk[str(datetime.datetime.now().date())] + 1
        else:
            chetchik_poisk[str(datetime.datetime.now().date())] = 1
        # def_start(message.from_user.id)
        bot.send_message(message.from_user.id, 'Напишите коротко о себе', reply_markup=key_stop)
        bot.register_next_step_handler(message, about_user)
    elif message.text.lower() == 'девушку':
        sex = 'девушка'
        user_sex_s[message.from_user.id] = {'sex': sex}
        user_status[message.from_user.id] = True
        user_session[message.from_user.id] = False
        if str(datetime.datetime.now().date()) in chetchik_poisk:
            chetchik_poisk[str(datetime.datetime.now().date())] = chetchik_poisk[str(datetime.datetime.now().date())] + 1
        else:
            chetchik_poisk[str(datetime.datetime.now().date())] = 1
        # def_start(message.from_user.id)
        bot.send_message(message.from_user.id, 'Напишите коротко о себе', reply_markup=key_stop)
        bot.register_next_step_handler(message, about_user)
    else:
        bot.send_message(message.from_user.id, 'Кого ищем?', reply_markup=key_sex2)
        bot.register_next_step_handler(message, get_sex_user_s)

@bot.message_handler(content_types=['text'])
def about_user(message):
    if message.text.lower() == 'остановить':
        delete_user(message.from_user.id)
        bot.send_message(message.from_user.id, 'Выберите следующее', reply_markup=keyboard_main)
    else:
        about = message.text
        user_about[message.from_user.id] = {'about': about}
        def_start(message.from_user.id)


def def_start(user_id):
    bot.send_message(user_id, 'Бот ищет вам пару', reply_markup=key_step)
    spisok_user = []
    if user_status[user_id] == True:
        for i in user_status:
            if user_status[i] == True:
                if user_choice[i]['choice'] == user_choice[user_id]['choice']:
                    if i != user_id:
                        if user_city[user_id] == user_city[i] and user_session[i] == False and user_status[i] == True:
                            if user_sex[user_id]['sex'] == user_sex_s[i]['sex'] and user_sex_s[user_id]['sex'] == user_sex[i]['sex']:
                                spisok_user.append(i)

        if spisok_user != []:
            user_opp = random.choice(spisok_user)
            if user_id != user_opp:
                if user_status[user_opp] == True:
                    para[user_id] = user_opp
                    para[user_opp] = user_id
                    user_session[user_opp] = True
                    user_session[user_id] = True
                    bot.send_message(user_id, 'Бот нашел вам пару, знакомтесь ' + user_name_spisok[user_opp]['name'].upper() + ', ' + user_age[user_opp]['age'] + " лет. О себе: " + user_about[user_opp]['about']+ "\n Напишите Привет")
                    bot.send_message(user_opp, 'Бот нашел вам пару, знакомтесь ' + user_name_spisok[user_id]['name'].upper() + ', ' + user_age[user_id]['age'] + " лет. О себе: " + user_about[user_id]['about'] +"\n Напишите Привет")
                    if str(datetime.datetime.now().date()) in chetchik_find:
                        chetchik_find[str(datetime.datetime.now().date())] = chetchik_find[str(datetime.datetime.now().date())] + 1
                    else:
                        chetchik_find[str(datetime.datetime.now().date())] = 1
                    # photo = bot.get_user_profile_photos(user_id)
                    # bot.send_photo(user_id, photo)
                    save_log()
        else:
            bot.send_message(user_id, "Пока не нашли вам пару, попробуйте чуть позже нажать ИСКАТЬ или подождите пока бот вам не подберет пару")

def delete_user(user_id):
    if user_id in user_choice:
        del user_choice[user_id]
    if user_id in user_name_spisok:
        del user_name_spisok[user_id]
    if user_id in user_age:
        del user_age[user_id]
    if user_id in user_city:
        del user_city[user_id]
    if user_id in user_sex:
        del user_sex[user_id]
    if user_id in user_sex_s:
        del user_sex_s[user_id]
    if user_id in user_session:
        del user_session[user_id]
    if user_id in user_status:
        del user_status[user_id]
    if user_id in user_about:
        del user_about[user_id]

def registracia_user(message):
    if not (message.from_user.id in reg_user or str(message.from_user.id) in reg_user):
        reg_user[str(message.from_user.id)] = {'first_name': message.from_user.first_name}
        reg_user[str(message.from_user.id)]['last_name'] = message.from_user.last_name
        reg_user[str(message.from_user.id)]['username'] = message.from_user.username
        with open('reg_list.txt', 'w') as f:
            json.dump(reg_user, f)

def save_log():
    with open('log_user_choice.txt', 'w') as f:
        json.dump(user_choice, f)
    with open('log_user_name_spisok.txt', 'w') as f:
        json.dump(user_name_spisok, f)
    with open('log_user_age.txt', 'w') as f:
        json.dump(user_age, f)
    with open('log_user_city.txt', 'w') as f:
        json.dump(user_city, f)
    with open('log_user_sex.txt', 'w') as f:
        json.dump(user_sex, f)
    with open('log_user_sex_s.txt', 'w') as f:
        json.dump(user_sex_s, f)
    with open('log_user_session.txt', 'w') as f:
        json.dump(user_session, f)
    with open('log_user_status.txt', 'w') as f:
        json.dump(user_status, f)
    with open('log_para.txt', 'w') as f:
        json.dump(para, f)
    with open('log_chetchik_poisk.txt', 'w') as f:
        json.dump(chetchik_poisk, f)
    with open('log_chetchik_find.txt', 'w') as f:
        json.dump(chetchik_find, f)


@bot.message_handler(content_types=['text'])
def get_user_sex(message):
    if message.text.lower() == 'да, потверждаю':
        bot.send_message(message.from_user.id, 'Укажите ваше ИМЯ', reply_markup=key_stop)
        user_choice[message.from_user.id] = {'choice': 'sex'}
        bot.register_next_step_handler(message, get_name_user)
    elif message.text.lower() == 'мне нет 18':
        bot.send_message(message.from_user.id, 'К сожалению вам нельзя пользоваться данной категорией', reply_markup=keyboard_main)
    else:
        bot.send_message(message.from_user.id, 'Вы потверждаете, что вам больше 18 лет?', reply_markup=key_18)
        bot.register_next_step_handler(message, get_user_sex)

@bot.message_handler(content_types=['text'])
def get_user_money(message):
    if message.text.lower() == 'да, потверждаю':
        bot.send_message(message.from_user.id, 'Укажите ваше ИМЯ', reply_markup=key_stop)
        user_choice[message.from_user.id] = {'choice': 'money'}
        bot.register_next_step_handler(message, get_name_user)
    elif message.text.lower() == 'мне нет 18':
        bot.send_message(message.from_user.id, 'К сожалению вам нельзя пользоваться данной категорией', reply_markup=keyboard_main)
    else:
        bot.send_message(message.from_user.id, 'Вы потверждаете, что вам больше 18 лет?', reply_markup=key_18)
        bot.register_next_step_handler(message, get_user_money)

@bot.message_handler(content_types=['text'])
def feedback(message):
    feedback_user[message.from_user.id] = {'feed': message.text}
    with open('log_feedback.txt', 'w') as f:
        json.dump(feedback_user, f)
    bot.send_message(message.from_user.id, 'Благодарим за отзыв', reply_markup=keyboard_main)

@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message="Что-то пошло не так."
                                                " Повторите попытку позже.")

@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    td = datetime.date.today()
    td = str(td)
    pay_user[str(message.from_user.id)] = {'date': td}
    # сохранение словаря в файл
    with open('pay_user.txt', 'w') as f:
        # dict_id[message.from_user.id] = {'date': td}
        json.dump(pay_user, f)
    bot.send_message(message.chat.id,
                     'Вы успешно совершили транзакцию на `{} {}`! '.format(message.successful_payment.total_amount / 100, message.successful_payment.currency),
                     parse_mode='Markdown')


def get_free(user_id):
    if not (user_id in reg_user or str(user_id) in reg_user):
        if not (user_id in free_user or str(user_id) in free_user):
            td = datetime.date.today()
            td = str(td)
            free_user[str(user_id)] = {'date': td}
            with open('free_user_list.txt', 'w') as f:
                json.dump(free_user, f)

def active_free(user_id):
    today_date = datetime.date.today()
    user_id = str(user_id)
    if user_id in free_user:
        date_user = free_user[user_id]['date'].replace('-', '')
        date_user = datetime.datetime.strptime(date_user, '%Y%m%d').date()
        if (today_date - date_user).days >= 7:
            del free_user[user_id]
            with open('free_user_list.txt', 'w') as f:
                json.dump(free_user, f)
    if user_id in pay_user:
        date_user = pay_user[user_id]['date'].replace('-', '')
        date_user = datetime.datetime.strptime(date_user, '%Y%m%d').date()
        if (today_date - date_user).days >= 10:
            del pay_user[user_id]
            with open('pay_user.txt', 'w') as f:
                json.dump(pay_user, f)



bot.polling(none_stop=True, interval=0, timeout=30)
# bot.skip_pending = True
