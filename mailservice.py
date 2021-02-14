import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class BodyMail:
    from_email: str
    to_emails: list[str]
    subject: str
    html_content: str


class IMailService:
    def send(self, body: BodyMail):
        raise NotImplemented


class SendGridMail(IMailService):

    def __init__(self, key):
        self.send_grid = SendGridAPIClient(key)

    def _set_body_mail(self, body: BodyMail):
        return Mail(
            from_email=body.from_email,
            to_emails=body.to_emails,
            subject=body.subject,
            html_content=body.html_content)

    def send(self, body: BodyMail):
        message = self._set_body_mail(body)
        self.send_grid.send(message)
