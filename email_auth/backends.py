# This file is part of django-email-auth, a fully integrated email
# authentication backend for Django.
# Copyright (C) 2010 Blair Bonnett
#
# django-email-auth is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# django-email-auth is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with django-email-auth.  If not, see <http://www.gnu.org/licenses/>.

from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailBackend(ModelBackend):
    """Allow user authentication via email address.

    The following settings are used by the backend:

    * EMAIL_AUTH_DEFAULT_DOMAIN - if a username is entered without a domain,
      this domain will be appended to create the email used to authenticate
      the user. For example, if EMAIL_AUTH_DEFAULT_DOMAIN is 'example.com',
      and the user enters 'bob', the backend will attempt to authenticate
      'bob@example.com'.

    """

    def authenticate(self, username=None, password=None):
        # Need a username
        if username is None:
            return None

        # No domain given
        if '@' not in username:
            # Try using the domain given in the settings
            domain = settings.EMAIL_AUTH_DEFAULT_DOMAIN
            if domain is None:
                return None
            else:
                username = '%s@%s' % (username, domain)

        # Search for a user
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None

        # Check their credentials
        if user.check_password(password):
            return user
        else:
            return None
