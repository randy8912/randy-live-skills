from django.contrib import admin
from django.utils.html import format_html
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("thumb", "title", "slug", "created", "updated")
    list_display_links = ("thumb", "title")
    list_filter = ("created", "updated")
    search_fields = ("title", "intro", "slug", "tech_stack")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("preview", "created", "updated")

    fieldsets = (
        ("Basis", {"fields": ("title", "slug", "intro")}),
        ("Media", {"fields": ("image", "preview")}),
        ("Links", {"fields": ("github_url", "demo_url")}),
        ("Extra", {"fields": ("tech_stack",)}),
        ("Meta", {"fields": ("created", "updated")}),
    )

    def thumb(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:32px;width:32px;object-fit:cover;border-radius:6px;" />', obj.image.url)
        return "—"
    thumb.short_description = "Img"

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:180px;border-radius:10px;" />', obj.image.url)
        return "—"
    preview.short_description = "Preview"