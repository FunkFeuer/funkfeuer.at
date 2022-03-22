# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time

BLOG_AUTHOR = "FunkFeuer Wien - Verein zur Förderung freier Netze"
BLOG_TITLE = "FunkFeuer.at"
SITE_URL = "/"
BLOG_EMAIL = "admin@funkfeuer.at"
BLOG_DESCRIPTION = "FunkFeuer.at"
THEME = 'funkfeuer.at-theme'
USE_BUNDLES = False

FAVICONS = (
     ("icon", "assets/favicon.ico", "16x16"),
 )

TWITTER_CARD = {
    'use_twitter_cards': True,
    'card': 'summary',
    'site': '@Funkfeuer_at',
    'creator': '@Funkfeuer_at',
}

# A HTML fragment describing the license, for the sidebar.
# (translatable)
LICENSE = ""


DEFAULT_LANG = "de"
TRANSLATIONS_PATTERN = "{path}.{lang}.{ext}"
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # "en": "./en",
}
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ('https://map.funkfeuer.at/', 'Karte'),
        ('https://wiki.funkfeuer.at/', 'Wiki'),
        ('https://forum.funkfeuer.at/', 'Forum'),
        ('https://housing.funkfeuer.at/', 'Server Housing'),
        ('https://wiki.funkfeuer.at/wiki/0xFF_in_der_Presse', 'Presse'),
        ('/impressum/', 'Kontakt'),
    ),
}

CONTENT_FOOTER = 'FunkFeuer Wien - Verein zur Förderung freier Netze &#8208; <a href="/impressum/">Impressum</a>'
TIMEZONE = "Europe/Vienna"

COMPILERS = {
    "markdown": ('.md', '.mdown', '.markdown'),
    "rest": ('.rst', '.txt'),
    "html": ('.html', '.htm'),
}

# Writes tag cloud data in form of tag_cloud_data.json.
# Warning: this option will change its default value to False in v8!
WRITE_TAG_CLOUD = False

IMAGE_FOLDERS = {'images': 'images'}
# IMAGE_THUMBNAIL_SIZE = 400

INDEX_TEASERS = True
# 'Read more...' for the index page, if INDEX_TEASERS is True (translatable)
INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'
# 'Read more...' for the feeds, if FEED_TEASERS is True (translatable)
FEED_READ_MORE_LINK = '<p><a href="{link}">{read_more}…</a> ({min_remaining_read})</p>'


CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}
STRIP_INDEXES = True
PRETTY_URLS = True
COPY_SOURCES = False
MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite', 'extra', 'attr_list', 'admonition']
FILE_METADATA_UNSLUGIFY_TITLES = True
ENABLE_AUTHOR_PAGES = False
COMMENT_SYSTEM = False
INDEX_PATH = "aktuelles"
ARCHIVE_PATH = "posts"

POSTS = (
    ("posts/*.rst", "posts", "post.tmpl"),
    ("posts/*.md", "posts", "post.tmpl"),
    ("posts/*.txt", "posts", "post.tmpl"),
    ("posts/*.html", "posts", "post.tmpl"),
)
PAGES = (
    ("pages/*.rst", "", "story.tmpl"),
    ("pages/*.md", "", "story.tmpl"),
    ("pages/*.txt", "", "story.tmpl"),
    ("pages/*.html", "", "story.tmpl"),
)
