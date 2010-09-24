Installation
============

Basic installation
------------------

1. Copy the ``email_auth`` folder to your project.
2. Add :class:`email_auth.backends.EmailBackend` to the
   :setting:`AUTHENTICATION_BACKENDS` list in your settings. Note that Django
   tries the backends in the order specified in the settings. So if you want to
   try the email backend and fall back to the default (username) backend, you
   would specify the backends as::

       AUTHENTICATION_BACKENDS = (
           'email.auth.backends.EmailBackend',
           'django.contrib.auth.backends.ModelBackend',
       )

   Note that there is no requirement to have the :class:`ModelBackend` backend
   i.e., you can have the email backend as the only login method. For more
   details on how to specify the backends, see the `User authentication in
   Django <http://docs.djangoproject.com/en/dev/topics/auth/#specifying-authentication-backends>`_
   document.

Default domains
---------------

Emails are given in the form ``<username>@<domain>``. If many of your users
will be logging in with email address with a common domain, you can specify a
set of default domains through the :setting:`EMAIL_AUTH_DEFAULT_DOMAINS`
setting. If the user enters a username without a domain, the backend will then
try the default domains (in order) to see if one successfully authenticates.

For example, suppose the default domains are::

    EMAIL_AUTH_DEFAULT_DOMAINS = (
        'example.com',
        'mysite.org',
    )

If the user enters the username ``bob``, the backend will try to authenticate
them as ``bob@example.com`` and then, if that fails, as ``bob@mysite.org``.

Multiple accounts
-----------------

If multiple accounts exist for the email address being checked, the backend
will try them in the order they are retrieved from the database. Once an
account is found for which the password matches, the backend will assume that
is the correct user and not check any further accounts.

As the :class:`django.contrib.auth.models.User` model does not specify a
default order, the order they will be returned in is undefined and hence
unpredictable. If you require them to be tested in a particular order, you
can set the fields to order them by in the :setting:`EMAIL_AUTH_ORDERING`
setting. For example, to sort the user by first name and then the date of their
last login::

    EMAIL_AUTH_ORDERING = (
        'first_name',
        'last_login',
    )

For more details on specifying ordering in Django, see the `QuerySet API
documentation <http://docs.djangoproject.com/en/dev/ref/models/querysets/#order-by-fields>`_.
