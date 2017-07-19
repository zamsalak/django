###app'in kurulu olduğu dosyada models.py'a:
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name = "Title")
    content = models.TextField()
    publishing_date = models.DateField()
    
    def __str__(self):
      return self.title
    
###proje dosyasındaki settings.py'da, INSTALLED_APPS'e app klasör adını --> 'post', şeklinde ekle.
###ardından command prompt'a python manage.py makemigrations ve migrate
###app'in kurulu olduğu dosyada admin.py'a:
from post.models import Post
admin.site.register(Post)
