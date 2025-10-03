from django.shortcuts import render
from django.utils import timezone

ARTICLES = [
    {"title": "First Steps with Django", "slug": "first-steps", "price": 0, "published": timezone.now()},
    {"title": "Template Power Moves", "slug": "template-power", "price": 49.99, "published": timezone.now()},
    {"title": "Filters, Tags & Blocks", "slug": "filters-tags-blocks", "price": 19.5, "published": timezone.now()},
]

def home(request):
    ctx = {
        "articles": ARTICLES,
        "lead": "Master inheritance, includes, filters & context processors in one mini-site."
    }
    return render(request, "pages/home.html", ctx)

def about(request):
    return render(request, "pages/about.html")

def article_detail(request, slug):
    article = next((a for a in ARTICLES if a["slug"] == slug), None)
    return render(request, "pages/article_detail.html", {"article": article})