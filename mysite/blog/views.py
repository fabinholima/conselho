from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.views.generic.list import ListView
# Create your views here.
from django.views.generic import CreateView
from .models import Post, Category, Menu, Genre
from .forms import ContactForm
from django.db.models import Q


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['flima21@me.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')


def about_view(request): 
    # render function takes argument  - request 
    # and return HTML as response 
    return render(request, "about.html") 

#class About(generic.AboutView):
#    templeate_name= 'about.html'




class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'
    #template_name = 'category.html'
    paginate_by = 2
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    #queryset = Post.objects.filter(status=1).order_by('-category')

    
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'




class SearchPostsView(ListView):
    model = Post
    template_name = 'blog_search.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list


#class CategoryList(generic.ListView):
#    queryset=Post.objects.filter(status=1).order_by('-category')
#    template_name= 'category.html'


class GenreListView(ListView):
    model = Genre
    template_name = 'category.html'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()

        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = len(self.object_list) == 0
            if is_empty:
                from django.http import Http404
                raise Http404(("Empty list and '%(class_name)s.allow_empty' is False.") % {
                    'class_name': self.__class__.__name__,
                })
        context = self.get_context_data()
        context['nodes'] = context.get('object_list')
        import pdb; pdb.set_trace()
        return self.render_to_response(context)


class CategoryView(CreateView):
    model=Category
    fields = ('name')


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'category', 'slug', 'author', 'updated_on', 'content', 'image', 'created_on', 'status')
