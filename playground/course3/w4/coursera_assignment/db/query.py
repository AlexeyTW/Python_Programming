from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC
'''
for objs in [User.objects.all(), Blog.objects.all(), Topic.objects.all()]:
    for obj in objs:
        obj.delete()
'''
from models import User, Blog, Topic


def create():
    u1 = User(first_name='u1', last_name='u1')
    u1.save()
    u2 = User(first_name='u2', last_name='u2')
    u2.save()
    u3 = User(first_name='u3', last_name='u3')
    u3.save()
    blog1 = Blog(title='blog1')
    blog1.author = u1
    blog1.save()
    blog2 = Blog(title='blog2')
    blog2.author = u1
    blog2.save()

    blog1.subscribers.add(u1, u2)
    blog2.subscribers.add(u2)

    t1 = Topic(title='topic1')
    t1.author = u1
    t1.blog = blog1
    t1.save()
    t2 = Topic(title='topic2_content', created='2017-01-01')
    t2.author = u3
    t2.blog = blog1
    t2.save()

    t2.likes.add(u1)
    t2.likes.add(u2)
    t2.likes.add(u3)


def edit_all():
    for obj in User.objects.all():
        obj.first_name = 'uu1'
        obj.save()


def edit_u1_u2():
    q = User.objects.filter(Q(first_name='u1') | Q(first_name='u2'))
    for obj in q:
        obj.first_name = 'uu1'
        obj.save()

def delete_u1():
    q = User.objects.filter(first_name='u1')
    q.delete()


def unsubscribe_u2_from_blogs():
    u2_users = User.objects.filter(first_name='u2')
    for blog in Blog.objects.all():
        for user in u2_users:
            blog.subscribers.remove(user)


def get_topic_created_grated():
    return Topic.objects.filter(created__gt = '2018-01-01')


def get_topic_title_ended():
    return Topic.objects.filter(title__iendswith = 'content')


def get_user_with_limit():
    sorted_users = User.objects.all().order_by('id')[::-1][:2]
    return sorted_users


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