from django.contrib.auth.models import User
from django.db import models


class WorryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.BigIntegerField(primary_key=True, unique=True, auto_created=True)
    user_name = models.CharField(max_length=100)


class WorryCategory(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, auto_created=True)
    name = models.CharField(max_length=100)


class WorryType(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, auto_created=True)
    name = models.CharField(max_length=100)


class UserAction(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, auto_created=True)
    worry_user = models.ForeignKey(WorryUser, on_delete=models.CASCADE)


class WorryMessage(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, auto_created=True)
    worry_category = models.ForeignKey(WorryCategory, on_delete=models.CASCADE)
    worry_type = models.ForeignKey(WorryType, on_delete=models.CASCADE)
    user_action = models.ForeignKey(UserAction, on_delete=models.CASCADE)


class OpinionMessage(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True, auto_created=True)
    user_action = models.ForeignKey(UserAction, on_delete=models.CASCADE)


class MessageRecord(models.Model):
    worry_message = models.ForeignKey(WorryMessage, on_delete=models.CASCADE)
    opinion_message = models.ForeignKey(OpinionMessage, on_delete=models.CASCADE)


class ConfigurationPreference(models.Model):
    worry_user = models.ForeignKey(WorryUser, on_delete=models.CASCADE)
    worry_category = models.ForeignKey(WorryCategory, on_delete=models.CASCADE)


