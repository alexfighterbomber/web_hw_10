from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from .models import Author, Quote, Tag

def main(request, page=1):
    quotes = Quote.objects.all().select_related('author').prefetch_related('tags')
    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)
    
    # Получаем топ-10 тегов для боковой панели
    top_tags = Tag.objects.annotate(
        num_quotes=Count('quote')
    ).order_by('-num_quotes')[:10]
    
    # Рассчитываем размер шрифта для тегов
    if top_tags.exists():
        max_count = top_tags[0].num_quotes or 1
        for tag in top_tags:
            tag.font_size = 8 + (tag.num_quotes / max_count) * 20
    
    return render(request, "index.html", {
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
    
    return render(request, 'author_detail.html', {
        'author': author,
        'author_quotes': author_quotes,
        'top_tags': top_tags
    })