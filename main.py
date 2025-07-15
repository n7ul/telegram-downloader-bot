import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Update
from telegram.ext import ContextTypes

import re

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلًا بك! أرسل لي رابطًا من أي منصة وسأعطيك رابط التحميل 🎬")

def extract_direct_link(text):
    # هذه دالة تجريبية فقط، تقدر تربطها بمواقع حقيقية لاحقًا
    match = re.search(r'(https?://\S+)', text)
    if match:
        url = match.group(1)
        return f"https://example.com/download?url={url}"
    return None

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    link = extract_direct_link(text)
    if link:
        await update.message.reply_text(f"📝 نص مستخرج:\n{link}")
    else:
        await update.message.reply_text("لم أستطع التعرف على رابط صالح، أرسل رابط مباشر من تيك توك أو يوتيوب أو إنستغرام.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
