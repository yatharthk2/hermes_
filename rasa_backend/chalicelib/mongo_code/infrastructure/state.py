from typing import Optional

from rasa_backend.chalicelib.mongo_code.data.Organisation import organisation
import data_service as svc

active_account: Optional[organisation] = None


def reload_account():
    global active_account
    if not active_account:
        return

    active_account = svc.find_account_by_email(active_account.email)
