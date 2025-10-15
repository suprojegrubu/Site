AUTHOR = 'İpek'
SITENAME = 'Su Önemi'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Istanbul'

DEFAULT_LANG = 'TR'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 5

RELATIVE_URLS = True

EXTRA_PATH_METADATA = {
    'static/DefineClasses.css': {'path': 'content/DefineClasses.css'},
}

CUSTOM_CSS = 'content/DefineClasses.css'

