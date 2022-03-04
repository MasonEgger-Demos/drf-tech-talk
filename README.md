1. Environment setup
    1. Install virtual env
    1. Pip install django djangorestframework black pylint pylint-django
    1. Setup app directory in VSCode
    1. Setup Terminal, browser, VSCode to proper config
1. Getting to an API
    1. `django-admin startproject techtalk .`
    1. `python manage.py runserver`
        1. Show page
    1. `python manage.py startapp library`
    1. Open `techtalk/settings.py` and add:
        ```python
        INSTALLED_APPS = [
            ...
            "rest_framework",
            "library.apps.LibraryConfig",
        ]
        ```
    1. Open `library/models.py` and add:
        ```python
        class Book(models.Model):
            title = models.CharField(max_length=255)
            author = models.CharField(max_length=128)
            isbn13 = models.CharField(max_length=13, blank=True, null=True)

        ```
    1. Create `library/serializers.py` and add:
        ```python
        from rest_framework import serializers
        from .models import Book


        class BookSerializer(serializers.ModelSerializer):
            class Meta:
                model = Book
                fields = [
                    "title",
                    "author",
                    "isbn13",
                ]
                extra_kwargs = {
                    "isbn13": {"required": False},
                }
        ```    
    1. Open `library/views.py` and add:
        ```python
        from rest_framework import generics
        from .models import Book
        from .serializers import BookSerializer


        class BookList(generics.ListCreateAPIView):
            queryset = Book.objects.all()
            serializer_class = BookSerializer


        class BookDetail(generics.RetrieveUpdateDestroyAPIView):
            queryset = Book.objects.all()
            serializer_class = BookSerializer
        ```

    1. Create `books/urls.py` and add:
        ```python
        from django.urls import path

        from . import views

        urlpatterns = [
            path("books/", views.BookList.as_view()),
            path("books/<int:pk>/", views.BookDetail.as_view()),
        ]
        ```
    1. Edit `techtalk/urls.py` and add:
        ```python
        from django.contrib import admin
        from django.urls import include, path

        urlpatterns = [
            path("", include("library.urls"), name="library"),
            path('admin/', admin.site.urls),
        ]
        ```
    1. View `localhost:8000/` to view the builtin DRF Documentation
    1. `http POST localhost:8000/books/ title="Hunger Games" author="Suzanne Collins"`
    1. `http localhost:8000/books/`
    1. `http POST localhost:8000/books/ title="Catching Fire" author="Suzanne Collins"`
    1. `http DELETE localhost:8000/books/ title="Hunger Games" author="Suzanne Collins"`
    
1. Adding Auth
    1. Open `library/views.py` and add:
    ```python
    from rest_framework import permissions

    # to both functions
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ```
    1. Authenticating
        1. `http -a megger:Sammy123! POST localhost:8000/books/ title="Mockingjay" author="Suzanne Collins"`
    1. Token Based Auth
        1. Open `techtalk/settings.py` and add:
        ```python
        INSTALLED_APPS = [
            ...
            "rest_framework.authtoken",
        ]
        ```
        and
        ```python
        REST_FRAMEWORK = {
            "DEFAULT_AUTHENTICATION_CLASSES": [
                "rest_framework.authentication.TokenAuthentication",
                "rest_framework.authentication.BasicAuthentication",
                "rest_framework.authentication.SessionAuthentication",
            ],
        }
        ```
        1. Stop server and run `django migrate`
        1. Create token in Admin UI
        1. `export MY_TOKEN=`
        1. `http POST localhost:8000/books/ title="Ballad of Songbirds and Snakes" author="Suzanne Collins" 'Authorization: Token '$MY_TOKEN`
1. Auto Documentation with `drf_spectacular`
    1. `pip install drf_spectacular`
    1. Open `techtalk/settings.py` and add:
        ```python
            INSTALLED_APPS = [
                ...
                "drf_spectacular",
            ]
        ```
        and
        ```python
            REST_FRAMEWORK = {
                "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
            }
        ```
    1. Open `techtalk/urls.py` and add:
    ```python

    from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

    urlpatterns = [
        ...
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "docs/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="docs",
        ),
    ]
    ```
    