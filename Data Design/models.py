from django.db import models
import datetime


class User(models.Model):
    name = models.CharField('Name', max_length=50)
    last_login = models.DateTimeField(auto_now_add=True)
    email = models.CharField('Email', max_length=254)
    password = models.CharField('Password', max_length=50)
    #raise NotImplementedError
    def __str__(self):
        return f'{self.name}'


class Agent(models.Model):
    name = models.CharField('Name', max_length=50)
    status = models.BooleanField()
    env = models.CharField('env', max_length=20)
    version = models.CharField(max_length=5)
    address = models.TextField('address', default='', max_length=39)

    
class Event(models.Model):
    level = models.CharField('level', max_length=20)
    data = models.TextField('data', default='', max_length=39)
    arquivado = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    agent = models.ForeignKey(Agent, on_delete=models.deletion.DO_NOTHING, default='')
    user = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING,default='')


class Group(models.Model):
    name = models.CharField('Name', max_length=50)

    
class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.deletion.DO_NOTHING,default='')
    user = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING,default='')
