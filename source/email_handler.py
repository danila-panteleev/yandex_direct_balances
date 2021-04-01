import yagmail
from typing import AnyStr, Dict


def email_receiver(user: AnyStr,
                   password: AnyStr,
                   receiver: AnyStr,
                   balances: Dict[AnyStr, AnyStr],
                   subject: AnyStr = '',
                   body: AnyStr = '',
                   attachments=None) -> None:

    email_balances = balances.copy()
    last_update = email_balances.pop('Last update')
    for k in sorted(email_balances.keys()):
        body += f'{k}: {email_balances[k]}\n'
    body += last_update

    yag = yagmail.SMTP(user=user, password=password)
    yag.send(
        to=receiver,
        subject=subject,
        contents=body,
        attachments=attachments,
    )