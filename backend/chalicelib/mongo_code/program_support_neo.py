import datetime
from colorama import Fore
from dateutil import parser
from chalicelib.mongo_code.switchlang import switch
from chalicelib.mongo_code import state
import chalicelib.mongo_code.data_service as svc
import json
import yaml as yaml


def create_account(name,email):
    print(' ****************** REGISTER **************** ')
    # input basic info
    # name = input('What is your organisation name? ')
    # email = input('What is your email? ').strip().lower()
    email = email.strip().lower()
    
    # # check if account exists
    # old_account = svc.find_account_by_email(email)
    # if old_account:
    #     error_msg(f"ERROR: Account with email {email} already exists.")
    #     return

    state.active_account = svc.create_account(name, email)
    success_msg(f"Created new account with id {state.active_account.id}.")


def log_into_account(email):
    print(' ****************** LOGIN **************** ')

    # email = input('What is your email? ').strip().lower()
    email = email.strip().lower()
    account = svc.find_account_by_email(email)

    if not account:
        error_msg(f'Could not find account with email {email}.')
        return

    state.active_account = account
    success_msg('Logged in successfully.')

def register_bot(email_org
                , bot_name 
                , bot_NLU 
                , bot_Domain 
                , bot_story
                , bot_Rules
                , bot_Forms):
    print(' ****************** REGISTER BOT **************** ')

    log_into_account(email_org)

    bot_name = bot_name
    bot_NLU = bot_NLU
    bot_Domain = bot_Domain
    bot_story = bot_story
    bot_Rules = bot_Rules
    bot_Form = bot_Forms
    bot_NLU_json = yaml.safe_load(open(bot_NLU))
    bot_Domain_json = yaml.safe_load(open(bot_Domain))
    bot_story_json = yaml.safe_load(open(bot_story))
    if bot_Rules != None :
        bot_Rules_json = yaml.safe_load(open(bot_Rules))
    if bot_Form != None :
        bot_Form_json = yaml.safe_load(open(bot_Form))
    if not bot_name:
        error_msg('Cancelled')
        return
    old_project = svc.find_bot_by_name(bot_name)
    if old_project:
        error_msg(f"ERROR: Bot with name {bot_name} already exists.")
        return
    bot = svc.register_bot(
        state.active_account , 
        bot_name = bot_name ,
        nlu = bot_NLU_json ,
        domain = bot_Domain_json ,
        story = bot_story_json ,
        rules = bot_Rules_json ,
        form = bot_Form_json)

    state.reload_bot()
    success_msg(f'Registered new bot with id {bot.id}.')


def log_into_bot(bot_name):
    print(' ****************** LOGIN **************** ')
    #bot = input('Which bot do you want to go to ?').strip().lower()
    bot_ = svc.find_bot_by_name(bot_name)

    if not bot_:
        error_msg(f'Could not find bot {bot_name}.')
        return

    state.active_bot = bot_
    success_msg('Logged in successfully.')



    state.active_bot = bot_
    success_msg('Logged in successfully.')

def get_bot_details(bot_name):
    print(' ****************** GET BOT DETAILS **************** ')
    bot = svc.find_bot_by_name(bot_name)

    if not bot:
        error_msg(f'Could not find bot {bot_name}.')
        return

    

    state.active_bot = bot
    success_msg('Logged in successfully.')
    
    
def exit_app():
    print()
    print('bye')
    raise KeyboardInterrupt()

def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)

def error_msg(text):
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)