import datetime
import mongoengine

class organisation(mongoengine.Document):
    org_name = mongoengine.StringField(required=True)
    org_email = mongoengine.StringField(required=True)
    # project_ids = mongoengine.ListField()
    # channel_id = mongoengine.ListField(mongoengine.ReferenceField('Channels'))
    bot_id = mongoengine.ListField(mongoengine.ReferenceField('bot'))
    log_id = mongoengine.ListField(mongoengine.ReferenceField('log'))

    meta = {
        'db_alias': 'core',
        'collection': 'organisation'
    }
