AUTHOR = 'İpek'
SITENAME = 'Su Önemi'
SITEURL = ""

PATH = "content"
TIMEZONE = 'Europe/Istanbul'
DEFAULT_LANG = 'tr'

# Feeds — disable for development
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
)

# Social links
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 5
RELATIVE_URLS = True

# ✅ Add custom CSS
STATIC_PATHS = ['images', 'static']

EXTRA_PATH_METADATA = {
    'static/DefineClasses.css': {'path': 'theme/css/DefineClasses.css'},
}

CUSTOM_CSS = 'theme/css/DefineClasses.css'

# ✅ Tell Pelican where your standalone pages live
PAGE_PATHS = ['pages']
