# monologue

![Christopher Walken](https://upload.wikimedia.org/wikipedia/commons/1/18/Christopher_Walken_-_1984.jpg)

[![PyPI version](https://badge.fury.io/py/django-monologue.svg)](https://pypi.python.org/pypi/django-monologue/)
[![PyPI format](https://img.shields.io/pypi/format/django-monologue.svg)](https://pypi.python.org/pypi/django-monologue/) [![Join the chat at https://gitter.im/aisk/monologue](https://badges.gitter.im/aisk/monologue.svg)](https://gitter.im/aisk/monologue?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


Simple blog system based on Django. Can be used as standalone project or as a django app to be used in your django project.

## Usage

### Embed

For used as a django app in your django project:

1, Install this package using `$ pip install django-monologue`, or using poetry / pipenv.

2, Add 'monogule' to you `settings.py`'s `INSTALLED_APPS` field, it should be like this:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    ...

    'monologue',  # <- Add this.
]
```

3, Run `$ python manage.py migrate monologue` to create database tables.

4, Mount `monologue`'s urls to your poject's `urls.py`. It should be looks like this:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    ...

    path('blog/', include('monologue.urls')), #  <- Add this.
]
```

The mount path in this example above is `blog/`, you can change it to whatever you like.

5, Run your server as normal, and check if monologue works fine. Admin site is registered too.

### Standalone

You can clone this repo and use it just like a normal django project.

And please notice that you should change the secret key in `settings.py` before use.

## License

MIT
