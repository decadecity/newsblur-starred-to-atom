import newsblur
import feedgenerator
import config

api = newsblur.API()
api.login(config.username, config.password)
stories = api.starred_stories()

feed = feedgenerator.Atom1Feed(
    title=u"newsblur starred stories",
    link=u"http://example.com",
    description=u"Stuff",
    language=u"en-GB",
)

for story in stories['stories']:
    feed.add_item(
        title=story['story_title'],
        link=story['story_permalink'],
        description=story['story_content'],
    )

print(feed.writeString('utf-8'))
