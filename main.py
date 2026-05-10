import telebot
from telebot import types

# التوكن الخاص بك الذي قمنا بتجهيزه
TOKEN = '8788666843:AAHCi4__29dTgS03LTNmtRRVc-ypZGhS8-g'
bot = telebot.TeleBot(TOKEN)

# 1. القائمة الرئيسية (Keyboard)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('📜 أعلام العترة')
    btn2 = types.KeyboardButton('⚖️ الميزان الصحيح')
    markup.add(btn1, btn2)
    bot.send_message(
        message.chat.id, 
        "مرحباً بك في بوت (حقائق الصدق) 🌿\nتم تفعيل البوت بنجاح على منصة Render.", 
        reply_markup=markup
    )

# 2. قسم أعلام العترة (مع أزرار داخلية)
@bot.message_handler(func=lambda message: message.text == '📜 أعلام العترة')
def show_etrah_menu(message):
    inline_markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("النبي محمد ﷺ", callback_data="prophet")
    item2 = types.InlineKeyboardButton("الإمام علي (ع)", callback_data="ali")
    item3 = types.InlineKeyboardButton("السيدة فاطمة (ع)", callback_data="fatima")
    inline_markup.add(item1, item2, item3)
    
    bot.send_message(message.chat.id, "اختر من أعلام العترة الطاهرة لمعرفة المزيد:", reply_markup=inline_markup)

# 3. الرد على الأزرار الداخلية
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "prophet":
        text = "✨ **النبي محمد ﷺ:** خاتم الأنبياء والمرسلين، أرسله الله رحمة للعالمين."
    elif call.data == "ali":
        text = "✨ **الإمام علي بن أبي طالب (ع):** أول من آمن من الصبيان، وباب مدينة علم النبي ﷺ."
    elif call.data == "fatima":
        text = "✨ **السيدة فاطمة الزهراء (ع):** سيدة نساء العالمين وبضعة النبي ﷺ."
    
    bot.send_message(call.message.chat.id, text, parse_mode='Markdown')

# 4. زر الميزان الصحيح
@bot.message_handler(func=lambda message: message.text == '⚖️ الميزان الصحيح')
def show_mizan(message):
    bot.send_message(message.chat.id, "⚖️ **الميزان الصحيح:** قسم القواعد العلمية والمناهج التحقيقية.")

# تشغيل البوت
print("البوت يعمل الآن بنجاح...")
bot.infinity_polling()
