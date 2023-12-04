from django.db import models
from django.utils.html import format_html 
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.

#category model

class Category(models.Model):
    cat_id= models.AutoField(primary_key=True,db_column="cid")
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField(upload_to='image')
    add_date=models.DateTimeField(auto_now_add=True,null=True)
    is_active = models.BooleanField(default=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;"/>'.format(self.image))

    def __str__(self):
        return self.title  

#Post Model

class Post(models.Model):
    
    #CAT=((cat_ob[0],'Food'),(cat_ob[1],'Health'),(cat_ob[2],'Sports'),(cat_ob[3],'Technology'))
    post_id = models.AutoField(primary_key=True,db_column="pid")
    title=models.CharField(max_length=200)
    content=HTMLField()
    #url=models.CharField(max_length=100)
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
   
    image=models.ImageField(upload_to='image')
    is_active = models.BooleanField(default=True)

    def image_tag1(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;"/>'.format(self.image))

    def __str__(self):
        return self.title


class Save(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    pid=models.ForeignKey(Post,on_delete=models.CASCADE,db_column="pid")

 

 




