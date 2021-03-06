from django import template
from article.models import ArticlePost
from django.db.models import Count


register = template.Library()


@register.simple_tag
def total_articles():
    return ArticlePost.objects.count()


@register.simple_tag
def author_total_articles(user):
    return user.article.count()


@register.inclusion_tag('article/list/latest_articles.html')
def latest_articles(n=5):
    latest_article = ArticlePost.objects.order_by("-created")[:n]
    return {"latest_article": latest_article}


@register.simple_tag
def most_comment_articles(n=3):
    return ArticlePost.objects.annotate(
        total_comments=Count('comments')).order_by("-total_comments")[:n]
