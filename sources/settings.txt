Settings
========

.. setting:: EMAIL_AUTH_DEFAULT_DOMAINS

EMAIL_AUTH_DEFAULT_DOMAINS
--------------------------

Default: ``None``

A string, or tuple of strings, defining the domain(s) to try if the user enters
a username without a domain. If it is set to ``None``, then only the value the
user enters will be used in the authentication attempt.
