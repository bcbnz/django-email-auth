Settings
========

.. setting:: EMAIL_AUTH_DEFAULT_DOMAINS

EMAIL_AUTH_DEFAULT_DOMAINS
--------------------------

Default: ``None``

A string, or tuple of strings, defining the domain(s) to try if the user enters
a username without a domain. If it is set to ``None``, then only the value the
user enters will be used in the authentication attempt.

.. setting:: EMAIL_AUTH_ORDERING

EMAIL_AUTH_ORDERING
-------------------

Default: ``None``

A tuple of strings defining the order in which to sort user accounts when more
than one exists for a given email address. If ``None``, no sorting is
performed. For details on how to specify ordering in Django, see the `QuerySet
API documentation <http://docs.djangoproject.com/en/dev/ref/models/querysets/#order-by-fields>`_.
