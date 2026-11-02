from django.contrib import admin
from .models import (Profile, AboutCard, Experience, Project, BusinessModule,
                     FrameworkTopic, ToolGroup, ContactMessage)

for m in (Profile, AboutCard, Experience, Project, BusinessModule, FrameworkTopic, ToolGroup):
    admin.site.register(m)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created")
    readonly_fields = ("created",)
