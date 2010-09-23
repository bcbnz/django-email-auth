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
For example, with the setting::

    EMAIL_AUTH_DEFAULT_DOMAINS = (
        'example.com',
        'mysite.org',
    )

if the user enters the username ``bob``, the backend will try to authenticate
them as ``bob@example.com`` and then, if that fails, as ``bob@mysite.org``.
