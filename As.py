import random
import datetime
import pytz
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Replace this with your actual bot token from BotFather
BOT_TOKEN = "7681136625:7672162651:AAGXapmAVmmqpdUaYrY0bJSxa4mQyVFAVew"

# Replace this with your Telegram channel username (must be publicUSERNAME = "@FREEVIPHACK22"

# Generate per
def get_pre
    result =IG", "SMALL"])
    now_utc tetime.now(pytz.UTC)
    period_number = now_utc.strftime('%Y%m result

# /start handler with channel membership check
async def start(update: Update, context: Contypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in ['member', 'administrator', 'creator']:
            # User is a member - show main menu
            keyboard = [
                [InlineKeyboardButton("🔮 Get Prediction", callback_data='get_prediction')],
                [InlineKeyboardButton("📞 Support", callback_data='support')],
                [InlineKeyboardButton("⬇️ Download Game", callback_data='download')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await context.bot.send_message(chat_id=chat_id, text="Welcome to Wingo AI Predictor!", reply_markup=reply_markup)
        else:
            raise Exception("User not a member")
    except:
        # User not a member or error occurred
        text = """
>>> ⚡ JOIN CHANNEL ⚡<<<

LINK 🔗 https://t.me/YourChannelUsername

>>> ⚡ JOIN CHANNEL ⚡<<<

>>> Dev by @GodXAshura <<<
"""
        await context.bot.send_message(chat_id=chat_id, text=text)

# Button click handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'get_prediction':
        period, result = get_prediction()
        text = f"""
>>> ASHURA AI BOT <<<
PERIOD ⚡ : {period}
RESULT ⚡ : {result}
MODE ⚡ : WINGO 1 MIN 

REGISTER LINK 🔗 https://www.Jalwa.me/#/register?invitationCode=34368633464

>>>DEV BY @GodXAshura<<<
"""
    elif query.data == 'support':
        text = """
>>> Support ✔️<<<

DM 📳 :- @Ravankin

>>> Dev by @GodXAshura <<<
"""
    elif query.data == 'download':
        text = """
✓ Register By This Link 🖇️ 

Link 🔗 https://www.Jalwa.me/#/register?invitationCode=34368633464

Register By This Link 🔗 For Activate Hack.

>>> Dev by @GodXAshura <<<
"""
    await query.edit_message_text(text)

# Main function
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
