from mongoengine import connect
import mongoengine

class bot(mongoengine.Document):
    botname = mongoengine.StringField()
    NLU = mongoengine.DictField()
    Domain = mongoengine.DictField()
    Story = mongoengine.DictField()
    Rules = mongoengine.DictField()
    Form = mongoengine.DictField()



    meta = {
        'db_alias': 'core',
        'collection': 'bot'
    }

def global_init():
    # connect('core', host='mongodb://localhost:27017/core')
    connect(db = 'SIH' ,alias = "core" , host = "mongodb+srv://yatharthk2:Bazinga#1702@cluster0.f1topxl.mongodb.net/?retryWrites=true&w=majority")

def find_bot_by_name(bot_name: str):
    bot1 = bot.objects(botname=bot_name).first()
    return bot1

def get_bot_details(bot_name):
    print(' ** GET BOT DETAILS ** ')
    bot = find_bot_by_name(bot_name)
    print(bot)

    if not bot:
        print(f'Could not find bot {bot_name}.')
        return
    # bot_NLU = bot.NLU
    # bot_Domain = bot.Domain
    # bot_story = bot.Story
    # bot_Rules = bot.Rules
    # bot_Form = bot.Form
    return bot

global_init()