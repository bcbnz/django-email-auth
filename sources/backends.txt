Backends
========

The Django authentication module (:mod:`django.contrib.auth`) delegates the
handling of logins and permission checking to separate authentication backend
classes. This allows authentication methods besides the default username and
password method to be easily integrated into the system.

See the `User authentication in Django <http://docs.djangoproject.com/en/dev/topics/auth/>`_
document for more details on how Django authentication works.

EmailBackend
------------

.. class:: email_auth.backends.EmailBackend

   Allow authentication via email address and password. To use this, add it to
   the :setting:`AUTHENTICATION_BACKENDS` list in your settings file.

   This backend inherits from the default backend - :class:`django.contrib.auth.backends.ModelBackend` -
   and all the permission lookup methods (such as :func:`has_perm`) are left
   unchanged i.e., permissions are determined in the same way as the default
   backend.

   .. function:: authenticate(email=None, password=None)

      Attempt to authenticate a user from their email and password. If the
      authentication is successful, it returns the corresponding
      :class:`django.contrib.auth.models.User` instance. If it is unsuccessful, it
      returns ``None``.

      If the email address is specified without a domain (i.e., just a username
      such as ``bob``), then any default domains given in the :setting:`EMAIL_AUTH_DEFAULT_DOMAINS`
      setting will be added to the username when attempting to authenticate.

      If multiple user accounts are found for a given email address, they are
      tested in the order they are returned from the database until one is
      found for which the password matches. If neccessary, this order can be
      specified through the :setting:`EMAIL_AUTH_ORDERING` setting.

   .. function:: get_users_from_email(email, ordering=None)

      Get a list of users (instances of the :class:`django.contrib.auth.models.User`
      class) which have the given email address. If there is no user with the
      email address, an empty list is returned. If the ``ordering`` parameter
      is not ``None``, the list is sorted by the fields specified in the
      parameter.
