from django.urls import path , include, re_path
from .views import *

app_name='blog'


urlpatterns = [
    

    path("", ListPosts.as_view(), name="index"),
    
     
    path("add/", AddPost.as_view(), name="add_post"),
    #path("add/drafts/", PostDraftsList.as_view(), name="list_drafts"),
    #path("search/", SearchPosts.as_view(), name="search"),
    # post archives
    #path("<int:year>/", PostYearArchive.as_view(), name="y_archive"),
    #path(
    #    "<int:year>/<int:month>/",
    #    PostYearMonthArchive.as_view(month_format="%m"),
    #    name="ym_archive",
    #),
    path("tag/<str:tag>/", ListByTag.as_view(), name="tag"),
    path("category/<str:name>/", ListByCategory.as_view(), name="category"),
    #path("author/<str:author>/", ListByAuthor.as_view(), name="author"),
    path("<slug:slug>/", DetailsPost.as_view(), name="details_post"),
    path("<slug:slug>/delete/", DeletePost.as_view(), name="delete_post"),
    #path("<slug:slug>/update/", UpdatePost.as_view(), name="update_post"),

    ##My views
	#path('', views.PostList.as_view(), name='home'),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    #path('cat', views.CategoryViewAll.as_view(), name='cat'),
    #path('category/<str:slug>', CategoryList.as_view(), name='category'),
    path('search', SearchView.as_view(), name='search'),
    #path('about', about_view, name='about' ),
    path('contact', emailView, name='contact' ), 
    

    
]