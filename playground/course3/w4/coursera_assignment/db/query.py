from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from models import User, Blog, Topic


def create():
    u1 = User(first_name='u1', last_name='u1')
    u1.save()
    u2 = User(first_name='u2', last_name='u2')
    u2.save()
    u3 = User(first_name='u3', last_name='u3')
    u3.save()
    blog1 = Blog(title='blog1', author_id=User.objects.filter(first_name='u1')[0].id)
    blog1.author = u1
    blog1.save()
    blog2 = Blog(title='blog2', author_id=User.objects.filter(first_name='u1')[0].id)
    blog2.author = u1
    blog2.save()

    blog1.subscribers.add(u1)
    blog2.subscribers.add(u2)


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

print(User.objects)