from django.contrib import admin
from profile_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.UserFeedItem)
# Register your models here.
