import feedparser, time

URL = "https://dongdong-119.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
### :hand: Hi, this is Donghui's Github<br/>
hi, my name is Donghui, and I a am web back-end developer. I'm interested in not only web and database technologies but policy environment surroungding them.

<br/><br/><br/>

#### :hammer_and_wrench: Projects<br/>
- [국회의원 발의 법률안 통계 사이트](https://github.com/dongdong-119/StatisticalDataOnLegislation)
- 향수 어플리케이션(개발중)

<br/><br/><br/>
#### :blue_book: latest blog posts
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
