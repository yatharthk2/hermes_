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