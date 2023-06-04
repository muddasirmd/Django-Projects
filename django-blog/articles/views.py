from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):

    articles = Article.objects.all().order_by('date')
    # return HttpResponse(articles[0].body)
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})

@login_required(login_url="/accounts/login")
def create_article(request):

    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            article = form.save(commit=False) # Don't save it, first attach user then save it
            article.author = request.user
            article.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    
    return render(request, 'articles/create_article.html', {'form': form})