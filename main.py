import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

# تأكد أن اسم المتغير مطابق تماماً لما في Railway
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# ━━━ Handlers ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """يرسل رسالة ترحيبية عند /start"""
    await update.message.reply_text("🎉 البوت يعمل بنجاح! أرسل لي أي رسالة.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """يتعامل مع الرسائل النصية"""
    text = update.message.text
    await update.message.reply_text(f"📩 تلقيت: {text}")

# ━━━ Main Setup ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def main():
    try:
        print("🚀 جاري تشغيل البوت...")
        
        # 1. بناء التطبيق مع إعدادات مضبوطة
        app = Application.builder() \
            .token(BOT_TOKEN) \
            .concurrent_updates(True) \  # ← حل مشكلة Conflict
            .build()

        # 2. إضافة الـ Handlers
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT, handle_message))

        # 3. التشغيل مع منع التكرار
        print("✅ البوت جاهز لاستقبال الرسائل...")
        app.run_polling(
            allowed_updates=Update.ALL_TYPES,
            close_loop=False,
            drop_pending_updates=True  # ← يحذف أي تحديثات قديمة متبقية
        )

    except Exception as e:
        print(f"❌ خطأ: {e}")

if __name__ == "__main__":
    main()
