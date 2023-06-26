from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .filters import PostFilter
from datetime import datetime
from .forms import PostForm
from django.urls import reverse_lazy


# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'one_news.html'
    context_object_name = 'one_news'

    def get_context_data(self, **kwargs):
        context = super(NewsDetail, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        return context


class SearchNewsList(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search_news'
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


# def create_post(request):
#    form = PostForm()
#    if request.method == 'POST':
#        form = PostForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect('/news/')
#    return render(request, 'post_create.html', {'form': form})

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if 'news' in self.request.path:
            post_type = 'NE'
        elif 'article' in self.request.path:
            post_type = 'AR'
        self.object.post_type = post_type
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')
