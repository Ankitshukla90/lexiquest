from django.contrib import admin
from .models import Lesson, Badge, UserBadge, Quiz

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Badge)
admin.site.register(UserBadge)
admin.site.register(Quiz)
