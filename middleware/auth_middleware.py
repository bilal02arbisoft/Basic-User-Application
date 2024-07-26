from django.shortcuts import redirect
from django.urls import reverse


class UserAuthMiddleware:

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        open_paths = [
           '/login/',
           '/signup/'
        ]

        if request.path not in open_paths:

            if not request.user.is_authenticated:

                return redirect(reverse('login'))

        response = self.get_response(request)

        return response
