


class Translation:
    START_TEXT = (
        "Hi!\n"
        "Thank you for using me 😬\n"
        "Enter your Telegram Phone Number, "
        "to get the API Credentials from my.telegram.org\n\n"
        "/start at any stage to re-enter your details"
    )
    AFTER_RECVD_CODE_TEXT = (
        "Got it!\n"
        "now please send the Telegram code that "
        "you received from Telegram!\n\n"

        "this code is only used for the purpose of "
        "getting the APP ID from my.telegram.org\n"
        "if you do not trust this bot dev, "
        "please host this bot yourself\n"
        "by opening https://t.me/DYNA_SUPPORT and "
        "clicking on the Deploy To Heroku Button\n\n"

        "/start at any stage to re-enter your details"
    )
    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."
    ERRED_PAGE = "something wrong. failed to get app id. \n\n@DYNA_SUPPORT"
    CANCELLED_MESG = "Bye! Please re /start the bot conversation"
    IN_VALID_CODE_PVDED = (
        "sorry, "
        "but the input does not seem to be "
        "a valid Telegram Web-Login code"
    )
    IN_VALID_PHNO_PVDED = (
        "sorry, "
        "but the input does not seem to be "
        "a valid phone number"
    )
