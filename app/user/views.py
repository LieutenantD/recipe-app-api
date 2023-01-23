"""
Views for the User API.
"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer,AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):     # Creates the API with CreateAPIView
    """Create a new user in the system."""        # Needs a create method in its serializer.
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):           # Creates the API token with ObtainAuthToken.
    """Create a new auth token for user."""       # Don't need a view method for creating the token.
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):               # Updates the API with RetrieveUpdateAPIView.
    """Manage the authenticated user."""                            # Also needs a view method called "update" in its serializer.
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication] # In this line it authenticates with TokenAuthentication.
    permission_classes = [permissions.IsAuthenticated]      # This is defining the permissions of the user.

    def get_object(self):
        """Retrieve and return the authenticated user."""      # Should return the authenticated user.
        return self.request.user
