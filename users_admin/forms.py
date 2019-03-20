from django.contrib.auth.forms import AuthenticationForm


class UsersAdminAuthenticationForm(AuthenticationForm):
    """
    Same as Django's AdminAuthenticationForm but allows login for a non staff.
    """

    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
