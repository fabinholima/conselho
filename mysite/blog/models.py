from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
#from tinymce.models import HTMLField
from django.urls import reverse

from taggit.managers import TaggableManager

# MarkDown form to context 
#from markdownx.models import MarkdownxField
#from markdownx.utils import markdownify


class Category(models.Model):
    name = models.CharField(max_length=250)
    #slug = models.SlugField(unique=True)
    #parent = models.ForeignKey('self',blank=True, null=True ,related_name='children',on_delete= models.CASCADE)


    #def get_absolute_url(self):
    #    return reverse('category', kwargs={'slug': self.slug})
    
    class Meta:
        # app_label = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:category", kwargs={"name": self.name})


#Class for Posts Blogs 

class Post(models.Model):
    STATUS = (("DRAFT", "Draft"), ("PUBLISHED", "Published"))

    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category,on_delete= models.PROTECT)
    slug = models.SlugField(max_length=100, unique_for_date="published_date")
    author = models.ForeignKey(User, on_delete= models.PROTECT,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    #content = HTMLField()
    height=models.IntegerField(null=True, blank=True)
    width=models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='static/blog/uploads/%Y/%m/%d/', null=True, blank=True)
    caption_image = models.CharField(max_length=200, null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default="DRAFT", choices=STATUS, max_length=10)

    # tags mechanism
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:details_post", kwargs={"slug": self.slug})
#