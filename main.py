from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Клавиатура с большими кнопками
reply_keyboard = [['Хочу цитату', 'Да_Нет']]
markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True)

quotes = [
    "Сделай сегодня то, что другие не хотят, и завтра будешь жить так, как другие не могут.",
    "Успех — это сумма малых усилий, повторяемых день за днем.",
    "Начни делать сейчас — идеальное время может никогда не наступить.",
    "Трудности — это то, что делает жизнь интересной, а их преодоление — то, что делает жизнь значимой. — Джошуа Дж. Марин",
    "Не бойся медленно идти вперед, бойся стоять на месте.",
    "Каждая большая мечта начинается с первого шага.",
    "Неудача — это просто возможность начать снова, но уже более мудро. — Генри Форд",
    "Настоящий успех — это не количество денег, а счастье и удовлетворение от того, что ты делаешь.",
    "Чтобы что-то изменить, нужно начать с себя.",
    "Ты не должен быть великим, чтобы начать — но должен начать, чтобы стать великим. — Зиг Зиглар",
    "Секрет успеха в том, чтобы начать. — Марк Твен",
    "Верь в себя, и весь мир поверит в тебя.",
    "Неважно, как медленно ты идёшь, главное — не останавливаться. — Конфуций",
    "Сделай сегодня то, что другие откладывают на завтра.",
    "Твой единственный предел — это ты сам."
]


ans = [
    "Да",
    "Нет",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Нажми кнопку, чтобы получить мотивационную цитату.",
        reply_markup=markup
    )
import random
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == 'Хочу цитату':
        quote = random.choice(quotes)
        await update.message.reply_text(quote, reply_markup=markup)
    elif text == 'Да_Нет':
        answer = random.choice(ans)
        await update.message.reply_text(answer, reply_markup=markup)
    else:
        await update.message.reply_text("Пожалуйста, выбери кнопку.", reply_markup=markup)

if __name__ == '__main__':
    app = ApplicationBuilder().token('TOKEN').build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
