import feedparser, time

URL = "https://dongdong-119.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
### Hi, this is Donghui's Github<br/>
hi, my name is Donghui, and I am web back-end developer. I'm interested in not only programming and web and database technologies but policy environment surroungding them.

<br/><br/><br/>

"""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"- [{feed['title']}]({feed['link']}) <br/>\n"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
