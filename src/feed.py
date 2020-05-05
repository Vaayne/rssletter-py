import imbox
from feedgen.entry import FeedEntry
from feedgen.feed import FeedGenerator

from settings import RSS_META
from src.mail import fetch_emails


def generate_item(msg):
    fe = FeedEntry()
    fe.author(msg.sent_from)
    fe.pubDate(msg.date)
    fe.title(msg.subject)
    # print(f"{fe.title()} - {fe.pubDate()}")
    content = msg.body.get("html")
    fe.description(content, isSummary=True)
    return fe


def generate_feed(mails, title: str = None):
    feed = RSS_META
    authors = feed.get("author")
    fg = FeedGenerator()
    # fg.load_extension('rss', rss=True)
    fg.title(title or feed.get("title"))
    fg.author(authors)
    fg.link(href=feed.get("link"), rel="alternate")
    fg.description(feed.get("description"))

    for msg in mails:
        fe = generate_item(msg)
        fg.add_entry(fe, order="append")

    return fg.rss_str(pretty=True)
