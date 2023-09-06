import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6648017333:AAFcoLqPTbZBeLyp6ddF_Th0FKk57qXAsAI)
    STRING_SESSION = os.environ.get("STRING_SESSION", BQDAZY_itu7UVsdnohkbzf4rfsW_8TaTTmCyPIxiyFoQw-oHm2Pd7Kreust7ApkNabUEQdgo5XhX-dQG-MUs1J0YNsSNZm7f-KNLtzth_vufq-5SKe-yn-LHD4pUYhNuaqJOihbybQJ6Z0B9S4jmdBJNtCfMADU3z28girXZU9KxkkkHF3jWdg8GZK3RkrsPVxoTMKnxSiJjB78NT09xvPDV4o-gSgh6bzCOHPX55HP8C0zmfq-dFees2jqLqlKjefs8pDTdHpFqUBotm9jF6ewd3eaEfDG-P-uGsU1c-8wj7xEnxmiFVoGru2B2bk5cy9boYvMehKKrNH1maIIfg0l6WnvjvAA)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
