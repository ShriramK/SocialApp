from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

class SocialUser(models.Model):
	username = models.CharField(max_length=40)
	recentMessage = models.TextField(max_length=10000, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	creator = models.ForeignKey(User, blank=True, null=True)

	def short(self):
		pass
	short.allow_tags = True

### Admin 

class SocialUserAdmin(admin.ModelAdmin):
	list_display = ["creator", "created", "recentMessage", "username"]

admin.site.register(SocialUser, SocialUserAdmin)
	