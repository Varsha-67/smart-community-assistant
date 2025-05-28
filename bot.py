from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, CallbackQueryHandler


# Replace with your actual token
BOT_TOKEN = "##############################################"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()

    if "hello" in user_message or "hi" in user_message:
        response = "Hey there! 👋"
    elif "how are you" in user_message:
        response = "I'm just a bot, but I'm doing great! 😄"
    elif "joke" in user_message:
        response = "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"
    elif "bye" in user_message:
        response = "Goodbye! Have a great day! 👋"
    else:
        response = f"You said: {user_message}"

    await update.message.reply_text(response)

async def show_options(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data="yes")],
        [InlineKeyboardButton("No", callback_data="no")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Do you like this bot?", reply_markup=reply_markup)

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "yes":
        response = "Awesome! 😊"
    elif query.data == "no":
        response = "Oh no! I’ll try to do better. 😢"
    else:
        response = "I didn't get that."

    await query.edit_message_text(text=response)



if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # This handles all text messages
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), reply))
    app.add_handler(CommandHandler("options", show_options))
    app.add_handler(CallbackQueryHandler(handle_button))


    print("Bot is running...")
    app.run_polling()
