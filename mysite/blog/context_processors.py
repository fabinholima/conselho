from .models import Post, Category

def category_view(request): 
    apps = Category.objects.all()
    return {'apps': apps}
    