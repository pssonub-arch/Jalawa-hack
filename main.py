import logging
import random
from datetime import datetime, timezone
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.constants import ChatMemberStatus

# === Config ===
BOT_TOKEN = "7730057723:AAFT_dT8hdlrbOFeJidm4tFyb7JwRkUdqF8"
CHANNEL_USERNAME = "Allbotsandhack"
OWNER_ID = 1016409707

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

user_last_prediction = {}

main_menu_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("💻 Get Prediction", callback_data="get_prediction")],
    [InlineKeyboardButton("👤 Support", callback_data="support")],
    [InlineKeyboardButton("📦 Download Game", callback_data="download")],
])

back_to_menu_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back_to_main")]
])

prediction_keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("🔁 Next Prediction", callback_data="get_prediction")],
    [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="back_to_main")]
])


def greeting_by_time():
    hour = datetime.now().hour
    if hour < 12:
        return "🌅 Good Morning"
    elif hour < 18:
        return "🌞 Good Afternoon"
    else:
        return "🌙 Good Evening"

# === Get period number ===
def get_period():
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%Y%m%d")
    total_minutes = now.hour * 60 + now.minute
    current = f"{date_str}1000{10001 + total_minutes}"
    previous = f"{date_str}1000{10001 + total_minutes - 1}"
    return previous, current

# === Format prediction output ===
def format_prediction_output(user_id, period, result, prev_period):
    user_last_prediction[user_id] = (prev_period, result)

    prev_display = (
        "🕘 *Previous Prediction*\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        f"🔢 *Period:* `{prev_period}`\n"
        f"🎯 *Result:* `{result}`\n"
        "━━━━━━━━━━━━━━━━━━━\n"
    )

    return (
        "```\n"
        "┏━━━━━━━━━━━━━━━┓\n"
        "┃ PREDICTION AI BOT  ┃\n"
        "┗━━━━━━━━━━━━━━━┛\n"
        "```"
        f"🧠 *Wingo 1 Min Hack*\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        f"📅 *Current Period:* `{period}`\n"
        f"💥 *Prediction:* `{result}`\n"
        "━━━━━━━━━━━━━━━━━━━\n"
        f"{prev_display}"
        "✅ [Register Here](https://www.Jalwa.me/#/register?invitationCode=34368633464)\n\n"
        "👨‍💻 *Dev:* @GodXAshura"
    )

# === Check if user joined ===
async def is_user_joined(context: ContextTypes.DEFAULT_TYPE, user_id: int) -> bool:
    try:
        member = await context.bot.get_chat_member(chat_id=f"@{CHANNEL_USERNAME}", user_id=user_id)
        return member.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
    except Exception as e:
        logger.warning(f"Error checking membership: {e}")
        return False

# === Start Command ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    greeting = greeting_by_time()

    if user.id == OWNER_ID or await is_user_joined(context, user.id):
        await update.message.reply_text(
            f"{greeting}, *{user.first_name}*!\n\n"
            "Welcome to *AI Hack Bot*.\n"
            "Please choose an option below:",
            parse_mode="Markdown",
            reply_markup=main_menu_keyboard
        )
    else:
        await update.message.reply_text(
            f"*Access Denied*\n\n"
            f"Please join our channel to use the bot:\n"
            f"🔗 [Join Now](https://t.me/{CHANNEL_USERNAME})\n\n"
            f"_After joining, return here and press /start._\n\n"
            "👨‍💻 *Dev:* @GodXAshura",
            parse_mode="Markdown"
        )

# === Button Handler ===
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = query.from_user
    await query.answer()

    if user.id != OWNER_ID and not await is_user_joined(context, user.id):
        await query.edit_message_text(
            f"*Access Denied*\n\n"
            f"🔗 [Join the channel first](https://t.me/{CHANNEL_USERNAME})\n\n"
            f"_Then press /start to continue._",
            parse_mode="Markdown"
        )
        return

    if query.data == "get_prediction":
        await query.edit_message_text("⌛ Generating your prediction...", parse_mode="Markdown")
        await context.bot.send_chat_action(chat_id=query.message.chat.id, action="typing")

        prev_period, curr_period = get_period()
        result = random.choice(["BIG", "SMALL"])

        await query.edit_message_text(
            format_prediction_output(user.id, curr_period, result, prev_period),
            parse_mode="Markdown",
            reply_markup=prediction_keyboard
        )

    elif query.data == "support":
        await query.edit_message_text("⌛ Loading support info...", parse_mode="Markdown")
        await query.edit_message_text(
            "*Need Help?*\n\n"
            "Message support:\n"
            "📨 [@Rahulpro1](https://t.me/Rahulpro1)\n\n"
            "_Support is available 24/7._",
            parse_mode="Markdown",
            reply_markup=back_to_menu_keyboard
        )

    elif query.data == "download":
        await query.edit_message_text("⌛ Loading download links...", parse_mode="Markdown")
        await query.edit_message_text(
            "*Download Game & Activate Hack*\n\n"
            "Register using any of the links below:\n\n"
            "1. [Jalwa](https://www.Jalwa.org/#/register?invitationCode=34368633464)\n"
            "2. [Sikkimin](https://sikkimin.com/#/register?invitationCode=65277140032)\n"
            "3. [TashanWin](http://www.tashanwin.club/#/register?invitationCode=66718202302)\n"
            "4. [91club](https://www.91appi.com/#/register?invitationCode=23848286654)\n\n"
            "👨‍💻 *Dev:* @GodXAshura",
            parse_mode="Markdown",
            reply_markup=back_to_menu_keyboard
        )

    elif query.data == "back_to_main":
        await query.edit_message_text(
            "*Main Menu*\n\n"
            "Please choose an option below:",
            parse_mode="Markdown",
            reply_markup=main_menu_keyboard
        )

# === Main ===
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
