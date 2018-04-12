from django.db import models


class News(models.Model):
    class Meta():
        db_table = 'news'

    news_title = models.CharField(max_length=120)
    news_likes = models.IntegerField(default=0)
    news_text = models.TextField()
    news_date = models.DateTimeField()

class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comments_text = models.TextField()
    comments_news = models.ForeignKey(News, on_delete=models.CASCADE)