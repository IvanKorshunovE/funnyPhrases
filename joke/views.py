from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request):
        return Response("Hello There (2024 Mar 14:26)")
