from django.core import mail
from django.test import TestCase
from .models import Profile, Project, ToolGroup


class ApiTests(TestCase):
    def setUp(self):
        Profile.objects.create(name="Test", role="Dev", intro="x", email="a@b.com", chips="One|Two, three")
        Project.objects.create(title="P", tags="Odoo, Python")
        ToolGroup.objects.create(title="T", items="A, B")

    def test_portfolio_endpoint(self):
        data = self.client.get("/api/portfolio/").json()
        self.assertEqual(data["profile"]["chips"], ["One", "Two, three"])
        self.assertEqual(data["projects"][0]["tags"], ["Odoo", "Python"])
        self.assertEqual(data["tools"][0]["items"], ["A", "B"])

    def test_contact_saves_and_emails(self):
        r = self.client.post("/api/contact/", {"name": "A", "email": "a@b.com", "message": "Hi"})
        self.assertEqual(r.status_code, 201)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].reply_to, ["a@b.com"])

    def test_contact_rejects_bad_email(self):
        r = self.client.post("/api/contact/", {"name": "A", "email": "bad", "message": "Hi"})
        self.assertEqual(r.status_code, 400)
