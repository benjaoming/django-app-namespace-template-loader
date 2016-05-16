===================
django-apptemplates
===================

|travis-develop| |coverage-develop| |PyPi|

Name change notification
------------------------

This project used to be called ``django-app-namespace-template-loader`` but a
decision has been made to merge with ``django-apptemplates``. The merge does not
actually include any code from ``django-apptemplates`` but rather bumps that
application to 2.0, keeping the code from this project.

The reason is to avoid having to projects addressing exactly the same issue.

Please update your PyPi requirements to use ``django-apptemplates``.

More background of the decision in
`this issue <https://github.com/Fantomas42/django-apptemplates/issues/14>`_.


Introduction
------------

Provides a template loader that allows you to load a template from a
specific application. This allows you to both **extend** and **override** a
template at the same time.

The default Django loaders require you to copy the entire template you want
to override, even if you only want to override one small block.

This is the issue that this package tries to resolve.

Examples:
---------

You want to change the titles of the admin site (located in
``my-project/templates/admin/base_site.html``), you would originally create
this template:

.. code-block:: html+django

    {% extends "admin/base.html" %}
    {% load i18n %}

    {% block title %}{{ title }} | My Project{% endblock %}

    {% block branding %}
    <h1 id="site-name">My Project</h1>
    {% endblock %}

    {% block nav-global %}{% endblock %}

But instead, you can extend ``my-project/templates/admin/base_site.html`` and
override Django's version with a namespace:

.. code-block:: html+django

    {% extends "admin:admin/base_site.html" %}

    {% block title %}{{ title }} - My Project{% endblock %}

    {% block branding %}
    <h1 id="site-name">My Project</h1>
    {% endblock %}

Note that in this version the block ``nav-global`` does not have to be
present because of the inheritance.

Shorter version of ``my-project/templates/admin/base_site.html`` without
namespace:

.. code-block:: html+django

    {% extends ":admin/base_site.html" %}

    {% block title %}{{ title }} - My Project{% endblock %}

    {% block branding %}
    <h1 id="site-name">My Project</h1>
    {% endblock %}

If we do not specify the application namespace, the first matching template
will be used. This is useful when several applications provide the same
templates but with different features.

Example of multiple empty namespaces:

``my-project/application/templates/application/template.html``

.. code-block:: html+django

    {% block content%}
    <p>Application</p>
    {% endblock content%}

``my-project/application_extension/templates/application/template.html``

.. code-block:: html+django

    {% extends ":application/template.html" %}
    {% block content%}
    {{ block.super }}
    <p>Application extension</p>
    {% endblock content%}

``my-project/templates/application/template.html``

.. code-block:: html+django

    {% extends ":application/template.html" %}
    {% block content%}
    {{ block.super }}
    <p>Application project</p>
    {% endblock content%}

Will render:

.. code-block:: html+django

    <p>Application</p>
    <p>Application extension</p>
    <p>Application project</p>

Installation
------------

First of all install ``django-apptemplates`` with your
favorite package manager. Example::

    $ pip install django-apptemplates

Once installed, add ``apptemplates.Loader`` to the ``TEMPLATE_LOADERS``
setting of your project.

.. code-block:: python

    TEMPLATE_LOADERS = [
      'apptemplates.Loader',
      ... # Other template loaders
    ]

With Django >= 1.8 ``apptemplates.Loader`` should be added to the
``'loaders'`` section in the OPTIONS dict of the ``DjangoTemplates`` backend
instead.

.. code-block:: python

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'OPTIONS': {
                'loaders': [
                    'apptemplates.Loader',
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ],
            },
        },
    ]

Known limitations
=================

``apptemplates.Loader`` can not work properly if you use it in conjunction
with ``django.template.loaders.cached.Loader`` and inheritance based on
empty namespaces.


Authors and Maintainers
-----------------------

Before version 2.0, django-apptemplates was created and maintained by:

 - Peter Bittner (current maintainer)
 - Tomas Zulberti (former maintainer)
 - Konrad Wojas (original author)

Since 2.0+, the project's codebase was replaced by the compatible project django-app-namespace-template-loader by author of django-blog-zinnia:

 - Fantomas42 (author and maintainer)

Notes
-----

Based originally on: http://djangosnippets.org/snippets/1376/

Requires: Django >= 1.8

Tested with Python 2.7, 3.3, 3.4, 3.5.

If you want to use this application for previous versions of Django, use the
version 0.3.1 of the package.

If you want to use this application with Python 2.6, use the version 0.2 of
the package.

.. |travis-develop| image:: https://travis-ci.org/Fantomas42/django-apptemplates.png?branch=develop
   :alt: Build Status - develop branch
   :target: http://travis-ci.org/Fantomas42/django-apptemplates
.. |coverage-develop| image:: https://coveralls.io/repos/Fantomas42/django-apptemplates/badge.png?branch=develop
   :alt: Coverage of the code
   :target: https://coveralls.io/r/Fantomas42/django-apptemplates
.. |PyPi| image:: https://badge.fury.io/py/django-apptemplates.svg
   :target: https://pypi.python.org/pypi/django-apptemplates/
   :alt: PyPi download page

