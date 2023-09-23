import yagmail

from .config import load_config

config = load_config()


def send_mail(subject: str, contents: str, to: str = config.user):
    """
    Sends an email.

    Args:
        subject (str): The subject of the email.
        contents (str): The contents of the email.
        to (str, optional): email addresses to send the email to. Defaults to yourself.

    Returns:
        None
    """
    yagmail.SMTP(
        user=config.user, password=config.password, host=config.host, port=config.port
    ).send(to=to, subject=subject, contents=contents)
