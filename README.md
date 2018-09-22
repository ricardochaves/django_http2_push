# django_http2_push

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3fde2e17d87f4fc68cd9211e342d465d)](https://app.codacy.com/app/ricardochaves/django_http2_push?utm_source=github.com&utm_medium=referral&utm_content=ricardochaves/django_http2_push&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/ricardochaves/django_http2_push.svg?branch=master)](https://travis-ci.org/ricardochaves/django_http2_push) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black) [![Maintainability](https://api.codeclimate.com/v1/badges/076c5d59aee18da4abc3/maintainability)](https://codeclimate.com/github/ricardochaves/django_http2_push/maintainability)

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

