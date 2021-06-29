from rest_framework.views import APIView
from ..push import pusher_client
from rest_framework.response import Response


class MessageAPIView(APIView):

    def get(self,request):
        pusher_client.trigger('chat', 'message', {
            'username': 'jermaine',
            'message': 'WOW'

        })
        return Response([])
