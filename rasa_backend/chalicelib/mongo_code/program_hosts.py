import datetime
from colorama import Fore
from dateutil import parser
from chalicelib.mongo_code.switchlang import switch
from chalicelib.mongo_code import state
import chalicelib.mongo_code.data_service as svc
import json
import yaml as yaml


def run():
    print(' ****************** Welcome host **************** ')
    print()

    show_commands()

    while True:
        action = get_action()

        with switch(action) as s:
            s.case('ca', create_account)
            s.case('b', register_bot)
            s.case('l', log_into_account)
            s.case('lb', log_into_bot)
            s.case('gb', get_bot_details)
            s.case('m', lambda: 'change_mode')
            s.case(['x', 'bye', 'exit', 'exit()'], exit_app)
            s.case('?', show_commands)
            s.case('', lambda: None)
            s.default(unknown_command)

        if action:
            print()

        if s.result == 'change_mode':
            return


def show_commands():
    print('-> New to hermes.ai?')
    print('1) [C]reate an [a]ccount')
    print('2) [L]ogin to your account\n')
    print('-> Following actions Requires account login :')
    print('1) Register a new [B]ot')
    print('2) [L]ogin to a [B]ot')
    



def create_account():
    print(' ****************** REGISTER **************** ')
    # input basic info
    name = input('What is your organisation name? ')
    email = input('What is your email? ').strip().lower()

    # # check if account exists
    # old_account = svc.find_account_by_email(email)
    # if old_account:
    #     error_msg(f"ERROR: Account with email {email} already exists.")
    #     return

    state.active_account = svc.create_account(name, email)
    success_msg(f"Created new account with id {state.active_account.id}.")


def log_into_account():
    print(' ****************** LOGIN **************** ')

    email = input('What is your email? ').strip().lower()
    account = svc.find_account_by_email(email)

    if not account:
        error_msg(f'Could not find account with email {email}.')
        return

    state.active_account = account
    success_msg('Logged in successfully.')

def register_bot():
    print(' ****************** REGISTER BOT **************** ')

    if not state.active_account:
        error_msg('You must login to your org account to register a product.')
        return

    bot_name = input('what is the name of your bot? ')
    bot_NLU = input('enter json of your NLU model: ')
    bot_Domain = input('enter json of your Domain model: ')
    bot_story = input('enter json of your story model: ')
    bot_Rules = input('enter json of your Rules model: ')
    bot_Form = input('enter json of your Form model: ')
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

def get_bot_details():
    print(' ****************** GET BOT DETAILS **************** ')
    bot_name = input('which bot do you want to see details of ?').strip().lower()
    bot = svc.find_bot_by_name(bot_name)
    print(bot)

    if not bot:
        error_msg(f'Could not find bot {bot_name}.')
        return
    # bot_NLU = bot.NLU
    # bot_Domain = bot.Domain
    # bot_story = bot.Story
    # bot_Rules = bot.Rules
    # bot_Form = bot.Form
    return bot 
    
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
