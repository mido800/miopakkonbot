from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8825701929:AAH3PPhgs2Q_OQPm2AejHejyW-4jS8Fg6nI"
KEYWORD = "میو"
DELETE_AFTER = 120

async def delete_later(context):
    try:
        await context.bot.delete_message(context.job.chat_id, context.job.data)
    except:
        pass

async def handle(update, context):
    if update.message and "میو" in update.message.text:
        context.job_queue.run_once(delete_later, DELETE_AFTER, chat_id=update.effective_chat.id, data=update.message.message_id)

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
app.run_polling()
