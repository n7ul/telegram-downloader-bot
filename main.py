import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✨ البوت يعمل الآن بنجاح!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"📩 تم استلام: {update.message.text}")

def main():
    # 1. إعدادات خاصة لمنع التعارض
    app = Application.builder() \
        .token(BOT_TOKEN) \
        .concurrent_updates(True) \  # ← يسمح بمعالجة متزامنة للرسائل
        .build()

    # 2. تسجيل ال handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # 3. تشغيل البوت مع إعدادات مضبوطة
    app.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True,  # ← يحذف أي تحديثات معلقة من التشغيلات السابقة
        close_loop=False  # ← يمنع إعادة فتح الاتصال تلقائياً
    )

if __name__ == "__main__":
    print("🚀 Starting bot...")
    main()
