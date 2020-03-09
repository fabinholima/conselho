from django import forms
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Category, Post
from taggit.forms import TagWidget
from froala_editor.widgets import FroalaEditor


class PageForm(forms.ModelForm):
  content = forms.CharField(widget=FroalaEditor(options={
    'toolbarInline': True,
  }))


def make_slug(instance, new_slug=None):
    """Function for creating unique slugs"""

    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    # check if there exists a post with existing slug
    q = Post.objects.filter(slug=slug)
    if q.exists():
        new_slug = "-".join([slug, get_random_string(4, "0123456789")])
        return make_slug(instance, new_slug=new_slug)
    return slug



class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("slug", "date")
        title= forms.CharField(required=True)
        content = forms.CharField(widget=FroalaEditor(options={
    'toolbarInline': True,
  }))

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        slug = cleaned_data.get("slug")

        if not slug and title:
            cleaned_data["slug"] = slugify(title)

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = make_slug(instance)

        if commit:
            instance.save()
            self.save_m2m()
        return instance


'''
class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("slug", "date")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "required": True,
                    "placeholder": "Type your title here...",
                    "class": "form-control",
                }
            ),
            "category": forms.Select(
                attrs={"required": True, "class": "form-control"}
            ),
             "author": forms.Select(
                attrs={"required": True, "class": "form-control"}
            ),

            "context": forms.TextInput(attrs={
                "required" : True,
                "class": "form-control",
                }
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
            "tags": TagWidget(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        slug = cleaned_data.get("slug")

        if not slug and title:
            cleaned_data["slug"] = slugify(title)

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = make_slug(instance)

        if commit:
            instance.save()
            self.save_m2m()
        return instance
'''