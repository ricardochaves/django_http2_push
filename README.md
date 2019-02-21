# django_http2_push

[![Build Status](https://travis-ci.org/ricardochaves/django_http2_push.svg?branch=master)](https://travis-ci.org/ricardochaves/django_http2_push) [![Coverage Status](https://coveralls.io/repos/github/ricardochaves/django_http2_push/badge.svg?branch=master)](https://coveralls.io/github/ricardochaves/django_http2_push?branch=master) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/3fde2e17d87f4fc68cd9211e342d465d)](https://app.codacy.com/app/ricardochaves/django_http2_push?utm_source=github.com&utm_medium=referral&utm_content=ricardochaves/django_http2_push&utm_campaign=Badge_Grade_Dashboard) [![Maintainability](https://api.codeclimate.com/v1/badges/076c5d59aee18da4abc3/maintainability)](https://codeclimate.com/github/ricardochaves/django_http2_push/maintainability) 
 [![Updates](https://pyup.io/repos/github/ricardochaves/django_http2_push/shield.svg)](https://pyup.io/repos/github/ricardochaves/django_http2_push/) [![Python 3](https://pyup.io/repos/github/ricardochaves/django_http2_push/python-3-shield.svg)](https://pyup.io/repos/github/ricardochaves/django_http2_push/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) 
[![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/ricardochaves/django_http2_push/blob/master/LICENSE) [![PyPI version](https://badge.fury.io/py/django-http2-push.svg)](https://badge.fury.io/py/django-http2-push) [![Downloads](https://pepy.tech/badge/django-http2-push)](https://pepy.tech/project/django-http2-push) [![Downloads](https://pepy.tech/badge/django-http2-push/month)](https://pepy.tech/project/django-http2-push) [![Downloads](https://pepy.tech/badge/django-http2-push/week)](https://pepy.tech/project/django-http2-push) [![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/ricardochaves)



A simple way to add Header LINK

## Install

```bash
pip install django_http2_push
```

Update your `settings.py`

```python
INSTALLED_APPS = [
    ...
    "django_http2_push",
    ...
]

MIDDLEWARE = [
    ...
    "django_http2_push.middleware.PushHttp2Middleware",
    ...
]
```

## Usage

In the templates now use `static_push` instead of `staticfiles`.

![template_html](docs/images/template_html.png)

![header](docs/images/header_done.png)

