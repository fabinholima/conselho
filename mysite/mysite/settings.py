"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')@@(x+o))-ylp=#7f6yu#6j5fw2uy(7pgg4@4)a*=011749==d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    #grappelli',
    #'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    #'ckeditor',
    #'ckeditor_uploader',
    #'tinymce',
 #   'sorl.thumbnail',
 #   'mce_filebrowser',
    'froala_editor',
     'blog',
     'taggit',
     'taggit_templatetags2',
     'rest_framework'

     
    
]




## Config para authethication
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

#FROALA_EDITOR_OPTIONS =('.selector', {heightMax: 500})

FRAOLA_EDITOR_THIRD_PARTY = ('image_aviary', 'spell_checker')

FROALA_EDITOR_PLUGINS = ('align', 'char_counter', 'code_beautifier' ,'code_view', 'colors', 'draggable', 'emoticons',
        'entities', 'file', 'font_family', 'font_size', 'fullscreen', 'image_manager', 'image', 'inline_style',
        'line_breaker', 'link', 'lists', 'paragraph_format', 'paragraph_style', 'quick_insert', 'quote', 'save', 'table',
        'url', 'video')



#FROALA_UPLOAD_PATH="/media/froala/"

#USE_FROALA_EDITOR=True

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "/media/uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
#CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, "ckeditor")
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_UPLOAD_SLUGIFY_FILENAME= False
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 500,
        'width': 'full',
        'mathJaxLib': '//cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [   
                'image',
                'div',
                'autolink',
                'autogrow',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath',
                'mathjax',
                'embed',
                'codesnippet',
                'image2',
                'imagebrowser',

            ]
       ),
    
    },
}


CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'

 
CKEDITOR_IMAGE_BACKEND = "pillow"


CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processors.category_view',
            ],
        },
    },
]
WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


## PostgreSQL
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
''' 


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


### Email 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST= 'smtp.gmai.com'
#EMAIL_HOST = 'imap.mail.me.com'
EMAIL_PORT= '465' #STPM ssl
#EMAIL_PORT = '993' #IMAP 587 TLS
EMAIL_HOST_USER= '' 
#EMAIL_HOST_USER='flima21@me.com'
EMAIL_HOST_PASSWORD= '' 
#EMAIL_HOST_PASSWORD='Legiao2110'
EMAIL_USE_SSL= True
#EMAIL_USE_TLS=True
EMAIL_TIMEOUT= 120

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "/home/lima/apps/conselho/static"),
)


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")
MEDIAFILES_DIRS = (
    os.path.join(BASE_DIR, "media"),
)



''' 

TINYMCE_DEFAULT_CONFIG = {
'theme': "advanced", # default value
'relative_urls': True, # default value
'plugins': 'table,spellchecker,paste,searchreplace,bbcode,advimage, visualblocks, autosave, latex',
'theme_advanced_buttons1': 'bold,italic,underline,bullist,numlist,link,unlink,styleselect,fontselect,fontsizeselect, code, paste, code, , image, advimage,',
'theme_advanced_buttons1_add': 'cut, latex',
'width': '70%',
'height': 500,
'toolbar_items_size': 'Big',
'paste_text_sticky': True,
'paste_text_sticky_default': True,
'valid_styles': 'font-weight,font-style,text-decoration',
'file_browser_callback': 'mce_filebrowser',
'fontsize_formats': "8pt 10pt 11pt 12pt 13pt 14pt 16pt 18pt 20pt 24pt 36pt",
'font_formats': "Andale Mono=andale mono,times;" +
    "Arial=arial,helvetica,sans-serif;" +
    "Arial Black=arial black,avant garde;" +
    "Book Antiqua=book antiqua,palatino;" +
    "Comic Sans MS=comic sans ms,sans-serif;" +
    "Courier New=courier new,courier;" +
    "Georgia=georgia,palatino;" +
    "Helvetica=helvetica;" +
    "Impact=impact,chicago;" +
    "Symbol=symbol;" +
    "Tahoma=tahoma,arial,helvetica,sans-serif;" +
    "Terminal=terminal,monaco;" +
    "Times New Roman=times new roman,times;" +
    "Trebuchet MS=trebuchet ms,geneva;" +
    "Verdana=verdana,geneva;" +
    "Webdings=webdings;" +
    "Wingdings=wingdings,zapf dingbats",}


''' 


#MEDIA_URL='/media/'

#MEDIA_ROOT='/media/'
