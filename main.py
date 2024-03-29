from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from googletrans import Translator

# Initialize translator
translator = Translator()

# Telegram bot token
TOKEN = 'https://github.com/Spudblocks'

# Function to handle /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the Translate Bot! Send me any English word, and I will translate it to Bengali for you.')

# Function to handle text messages
def translate_text(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    translation = translator.translate(text, src='en', dest='bn').text
    update.message.reply_text(translation)

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))

    # Register message handler for text messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_text))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
