AUTHOR = 'thelumberjhack'
SITENAME = 'thelumberj(h)ack'
SITEURL = ''
SITESUBTITLE = 'Trials and tribulations of a lumberj(h)ack in a binary world'

PATH = 'content'

TIMEZONE = 'America/Vancouver'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('BlahCats', 'https://blahcats.github.io/'),)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/thelumberjhack'),
    ('Github', 'https://github.com/thelumberjhack'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'assets',
    'assets/images',
]

EXTRA_PATH_METADATA = {
    'assets/images/favicon.ico': {'path': 'favicon.ico'},
}