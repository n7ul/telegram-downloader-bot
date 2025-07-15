import os
import re
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# الحصول على توكن البوت من متغيرات البيئة
BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """يرسل رسالة ترحيبية عند استخدام الأمر /start"""
    await update.message.reply_text("مرحباً بك في البوت! 👋\nأرسل لي أي رابط وسأحاول تحليله.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """يعالج الرسائل الواردة ويستخرج الروابط"""
    text = update.message.text
    link = extract_direct_link(text)
    
    if link:
        await update.message.reply_text(f"🔍 وجدت هذا الرابط:\n{link}")
    else:
        await update.message.reply_text("⚠ لم أتمكن من العثور على رابط صالح في الرسالة")

def extract_direct_link(text):
    """يستخرج الروابط من النص باستخدام تعبير منتظم"""
    match = re.search(r'(https?://[^\s]+)', text)
    return match.group(1) if match else None

def main():
    """الدالة الرئيسية لتشغيل البوت"""
    try:
        # إنشاء تطبيق البوت
        app = Application.builder().token(BOT_TOKEN).build()
        
        # إضافة معالجات الأوامر والرسائل
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        print("✅ البوت يعمل الآن...")
        app.run_polling()
    except Exception as e:
        print(f"❌ حدث خطأ: {e}")

if __name__ == "__main__":
    main()
