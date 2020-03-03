from django.contrib import admin
from django import forms
# Register your models here.
from .models import Post, Category
#from ckeditor.widgets import CKEditorWidget
from tinymce.models import HTMLField


from mce_filebrowser.admin import MCEFilebrowserAdmin



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title','image', 'content']
    prepopulated_fields = {'slug': ('title',)}
  

class CategoriaAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug': ('titulo',)}



class PostAdminForm(forms.ModelForm):
    #content = forms.CharField(widget=CKEditorWidget())
    content = HTMLField('Content')    
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

#class Post  
class MyModelAdmin(MCEFilebrowserAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
