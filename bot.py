import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 8554022206:AAGQMVDqNC7QXEvnMnqpmQgPNB8EW_0pte4

def get_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(url).json()
    return float(data["price"])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ BTC Risk Coach läuft!\nBefehle:\n/price - aktueller BTC Preis\n/signal - Marktinfo")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price = get_price()
    await update.message.reply_text(f"💰 Aktueller BTC Preis: {price:.2f} $")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    price = get_price()

    if price > 60000:
        msg = f"📊 BTC: {price:.2f}$\nTrend eher LONG beobachten"
    else:
        msg = f"📊 BTC: {price:.2f}$\nTrend eher SHORT beobachten"

    await update.message.reply_text(msg)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("signal", signal))

app.run_polling()
