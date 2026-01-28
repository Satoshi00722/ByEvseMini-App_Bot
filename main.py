import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("❌ BOT_TOKEN не задан")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    text = (
        "👋 Добро пожаловать в ByEvse Market\n\n"
        "Мы создаём:\n"
        "🤖 Telegram-ботов любой сложности\n"
        "📱 Mini Apps под бизнес\n"
        "🌐 Сайты и digital-решения\n"
        "🎬 Видео и SMM-продвижение\n\n"
        "💡 Работаем под ключ\n"
        "🛡 Оплата только после проверки функционала\n\n"
        "👇 Открой каталог и выбери услугу"
    )

    with open("welcome.jpg", "rb") as photo:
        bot.send_photo(
            chat_id=message.chat.id,
            photo=photo,
            caption=text
        )

bot.infinity_polling()
