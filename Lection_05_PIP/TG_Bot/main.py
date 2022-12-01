from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *



app = ApplicationBuilder().token("5851137049:AAEQsq4gR4nHe53wl1JU0dPANTk2NgzERtA").build()

app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("hello", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("sum", sum_command))

app.run_polling()