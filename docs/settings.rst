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

Default: ``()`` (Empty tuple)

A tuple of strings defining the order in which to sort user accounts when more
than one exists for a given email address. An empty tuple means that the
ordering is undefined (and hence unpredictable). For example, to sort the user
by first name and then the date of their last login::

    EMAIL_AUTH_ORDERING = (
        'first_name',
        'last_login',
    )
