from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime



def log(update: Update):
    filepath = 'D:\GeekBrainsLessons\PythonProjects\Lection_05_PIP\TG_Bot\Database\db.csv'
    file = open(filepath, 'a')
    file.write(f'{datetime.datetime.now().strftime("%X %d.%m.%Y")}: {update.effective_user.username}, {update.effective_user.id}, {update.message.text} \n')
    file.close()