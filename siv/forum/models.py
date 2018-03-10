from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class WorryUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.BigIntegerField(primary_key=True)
    user_name = models.CharField(default='USERNAME', max_length=100, null=False)
    date_created = models.DateTimeField(default=timezone.now)


class WorryCategory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    observation = models.CharField(default='OBSERVATION', max_length=200, null=False)
    description = models.CharField(max_length=1000, null=True)


class WorryType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    observation = models.CharField(default='OBSERVATION', max_length=200, null=False)
    description = models.CharField(max_length=1000, null=True)


class WorryMessage(models.Model):
    id = models.BigIntegerField(primary_key=True)
    worry_category = models.ForeignKey(WorryCategory, on_delete=models.CASCADE)
    worry_type = models.ForeignKey(WorryType, on_delete=models.CASCADE)
    worry_message = models.TextField(default='MY EXPERIENCE', null=False)
    publish_date = models.DateTimeField(default=timezone.now)
    message_updated = models.DateTimeField(null=True, blank=True)
    # PUBLISHED, DELETED, UPDATED, REPORTED, REASSIGNED
    status_message = models.CharField(default='PUBLISHED', max_length=50, null=False)


class OpinionMessage(models.Model):
    id = models.BigIntegerField(primary_key=True)
    opinion_message = models.TextField(default='MY OPINION', null=False)
    publish_date = models.DateTimeField(default=timezone.now)
    opinion_updated = models.DateTimeField(null=True, blank=True)
    # PUBLISHED, DELETED, UPDATED, REPORTED, INACTIVE
    status_opinion = models.CharField(default='PUBLISHED', max_length=50, null=False)
    grade_opinion = models.BigIntegerField(default=0, null=False)


class UserAction(models.Model):
    id = models.BigIntegerField(primary_key=True)
    worry_user = models.ForeignKey(WorryUser, on_delete=models.CASCADE)
    worry_message = models.ForeignKey(WorryMessage, on_delete=models.CASCADE, null=True, blank=True)
    opinion_message = models.ForeignKey(OpinionMessage, on_delete=models.CASCADE, null=True, blank=True)
    # PUBLISH, RESPONSE, UPDATE, DELETE, VOTE, REPORT, REASSIGN
    action = models.CharField(default='PUBLISH', max_length=50, null=False)
    action_date = models.DateTimeField(default=timezone.now)


class MessageRecord(models.Model):
    id = models.BigIntegerField(primary_key=True)
    worry_message = models.ForeignKey(WorryMessage, on_delete=models.CASCADE)
    opinion_message = models.ForeignKey(OpinionMessage, on_delete=models.CASCADE)
    record_date = models.DateTimeField(default=timezone.now)


class ConfigurationPreference(models.Model):
    id = models.BigIntegerField(primary_key=True)
    worry_user = models.ForeignKey(WorryUser, on_delete=models.CASCADE)
    worry_category = models.ForeignKey(WorryCategory, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    status_configuration = models.CharField(default='ACTIVE', max_length=50, null=False)  # ACTIVE, INACTIVE
