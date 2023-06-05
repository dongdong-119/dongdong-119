import feedparser, time

URL = "https://dongdong-119.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
#### :hammer_and_wrench: Projects<br/>
- [국회의원 발의 법률안 통계 사이트](https://github.com/dongdong-119/StatisticalDataOnLegislation)
- [딥러닝 기반 얼굴 자동인식 및 블러 서비스(RULB)] 
  1) Back-End : 
  2) Front-End : 
- [향수 어플리케이션(개발중)](https://github.com/kimyounil1/AllPouse)


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
