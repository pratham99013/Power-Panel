from django.contrib import admin
from .models import Tweet, Question, Reply
# Register your models here.

admin.site.register(Tweet)
admin.site.register(Question)
admin.site.register(Reply)
