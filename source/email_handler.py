import yagmail


def email_wrapper(user,
                  password,
                  receiver,
                  subject='',
                  body='',
                  attachments=None):
    yag = yagmail.SMTP(user=user, password=password)
    yag.send(
        to=receiver,
        subject=subject,
        contents=body,
        attachments=attachments,
    )