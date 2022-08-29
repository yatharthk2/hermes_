# from curses import noqiflush
from typing import List, Optional
import datetime
import bson


import chalicelib.mongo_code.data as data


def create_account(name: str, email: str) -> data.organisation:
    owner = data.organisation()
    owner.org_name = name
    owner.org_email = email

    owner.save()

    return owner


def find_account_by_email(email: str) -> data.organisation:
    owner = data.organisation.objects(org_email=email).first()
    return owner

def find_bot_by_name(bot_name: str) -> data.bot:
    bot = data.bot.objects(botname=bot_name).first()
    return bot

    
def register_bot(active_account: data.organisation, bot_name: str , nlu:dict , domain:dict , story:dict , rules:dict , form:dict     ) -> data.bot:
    
    bot = data.bot()
    bot.botname = bot_name
    bot.NLU = nlu
    bot.Domain = domain
    bot.story = story
    bot.Rules = rules
    bot.Form = form

    bot.save()

    account = find_account_by_email(active_account.org_email)
    account.bot_id.append(bot.id)
    account.save()

    return bot





