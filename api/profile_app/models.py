from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    also_known_as = models.CharField(max_length=100, blank=True, help_text="Name used at work")
    role = models.CharField(max_length=200)
    availability = models.CharField(max_length=200, blank=True)
    intro = models.TextField()
    chips = models.CharField(max_length=400, blank=True, help_text="Separate with |")
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    github = models.URLField(blank=True)
    gitlab = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    degree = models.CharField(max_length=200, blank=True)
    institution = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Ordered(models.Model):
    order = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ["order"]


class AboutCard(Ordered):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title


class Experience(Ordered):
    role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    period = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=200, blank=True, help_text="Comma separated")

    def __str__(self):
        return f"{self.role} - {self.company}"


class Project(Ordered):
    title = models.CharField(max_length=200)
    goal = models.TextField(blank=True)
    approach = models.TextField(blank=True)
    result = models.TextField(blank=True)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma separated")
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class BusinessModule(Ordered):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class FrameworkTopic(Ordered):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.title


class ToolGroup(Ordered):
    title = models.CharField(max_length=100)
    items = models.TextField(help_text="Comma separated")

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name} <{self.email}>"
