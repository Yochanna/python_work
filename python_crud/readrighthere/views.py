from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Article
from .forms import ArticleForm

def article_list(request):
    search_query = request.GET.get('q', '')
    if search_query:
        articles = Article.objects.filter(title__icontains=search_query) | Article.objects.filter(content__icontains=search_query)
    else:
        articles = Article.objects.all().order_by('-created')

    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'readrighthere/article_list.html', {'page_obj': page_obj, 'search_query': search_query})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'readrighthere/article_detail.html', {'article': article})

def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'readrighthere/article_form.html', {'form': form})

def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'readrighthere/article_form.html', {'form': form})

def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('article_list')
    return render(request, 'readrighthere/article_confirm_delete.html', {'article': article})
