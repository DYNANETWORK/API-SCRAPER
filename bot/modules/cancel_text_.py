


from telegram import (
    Update
)
from bot import (
    Config,
    ConversationHandler
)


def cancel(update: Update, context):
    """ ConversationHandler /cancel state """
    # user = update.message.from_user
    # info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(Config.CANCELLED_MESG)
    return ConversationHandler.END


def error(update: Update, context):
    """Log Errors caused by Updates."""
    print("Update %s caused error %s", update, context.error)
