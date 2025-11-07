from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from projects.models import Project

def home(request):
    projects = Project.objects.all().order_by("-created")[:6]
    return render(request, "home.html", {"projects": projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)

    # Prev/Next op basis van aanmaakdatum
    newer = Project.objects.filter(created__gt=project.created).order_by("created").first()
    older = Project.objects.filter(created__lt=project.created).order_by("-created").first()

    # Eenvoudige related op basis van eerste tech-term
    techs = [t.strip() for t in (project.tech_stack or "").split(",") if t.strip()]
    related = Project.objects.none()
    if techs:
        related = (
            Project.objects
            .filter(tech_stack__icontains=techs[0])
            .exclude(pk=project.pk)
            .order_by("-created")[:3]
        )

    ctx = {
        "project": project,
        "older": older,
        "newer": newer,
        "related": related,
    }
    return render(request, "projects/detail.html", ctx)

def project_list(request):
    query = request.GET.get("q", "")
    tech = request.GET.get("tech", "")
    sort = request.GET.get("sort", "new")

    qs = Project.objects.all()

    if query:
        qs = qs.filter(title__icontains=query) | qs.filter(intro__icontains=query)

    if tech:
        qs = qs.filter(tech_stack__icontains=tech)

    if sort == "old":
        qs = qs.order_by("created")
    elif sort == "title":
        qs = qs.order_by("title")
    else:
        qs = qs.order_by("-created")

    paginator = Paginator(qs, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "projects/list.html",
        {
            "projects": page_obj,
            "query": query,
            "tech": tech,
            "sort": sort,
            # 👇 deze drie zijn om de template dom te houden
            "is_sort_new": sort == "new",
            "is_sort_old": sort == "old",
            "is_sort_title": sort == "title",
        },
    )

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")