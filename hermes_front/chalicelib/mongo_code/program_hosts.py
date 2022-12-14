import datetime
from colorama import Fore
from dateutil import parser
from chalicelib.mongo_code.switchlang import switch
from chalicelib.mongo_code import state
import chalicelib.mongo_code.data_service as svc
import json
import yaml as yaml

import os
def run():
    import json
    import requests
    f = open('email.json')
    email = json.load(f)
    create_account(email["orgName"],email["email"])
    bot_name = email["botName"]
    
    register_bot((bot_name),'nluExample.yml','domainExample.yml','storiesExample.yml','rulesExample.yml',None)
    # URL = "http://h-388555080.us-east-1.elb.amazonaws.com"
    # requests.get(f"{URL}/{bot_name}")
    print("done")

    

def create_account(name, email):
    print(' ****************** REGISTER **************** ')
    # input basic info
    name = name
    email = email

    # # check if account exists
    # old_account = svc.find_account_by_email(email)
    # if old_account:
    #     error_msg(f"ERROR: Account with email {email} already exists.")
    #     return

    state.active_account = svc.create_account(name, email)
    success_msg(f"Created new account with id {state.active_account.id}.")


def log_into_account(email=None):
    print(' ****************** LOGIN **************** ')

    email = email.strip().lower()
    account = svc.find_account_by_email(email)

    if not account:
        error_msg(f'Could not find account with email {email}.')
        return

    state.active_account = account
    success_msg('Logged in successfully.')

def register_bot(bot_name,bot_NLU,bot_Domain,bot_Story,bot_Rules,bot_Forms):
    print(' ****************** REGISTER BOT **************** ')

    if not state.active_account:
        error_msg('You must login to your org account to register a product.')
        return

    bot_name = bot_name
    bot_NLU = bot_NLU
    bot_Domain = bot_Domain
    bot_Story = bot_Story
    bot_Rules = bot_Rules
    bot_Forms = bot_Forms
    
    bot_NLU_json = yaml.safe_load(open(bot_NLU))
    bot_Domain_json = yaml.safe_load(open(bot_Domain))
    bot_Story_json = yaml.safe_load(open(bot_Story))
    #print(bot_story_json)
    if bot_Rules != None :
        bot_Rules_json = yaml.safe_load(open(bot_Rules))
    if bot_Forms != None :
        bot_Form_json = yaml.safe_load(open(bot_Forms))
    else:
        bot_Form_json = None
    if not bot_name:
        error_msg('Cancelled')
        return
    old_project = svc.find_bot_by_name(bot_name)
    if old_project:
        error_msg(f"ERROR: Bot with name {bot_name} already exists.")
        return
    print(bot_Story_json)
    print(bot_Rules_json)
    bot = svc.register_bot(
        state.active_account , 
        bot_name = bot_name ,
        nlu = bot_NLU_json ,
        domain = bot_Domain_json ,
        story = bot_Story_json ,
        rules = bot_Rules_json ,
        form = bot_Form_json)

    state.reload_bot()
    success_msg(f'Registered new bot with id {bot.id}.')


def log_into_bot():
    print(' ****************** LOGIN **************** ')

    if not state.active_account:
        error_msg('You must login first to register a product.')
        return
    bot = input('Which bot do you want to go to ?').strip().lower()
    bot_ = svc.find_bot_by_name(bot)

    if not bot_:
        error_msg(f'Could not find bot {bot}.')
        return

    state.active_bot = bot_
    success_msg('Logged in successfully.')

def update_bot():
    print(' ****************** UPDATE BOT **************** ')

    if not state.active_account:
        error_msg('You must login first to register a product.')
        return
    bot = input('Which bot do you want to go to ?').strip().lower()
    bot_ = svc.find_bot_by_name(bot)

    if not bot_:
        error_msg(f'Could not find bot {bot}.')
        return

    state.active_bot = bot_
    success_msg('Logged in successfully.')
    
def exit_app():
    print()
    print('bye')
    raise KeyboardInterrupt()


def get_action():
    text = '> '
    if state.active_account:
        text = f'{state.active_account.org_name}> '
        if state.active_bot:
            text = f'{state.active_bot.botname}> '

    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action.strip().lower()


def unknown_command():
    print("Sorry we didn't understand that command.")


def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)


def error_msg(text):
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)
