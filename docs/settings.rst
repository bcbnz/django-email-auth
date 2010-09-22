Settings
========



EMAIL_AUTH_DEFAULT_DOMAINS
--------------------------

Default: ``None``

A string, or list of strings, defining the domain(s) to try if the user enters
a username without a domain. For example, if it is set to::

    EMAIL_AUTH_DEFAULT_DOMAINS = (
        'example.com',
        'mysite.org',
    )

and the user enters ``bob``, then the backend will try to authenticate the user
as ``bob@example.com`` and then, if that fails, as ``bob@mysite.org``.

If it is set to ``None``, or is not a string/list of strings, then only the
value the user enters will be used in the authentication attempt.
