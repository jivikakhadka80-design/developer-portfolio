import logging
from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from . import models as m
from . import serializers as s


class PortfolioView(APIView):
    """GET /api/portfolio/ - everything the React page needs in one request."""

    def get(self, request):
        profile = m.Profile.objects.first()

        def many(serializer, model):
            return serializer(model.objects.all(), many=True).data

        return Response({
            "profile": s.ProfileSerializer(profile).data if profile else None,
            "about": many(s.AboutSerializer, m.AboutCard),
            "experience": many(s.ExperienceSerializer, m.Experience),
            "projects": many(s.ProjectSerializer, m.Project),
            "modules": many(s.ModuleSerializer, m.BusinessModule),
            "framework": many(s.FrameworkSerializer, m.FrameworkTopic),
            "tools": many(s.ToolSerializer, m.ToolGroup),
        })


class ContactView(CreateAPIView):
    """POST /api/contact/ - saves the message and emails it to you."""
    serializer_class = s.ContactSerializer

    def perform_create(self, serializer):
        msg = serializer.save()  # always saved, so it shows in /admin even if email fails
        try:
            EmailMessage(
                subject=f"Portfolio message from {msg.name}",
                body=f"From: {msg.name} <{msg.email}>\n\n{msg.message}",
                from_email=settings.EMAIL_HOST_USER or None,
                to=[settings.CONTACT_RECEIVER],
                reply_to=[msg.email],
            ).send()
        except Exception:
            logging.getLogger(__name__).exception("Contact email could not be sent")
