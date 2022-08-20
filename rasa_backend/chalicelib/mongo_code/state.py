from typing import Optional

# from data.owners import Owner
# from data.project_c import Project
# import data_service as svc

# if __package__ is None or __package__ == '':
#     # uses current directory visibility
#     from data.owners import Owner
#     import data_service as svc
#     from data.project_c import Project
# else:
#     # uses current package visibility
#     from .data.owners import Owner
#     from . import data_service as svc
#     from .data.project_c import Project
import chalicelib.mongo_code.data as data 
import chalicelib.mongo_code.data_service as svc

active_account: Optional[data.organisation] = None
active_bot: Optional[data.bot] = None


def reload_account():
    global active_account
    if not active_account:
        return

    active_account = svc.find_account_by_email(active_account.org_email)


def reload_bot():
    global active_bot
    if not active_bot:
        return

    active_bot = svc.find_bot_by_name(active_bot.botname)
