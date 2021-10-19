
def main_menu(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
# Create buttons to slect language:
    keyboard = [['💳 Оформить подписку', '📱 Перейти в меню']]

    message = """📱 Главное меню 📱

Для выбора тематики и оплаты нажмите кнопку "💳 Оформить подписку".

Если клавиатура не видна, нажмите на иконку с четырьмя точками справа от поля ввода сообщения."""
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    update.message.reply_text(message, reply_markup=reply_markup)


def start_payments_subjects(update: Update, context: CallbackContext) -> int:
    """Stores the selected gender and asks for a photo."""
    subject = update.message.text
    logger.info("Тематика %s", subject)
    message = f"Тематика \n{subject}",
    update.message.reply_text(message,
        reply_markup=ReplyKeyboardRemove(),
    )
    return SUBJECT


def start_payments(update: Update, context: CallbackContext) -> None:
# Create buttons to slect language:
    keyboard = [['Digital', 'Seo'],
                ['SMM', 'Бухгалтерия'],
                ['Контекст', 'Таргет'],
                '📱 Главное меню']

    message = 'Выберите тематику'
    reply_markup = ReplyKeyboardMarkup(keyboard,
                                       one_time_keyboard=True,
                                       resize_keyboard=True)

    update.message.reply_text(message, reply_markup=reply_markup)




def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text=f"Selected option: {query.data}")


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")

def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(bot_token)

    updater.dispatcher.add_handler(CommandHandler('start', main_menu))
    updater.dispatcher.add_handler(CommandHandler('📱 Главное меню', main_menu))

    # Add command handler to start the payment invoice
    dispatcher.add_handler(CommandHandler("💳 Оформить подписку", start_payments))
    dispatcher.add_handler(CommandHandler("📱 Перейти в меню", start_menu))

    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()