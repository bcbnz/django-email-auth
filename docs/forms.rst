Forms
=====

AuthenticationForm
------------------

.. class:: email_auth.forms.AuthenticationForm

   A form to show an authentication form for users attempting to login via
   email address and password. This is designed as a direct replacement for
   the ``django.contrib.auth.forms.AuthenticationForm`` form.

   In Django 1.2 or later, you can specify the form to be used with the login
   view when configuring your URLconf. To use this form for logins, pass it as
   the value for the ``authentication_form`` argument to the
   ``django.contrib.auth.views.login`` view::

       from mysite.email_auth.forms import AuthenticationForm

       urlpatterns = patterns('',
           ....
           (r'^accounts/login', 'django.contrib.auth.views.login',
            {'authentication_form': AuthenticationForm}),
           ....
       )

   See the `Django authentication documentation <http://docs.djangoproject.com/en/dev/topics/auth/>`_
   for details of the ``login`` view, or the `URL dispatcher
   <http://docs.djangoproject.com/en/dev/topics/http/urls/>`_ documentation for
   details on how to write URLconfs.

   If you are designing templates specifically for this form, note that the
   email address is entered in a field called ``username``. This is in order to
   allow templates designed for the default login form to work seamlessly with
   this form.

   .. function:: clean()

      Process the form and attempt to log the user in with the details they
      provided. If the login was successful, the form data is returned. If the
      login is unsuccessful, a ``django.forms.ValidationError`` is raised with
      a message explaining why it did not succeed.

   .. function:: get_user_id()

      Get the user ID of the user logged in by the form. If no user was logged
      in, this function returns None.

   .. function:: get_user()

      Get the user object (an instance of ``django.contrib.auth.models.User``)
      corresponding to the user logged in by the form. If no user was logged
      in, this function returns None.
