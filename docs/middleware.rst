Middleware
==========

In Django, middleware is called for each request and response. It can be used
to modify the input and/or output independently of the views. We use it to
modify some of the built-in behaviour of the Django administration interface
(``django.contrib.admin``) to better integrate it with the custom backend.

See the `Django middleware documentation <http://docs.djangoproject.com/en/dev/topics/http/middleware/>`_
for more information on middleware.

EmailAuthMiddleware
-------------------

.. class:: email_auth.middleware.EmailAuthMiddleware

   Many of the views in the Django administration interface use the
   ``@staff_member_required`` decorator to ensure that the user has staff
   permissions. However, the built-in decorator provides its own login form
   rather than using the ``LOGIN_URL`` specified in the settings. This has
   hard-coded field names (so the user is prompted for a username rather than a
   password). It also gives misleading error messages; for example, if the user
   enters their password wrong they are told that their username cannot contain
   the '@' character. Finally, if they successfully log in but don't have staff
   status, they are prompted to log in again rather than being told what the
   problem is.

   This piece of middleware overcomes this by replacing the decorator with a
   custom version. It redirects the user to the settings ``LOGIN_URL`` when
   needed, allowing any customisations made to the login view (such as custom
   authentication forms) to be used. If the user is logged in but does not have
   staff status, it uses the ``admin/not_staff.html`` template to tell them
   this. As a sanity check, it checks that they have an active account (this
   should have been done by the login view) and, if not, tells them so using
   the ``admin/inactive.html`` template.

   For this to work correctly, you must:

   * Configure ``LOGIN_URL`` in your settings to point to your login view.

   * Ensure your login view correctly handles the ``next`` parameter to
     redirect the user to the appropriate page after login.

   * Make the ``admin/inactive.html`` and ``admin/not_staff.html`` templates
     available to the Django template loader. Templates are provided in the
     ``email_auth/templates`` directory of the project, or you can create your
     own using these as a guide.

   It is recommended that you place this as the first piece of middleware to be
   used. If another piece of middleware above this directly generates a
   response, it may use the default decorator.

   .. function:: process_request(request)

      Django calls this function for every request made. It replaces the
      ``django.contrib.admin.views.decorators.staff_member_required`` decorator
      with the custom version.
