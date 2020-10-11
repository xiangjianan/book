from django.db import models


# Create your models here.


class Author(models.Model):
    a_id = models.AutoField(primary_key=True)
    auth_name = models.CharField(max_length=20)


class Publish(models.Model):
    p_id = models.AutoField(primary_key=True)
    pub_name = models.CharField(max_length=20)


class Book(models.Model):
    b_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=20, unique=True)  # 书名不重复
    # 一对多
    pub = models.ForeignKey(to='Publish', to_field='p_id',on_delete=models.CASCADE)
    # 多对多
    auth = models.ManyToManyField(to='Author')
