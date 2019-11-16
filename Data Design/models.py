import ipaddress
from django.db import models
import datetime
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _


def validate_email(string):
    validator = EmailValidator()
    try:
        validator(string)
    except ValidationError:
        return False
    return True


def validate_ipv4_address(value):
    try:
        ipaddress.IPv4Address(value)
    except ValueError:
        raise ValidationError(_('Enter a valid IPv4 address.'), code='invalid')


def validate_level(value):
    if value not in ['CRITICAL', 'DEBUG', 'ERROR', 'WARNING', 'INFO']:
        raise ValidationError("Invalid value.")


class User(models.Model):
    name = models.CharField('Name', max_length=50)
    last_login = models.DateTimeField(auto_now_add=True)
    email = models.CharField('Email', max_length=254,
                             validators=[validate_email])
    password = models.CharField(
        'Password', max_length=50, validators=[MinValueValidator(8)])


class Agent(models.Model):
    name = models.CharField('Name', max_length=50)
    status = models.BooleanField()
    env = models.CharField('env', max_length=20)
    version = models.CharField(max_length=5)
    address = models.TextField('address', default='', max_length=39, validators=[
                               validate_ipv4_address])


class Event(models.Model):
    level = models.CharField('level', max_length=20,
                             validators=[validate_level])
    data = models.TextField('data', default='', max_length=39)
    arquivado = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    agent = models.ForeignKey(
        Agent, on_delete=models.deletion.DO_NOTHING, default='')
    user = models.ForeignKey(
        User, on_delete=models.deletion.DO_NOTHING, default='')


class Group(models.Model):
    name = models.CharField('Name', max_length=50)


class GroupUser(models.Model):
    group = models.ForeignKey(
        Group, on_delete=models.deletion.DO_NOTHING, default='')
    user = models.ForeignKey(
        User, on_delete=models.deletion.DO_NOTHING, default='')
