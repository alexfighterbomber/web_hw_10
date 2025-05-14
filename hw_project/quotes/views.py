from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Author, Quote, Tag
from .forms import UserAuthorForm, UserQuoteForm, UserAuthor, UserQuote

def main(request, page=1):
    quotes = Quote.objects.all().select_related('author').prefetch_related('tags')
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)
    
    # top-10 tags
    top_tags = Tag.objects.annotate(
        num_quotes=Count('quote')
    ).order_by('-num_quotes')[:10]
    
    # font size
    if top_tags.exists():
        max_count = top_tags[0].num_quotes or 1
        for tag in top_tags:
            tag.font_size = 8 + (tag.num_quotes / max_count) * 20
    
    return render(request, "quotes/index.html", {
        'quotes': quotes_on_page,
        'top_tags': top_tags
    })

def author_detail(request, fullname):
    author = get_object_or_404(Author, fullname=fullname)
    author_quotes = Quote.objects.filter(author=author).prefetch_related('tags')
    
    top_tags = Tag.objects.annotate(
        num_quotes=Count('quote')
    ).order_by('-num_quotes')[:10]
    
    if top_tags.exists():
        max_count = top_tags[0].num_quotes or 1
        for tag in top_tags:
            tag.font_size = 8 + (tag.num_quotes / max_count) * 20
    
    return render(request, 'quotes/author_detail.html', {
        'author': author,
        'author_quotes': author_quotes,
        'top_tags': top_tags
    })

def quotes_by_tag(request, tag_name, page=1):
    tag = get_object_or_404(Tag, name=tag_name)
    quotes = Quote.objects.filter(tags__name=tag_name).select_related('author').prefetch_related('tags')
    
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)
    
    top_tags = Tag.objects.annotate(
        num_quotes=Count('quote')
    ).order_by('-num_quotes')[:10]
    
    if top_tags.exists():
        max_count = top_tags[0].num_quotes or 1
        for t in top_tags:
            t.font_size = 8 + (t.num_quotes / max_count) * 20
    
    return render(request, "quotes/quotes_by_tag.html", {
        'tag': tag,
        'quotes': quotes_on_page,
        'top_tags': top_tags
    })

@login_required
def add_user_author(request):
    if request.method == 'POST':
        form = UserAuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect('quotes:user_contributions')
    else:
        form = UserAuthorForm()
    
    return render(request, 'quotes/add_user_author.html', {'form': form})

@login_required
def add_user_quote(request):
    if request.method == 'POST':
        form = UserQuoteForm(request.user, request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            
            # Обработка тегов
            tags = [t.strip() for t in form.cleaned_data['tags'].split(',') if t.strip()]
            for tag_name in tags:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                quote.tags.add(tag)
            
            return redirect('quotes:user_contributions')
    else:
        form = UserQuoteForm(request.user)
    
    return render(request, 'quotes/add_user_quote.html', {'form': form})

@login_required
def user_contributions(request):
    authors = UserAuthor.objects.filter(user=request.user)
    quotes = UserQuote.objects.filter(user=request.user)
    return render(request, 'quotes/user_contributions.html', {
        'authors': authors,
        'quotes': quotes
    })