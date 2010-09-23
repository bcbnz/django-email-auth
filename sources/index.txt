=================
django-email-auth
=================

When asked to log a user in, `Django`_ uses one or more authentication backend
classes to perform the authentication. The default backend requires a username
and password. This project provides an email authentication backend, thus
allowing users to log in with their email address and password.

This documentation describes how to obtain and install django-email-auth on
your own Django-based website. You may also want to see the `django-admin-loginpatches
project <http://blairbonnett.github.com/django-admin-loginpatches>`_ to provide
better integration of the email authentication backend into Django's
admininstration system.

.. _`Django`: http://www.djangoproject.com

Contents:
=========

.. toctree::
   :maxdepth: 2

   obtain
   install
   settings
   backends
   forms
   gpl3

License
=======

Copyright (C) 2010 Blair Bonnett

django-email-auth is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

django-email-auth is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

Version 3 of the GNU General Public License is available `here <gpl3.rst>`_,
or online (along with any later versions) at http://www.gnu.org/licenses/.
