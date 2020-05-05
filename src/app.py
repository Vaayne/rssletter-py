from fastapi import FastAPI, Response
from src.feed import generate_feed
from src.mail import fetch_emails

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/rss")
def read_item(
        title: str = "Rssletter",
        query: str = None
    ):
    mails = fetch_emails(query)
    mails = sorted(mails, key=lambda x: x.date, reverse=True)
    feed = generate_feed(mails, title)
    return Response(content=feed, media_type="application/xml")
