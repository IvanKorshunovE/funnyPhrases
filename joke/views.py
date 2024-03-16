from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from joke.models import TestModel


class TestView(APIView):
    def get(self, request):
        users = TestModel.objects.values("text")
        user_dict = {user["text"]: user for user in users}
        return Response(f"Hello There (2024 Mar 14:26), {user_dict}")
