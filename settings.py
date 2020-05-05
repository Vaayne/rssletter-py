import os


IMAP_HOST = os.environ.get("IMAP_HOST")
IMAP_PORT = os.environ.get("IMAP_PORT")
IMAP_USER = os.environ.get("IMAP_USER")
IMAP_PASS = os.environ.get("IMAP_PASS")

print(IMAP_HOST)
print(IMAP_PORT)
print(IMAP_USER)
print(IMAP_PASS)



RSS_META = {
    "title": "Rssletter",
    "author": [{"name": "Liu Vaayne", "email": "lyishaou@gmail.com"}],
    "description": "Personal newsletter to RSS",
    "link": "https://blog.disbay.com",
}
