import newsblur
import feedgenerator
import config

from datetime import datetime

def get_date(string, fmt="%Y-%m-%d %H:%M:%S"):
    return datetime.strptime(string, fmt)

api = newsblur.API()
api.login(config.username, config.password)
stories = api.starred_stories()

feed = feedgenerator.Atom1Feed(
    title=u"newsblur starred stories",
    link=u"http://orde.org.uk/shared.xml",
    description=u"Stuff",
    language=u"en-GB",
    author=u'Fnord',
)

for story in stories['stories']:
    feed.add_item(
        title=story['story_title'],
        link=story['story_permalink'],
        description=story['story_content'],
        author_name=story['story_authors'],
        pubdate=get_date(story['story_date']),
    )

print(feed.writeString('utf-8'))
