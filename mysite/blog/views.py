from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.
from django.views.generic import CreateView
from .models import Post, Category
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




class SearchView(ListView):
    template_name = 'search.html'
    model = Post
        
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
            
        else:
            return Post.objects.all()
            
  
class CategoryViewAll(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'
    def menu(request):
        return {
            'category':Category.objects.all().order_by('-name')
    }

 
class CategoryView(ListView):
    """
    Displays the list of posts in a given category
    Template: ``blog_posts_list.html``
    Specific context variables:
    - ``posts``
    - ``page_title``
    """
    model = Post
    template_name = 'post_list.html'
    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        self.page_title = _('Posts in "{0}" category'.format(category.name))
        return Post.objects.published().filter(categories__pk=category.pk)




class CategoryListView(ListView):
    """
    Displays the list of categories that have posts in them
    Template: ``blog_categories_list.html``
    Specific context variables:
    - ``categories``
    """
    template_name = 'category.html'
    queryset = Category.objects.all()
    context_object_name = 'category'





#---------------------------
# Class for add Posts
#
class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'category', 'slug', 'author', 'updated_on', 'content', 'image', 'created_on', 'status')


#================
#  Class for delete 
#