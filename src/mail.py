from imbox import Imbox
from dateutil.parser import parse
from settings import IMAP_HOST, IMAP_PASS, IMAP_USER


def fetch_emails(query: str = None):
    """
    query:
        sent_from: Messages sent FROM
        sent_to: Messages sent TO
        subject: Messages whose subjects contain a string
        folder: Messages from a specific folder
    """
    with Imbox(
        IMAP_HOST,
        username=IMAP_USER,
        password=IMAP_PASS,
        ssl=True,
        ssl_context=None,
        starttls=False,
    ) as box:
        messages = box.messages()
        for uid, message in messages[-1:-11:-1]:
            if not message.body.get("html"):
                plain = message.body.get("plain")[0]
                message.body["html"] = f"<pre>{plain}</pre>"
            else:
                message.body["html"] = message.body["html"][0]
            message.date = parse(message.date)
            yield message
