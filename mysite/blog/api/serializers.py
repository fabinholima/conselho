
from django.contrib.auth.models import User
from django.utils.text import slugify
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from blog.models import Post, Category