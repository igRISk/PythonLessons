from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hello\n/time\n/sum')

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update)
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update)
    msg = update.message.text
    items = msg.split() # /sum 123 456
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')