import telebot
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Users
bot = telebot.TeleBot('2144928257:AAG9jHTBQoUlPS5KDydyEny9RO_PTpZ6hIQ')

engine = create_engine('sqlite:///test.db', echo = True)
Session = sessionmaker(engine)

name = ''
surname = ''
age = 0
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    print(name, ' ', surname)
    Base.metadata.create_all(engine)
    with Session() as session:
        new = Users(name = name, surname = surname)
        session.add(new)
        session.commit()

def main():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()

bot.polling(none_stop=True, interval=0)


