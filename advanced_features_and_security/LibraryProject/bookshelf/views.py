from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .forms import ArticleForm

@permission_required('relationship_app.can_view', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'relationship_app/article_list.html', {'articles': articles})

@permission_required('relationship_app.can_create', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'relationship_app/article_form.html', {'form': form})

@permission_required('relationship_app.can_edit', raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('article_list')
    return render(request, 'relationship_app/article_form.html', {'form': form})

@permission_required('relationship_app.can_delete', raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'relationship_app/article_confirm_delete.html', {'article': article})
