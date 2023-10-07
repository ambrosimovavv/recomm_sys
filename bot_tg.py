import telebot
import main
# ни в коем случае нельзя открыто писать токен
token = '6334360475:AAFNegcH1OTkdWRYWFWKU2BE3ETgiQX5cKM'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def get_text_message(massage):
    answ = list(main.recom_by_user(massage.text))
    print(answ)
    try:
        bot.send_message(massage.from_user.id, "Фильмы на вечер")
        for i in answ:
            bot.send_message(massage.from_user.id, i)
    except:
        bot.send_message(massage.from_user.id, "dont worry")


bot.polling(none_stop=True, interval=0)