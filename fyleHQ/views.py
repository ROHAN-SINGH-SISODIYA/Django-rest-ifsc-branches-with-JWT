from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from rest_auth.views import LoginView


sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters('password1', 'password2')
)

class CustomLoginView(LoginView):

    def get_response(self):
        orginal_response = super().get_response()

        custom_response = {"user": {
            "username": self.user.username,
            "email": self.user.email
        }}

        orginal_response.data.update(custom_response)
        return orginal_response
