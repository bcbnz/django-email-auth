Backends
========

The Django authentication system (``django.contrib.auth``) delegates the
handling of logins and permission checking to separate authentication backend
classes. This allows authentication methods besides the default username and
password method to be easily integrated into the system.

See the `User authentication in Django <http://docs.djangoproject.com/en/dev/topics/auth/>`_
document for more details on how Django authentication works.

EmailBackend
------------

.. class:: email_auth.backends.EmailBackend

   Allow authentication via email address and password. To use this, add it to
   the ``AUTHENTICATION_BACKENDS`` list in your settings file.

   This backend inherits from the default backend - ``django.contrib.auth.backends.ModelBackend`` -
   and all the permission lookup methods (such as has_perm()) are left
   unchanged.

   .. function:: authenticate(email=None, password=None)

      Attempt to authenticate a user from their email and password. If the
      authentication is successful, it returns the corresponding
      ``django.contrib.auth.models.User`` instance. If it is unsuccessful, it
      returns ``None``.

      If the email address is specified without a domain (i.e., just a username
      such as ``bob``), then any default domains given in the :ref:`default_domains`
      setting will be added to the username when attempting to authenticate.

   .. function:: get_user(email)

      Get an user (an instance of the ``django.contrib.auth.models.User`` class)
      from the corresponding email address. If no such user exists, it returns
      ``None``.
