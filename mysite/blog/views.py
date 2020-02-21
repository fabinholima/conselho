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
from operator import attrgetter

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

#
class CategoryView(CreateView):
    model=Category
    fields = ('name')

#
class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'category', 'slug', 'author', 'updated_on', 'content', 'image', 'created_on', 'status')

def searchview(request):
    context= {}
    query= ""
    if request.GET:
        query=request.GET['q']
        context['query']=str(query)
        posts = sorted(Post.objects.all(), key=attrgetter('created_on'), reverse=True)
        context['post']=posts
        return render(request, 'blog_search.html', context)


def search(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts= Post.objects.filter(
            Q(title__icontains=q) |
            Q(body__icontains=q)
            ).distinct()

        for post in posts:
            queryset.append(post)
        return list(set(queryset))
