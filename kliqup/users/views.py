from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from kliqup.users.serializers import UserSerializer
from .models import User


class UserViewSet(ModelViewSet):
    """
    The User view set.

    list:
    List all Devices.

    create:
    Create a Device instance.

    destroy:
    Delete a Device instance.

    retrieve:
    Retrieve a Device instance.

    update:
    Update a Device instance.

    partial_update:
    Partially update a Device instance.
    """
    model = get_user_model()
    permission_classes = (DjangoModelPermissions,)
    serializer_class = UserSerializer
    queryset = User.objects.prefetch_related('connections').all()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
