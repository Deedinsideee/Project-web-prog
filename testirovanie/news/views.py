from django.db.models import Q
from django.shortcuts import render, redirect,get_object_or_404
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import  ListView
from django.views.generic import DetailView, UpdateView, DeleteView, RedirectView


def news_home(request):
    news = Articles.objects.order_by('-time')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDeleteVeiw(DeleteView):
    model = Articles
    template_name ='news/news-delete.html'
    success_url = '/news'

class NewsDetailVeiw(DetailView):

    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'
    def updatecounter(self, *args, **kwargs):
        article = get_object_or_404(Articles, pk=kwargs['pk'])
        article.update_counter()
        return True






class NewsUpdateVeiw(RedirectView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm

class ArticleCounterRedirectView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Articles, pk=kwargs['pk'])
        article.update_counter()
        return article.id


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news')
        else:
            error = 'Неправильно заполнил!!!'

    form = ArticlesForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)


class SearchResultsView(ListView):
    model = Articles
    template_name = 'news/search_result.html'

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Articles.objects.filter(
            Q(title__icontains=query)
        )
        return object_list
