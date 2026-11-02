from rest_framework import serializers
from .models import (Profile, AboutCard, Experience, Project, BusinessModule,
                     FrameworkTopic, ToolGroup, ContactMessage)


def split(text, sep=","):
    return [x.strip() for x in (text or "").split(sep) if x.strip()]


class ProfileSerializer(serializers.ModelSerializer):
    chips = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = "__all__"

    def get_chips(self, obj):
        return split(obj.chips, "|")


def simple(model, field_names, list_fields=()):
    """Build a small serializer; fields in list_fields are turned into lists."""
    attrs = {f: serializers.SerializerMethodField() for f in list_fields}
    for f in list_fields:
        attrs[f"get_{f}"] = (lambda name: lambda self, obj: split(getattr(obj, name)))(f)
    attrs["Meta"] = type("Meta", (), {"model": model, "fields": ["id", *field_names]})
    return type(f"{model.__name__}Serializer", (serializers.ModelSerializer,), attrs)


AboutSerializer = simple(AboutCard, ["title", "text"])
ExperienceSerializer = simple(Experience, ["role", "company", "period", "description", "tags"], ["tags"])
ProjectSerializer = simple(Project, ["title", "goal", "approach", "result", "tags", "link"], ["tags"])
ModuleSerializer = simple(BusinessModule, ["name", "description"])
FrameworkSerializer = simple(FrameworkTopic, ["title", "description"])
ToolSerializer = simple(ToolGroup, ["title", "items"], ["items"])


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
