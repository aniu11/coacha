from django.contrib import admin
from wow.models import Wower
from wow.models import Arriving
from wow.models import Notice
from wow.models import Comment

# Register your models here.
admin.site.register(Wower)
admin.site.register(Arriving)
admin.site.register(Notice)
admin.site.register(Comment)