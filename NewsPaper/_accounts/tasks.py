from celery import shared_task
from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.core.mail import send_mail
from datetime import datetime, timedelta
from django.utils import timezone

from _accounts.models import Post, UserCategory, Category


@shared_task
def post_of_last_week():
    prew_week = datetime.now(tz=timezone.utc) - timedelta(7)
    last_week = Post.objects.filter(time__gte=prew_week)
    category_set = set()
    for post in last_week:
        for cat in post.categories.values('name'):
            category_set.add(cat.get('name'))
    for category in category_set:
        email_subject = f'Посты за прошлую неделю в категории {category}'
        user_emails = get_subs(category)
        email_message = f''
        for post in Post.objects.filter(time__gte=prew_week, categories__name=category):
            email_message += f"{post.title} \n Подробнее: 127.0.0.1:8000/news/{post.id}\n"
        send_mail(
            subject=email_subject,
            message=email_message,
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=user_emails
        )



def get_subs(category):
    subs_emails = []
    for user in UserCategory.objects.filter(category__name=category).values('user__email'):
        subs_emails.append(user.get('user__email'))
    return subs_emails




def new_post_add():
    new_post = Post.objects.all().order_by('-time').first()
    if new_post:
        for category in new_post.categories.all():
            email_subject = f'Новый пост в категории {category}'
            email_message = f'{new_post.title}\n Подробнее: 127.0.0.1:8000/news/{new_post.id}'
            user_emails = get_subs(category)
            send_mail(
                subject=email_subject,
                message=email_message,
                from_email=DEFAULT_FROM_EMAIL,
                recipient_list=user_emails
            )

