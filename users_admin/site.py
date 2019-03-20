from django.contrib.admin.sites import AdminSite
from .forms import UsersAdminAuthenticationForm


class UsersAdminBase(AdminSite):

    site_header = "Users' admin"
    site_title = "Users' admin"
    index_title = "Welcome"
    site_url = None

    login_form = UsersAdminAuthenticationForm

    def __init__(self, name=None):
        name = name or 'users_admin'
        super().__init__(name)

    def has_permission(self, request):
        """
        Removed check for is_staff.
        """
        return request.user.is_active
