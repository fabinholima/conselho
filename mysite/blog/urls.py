from . import views
from django.urls import path
from .views import about_view, emailView, Genre 
from blog.views import *
#from django.views.generic import TemplateView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    #path('', views.CategoryList.as_view(), name='category'),
    #path('category', show_menu, name='nodes'),
    path('search', searchview, name='search'),
    path('about', about_view, name='about' ),
    path('contact', emailView, name='contact' ), 
    #path('genres', GenreListView.as_view(), name='genres'),

]