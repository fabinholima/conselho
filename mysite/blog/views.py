from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Post, Category
from taggit.models import Tag

from .forms import AddPostForm

from .forms import ContactForm

# complex lookups (for searching)
from django.db.models import Q

from django.urls import reverse_lazy

# class based views
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView

from django.views import View
from django.utils.decorators import method_decorator

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

from django.views.generic.dates import YearArchiveView, MonthArchiveView, DayArchiveView

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
    PermissionRequiredMixin,
)

from django.db import transaction



### Form contact 

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
    return render(request, "blog/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')




class CategoryDatesMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        # get queryset of datetime objects for all published posts
        context["dates"] = Post.objects.filter(status="PUBLISHED").datetimes(
            field_name="published_date", kind="month", order="DESC"
        )
        context["recent_posts"] = Post.objects.filter(status="PUBLISHED").order_by(
            "-published_date"
        )[:3]
        return context


def about_view(request): 
    # render function takes argument  - request 
    # and return HTML as response 
    return render(request, "blog/about.html") 

#class About(generic.AboutView):
#    templeate_name= 'about.html'



class ListPosts(CategoryDatesMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    paginate_by = 2
    #ordering= ("-published_date",)
    #queryset = Post.objects.filter(status=1).order_by('-published_date')
    #queryset = Post.objects.filter(status=1).order_by('-category')




class ListByAuthor(CategoryDatesMixin, ListView):
    model = Post
    context_object_name = "posts"
    template_name = "posts/post_by_author.html"
    paginate_by = 5
    ordering = ("-published_date",)

    def get_queryset(self):
        author = self.kwargs.get("author", None)
        results = []
        if author:
            results = Post.objects.filter(author__username=author)
        return results

    def get_context_data(self, **kwargs):
        """
        Pass author's name to the context
        """
        context = super().get_context_data(**kwargs)
        context["author"] = self.kwargs.get("author", None)
        return context


class ListByTag(CategoryDatesMixin, ListView):
    model = Post
    context_object_name = "blog"
    template_name = "blog/post_by_tag.html"
    paginate_by = 5
    ordering = ("-published_date",)

    def get_queryset(self):
        tag = self.kwargs.get("tag", None)
        results = []
        if tag:
            results = Post.objects.filter(tags__name=tag)
        return results

    def get_context_data(self, **kwargs):
        """
        Pass tag name to the context
        """
        context = super().get_context_data(**kwargs)
        context["tag"] = self.kwargs.get("tag", None)
        return context



class ListByCategory(CategoryDatesMixin, ListView):
    model = Post
    #context_object_name = "blog"
    template_name = "blog/post_by_category.html"
    paginate_by = 5
    ordering = ("-published_date",)

    def get_queryset(self):
        category = self.kwargs.get("name", None)
        results = []
        if category:
            results = Post.objects.filter(category__name=category)
        return results

    def get_context_data(self, **kwargs):
        """
        Pass category's name to the context
        """
        context = super().get_context_data(**kwargs)
        context["category"] = self.kwargs.get("name", None)
        return context
 





class DetailsPost(CategoryDatesMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'




# Post archive views
class ArchiveMixin:
    model = Post
    date_field = "published_date"
    allow_future = False
    context_object_name = "posts"

############# Update Blog


class AddPost( #CategoryDatesMixin, PermissionRequiredMixin, LoginRequiredMixin, 
    CreateView
):
    form_class = AddPostForm
    permission_required = "posts.add_post"
    template_name = "blog/addpost.html"

class DeletePost( #CategoryDatesMixin, LoginRequiredMixin, UserPassesTestMixin, 
    DeleteView
):
    model = Post
    success_url = reverse_lazy("blog:index")

    def test_func(self):
        """
        Only let the user delete object if they own the object being deleted
        """
        return self.get_object().author.username == self.request.user.username






############ Busca no Blog 

class SearchView(ListView):
    template_name = 'blog/search.html'
    model = Post
    paginate_by = 5
    ordering = ("-published_date",)
        
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(Q(content__icontains=query)|Q(title__icontains=query))
            
        else:
            return Post.objects.all()
            
  

