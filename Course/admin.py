from django.contrib import admin
from Course import models

# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.Content)
admin.site.register(models.Chapter)
admin.site.register(models.Review)
admin.site.register(models.Instructor)
admin.site.register(models.Course)
