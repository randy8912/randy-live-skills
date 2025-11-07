from django.db import models
from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=220)
    intro = models.TextField(blank=True)

    # Nieuwe velden
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    tech_stack = models.CharField(max_length=250, blank=True, help_text="Bijv: Python, Django, Tailwind")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("project-detail", args=[self.slug])