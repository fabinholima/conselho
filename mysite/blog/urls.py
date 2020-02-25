from . import views
from django.urls import path , include, re_path
from .views import about_view, emailView
from blog.views import *
from django.views.generic import TemplateView

urlpatterns = [
    
	path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('cat', views.CategoryViewAll.as_view(), name='cat'),
    path('categories/<slug>', CategoryView.as_view(), name='category'),
    #re_path(r'^categories/$', CategoryListView.as_view(), name='categories_list'),
    path('search', SearchView.as_view(), name='search'),
    path('about', about_view, name='about' ),
    path('contact', emailView, name='contact' ), 

    #path('genres', GenreListView.as_view(), name='genres'),

]