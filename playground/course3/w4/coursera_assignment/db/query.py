import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'D:\Python\Git\Python_Programming\playground\course3\w4\coursera_assignment\grader\settings.py')
import django
django.setup()

from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from models import User, Blog, Topic


def create():
    for fn, sn in [('u1', 'u1'), ('u2', 'u2'), ('u3', 'u3')]:
        user = User(first_name=fn, last_name=sn)
        user.save()


def edit_all():
    pass


def edit_u1_u2():
    pass


def delete_u1():
    pass


def unsubscribe_u2_from_blogs():
    pass


def get_topic_created_grated():
    pass


def get_topic_title_ended():
    pass


def get_user_with_limit():
    pass


def get_topic_count():
    pass


def get_avg_topic_count():
    pass


def get_blog_that_have_more_than_one_topic():
    pass


def get_topic_by_u1():
    pass


def get_user_that_dont_have_blog():
    pass


def get_topic_that_like_all_users():
    pass


def get_topic_that_dont_have_like():
    pass