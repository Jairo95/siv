from django.contrib import admin
from forum.models import WorryUser, WorryCategory, WorryType
from forum.models import WorryMessage, OpinionMessage, UserAction, MessageRecord, ConfigurationPreference

# Register your models here.

admin.site.register(WorryUser)
admin.site.register(WorryCategory)
admin.site.register(WorryType)
admin.site.register(WorryMessage)
admin.site.register(OpinionMessage)
admin.site.register(MessageRecord)
admin.site.register(UserAction)
admin.site.register(ConfigurationPreference)
