from django.contrib.auth.models import User


class EmailBackend:
    """
    This is a custom authentication backend to authenticate users using email instead of username.
    for every costume authentication class we have to implement the two methods authenticate and get_user.
    and also we have to add it to the django authentication backends in the settings.py file.
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        this is essential for Session Management:
        After a user logs in, Django stores the user's ID in the session.
        When subsequent requests are made, Django uses this ID to retrieve the user object from the database.
        The get_user method is called to perform this retrieval.
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
