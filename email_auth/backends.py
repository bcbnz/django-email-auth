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

    * EMAIL_AUTH_DEFAULT_DOMAINS - default domain name(s) to try if the user
      does not provide one. Must be either a string, or a tuple of strings. For
      example, if it is set to ('example.com', 'mysite.org'), and the user
      enters 'bob', the following steps will be performed:

      1. Is there a user with the email address 'bob@example.com' in the
         database? If so, is the password correct for this user? If so, this is
         the user we want.
      2. Does 'bob@mysite.org' appear in the database? If so, is the password
         correct for this user? If so, this is the user we want.

    If multiple user accounts exist for an email address, they will be tested
    in the order they are returned from the database until one is found for
    which the password matches.

    """

    def authenticate(self, username=None, password=None):
        # Need a username
        if username is None:
            return None

        # Domain given
        if '@' in username:
            # Find the user
            users = self.get_users_from_email(username)
            for user in users:
                # See if they match
                if user.check_password(password):
                    return user

            # Nobody found
            return None

        # No default domains
        domains = getattr(settings, 'EMAIL_AUTH_DEFAULT_DOMAINS', None)
        if domains is None:
            return None

        # Force it into a tuple to simplify logic
        if not isinstance(domains, tuple):
            domains = (domains,)

        # Try each domain until we find a match
        for domain in domains:
            email = '%s@%s' % (username, domain)
            users = self.get_users_from_email(email)
            for user in users:
                if user.check_password(password):
                    return user

        # Nobody found
        return None

    def get_users_from_email(self, email):
        # Search for a user
        try:
            return User.objects.filter(email=email)
        except User.DoesNotExist:
            return []
