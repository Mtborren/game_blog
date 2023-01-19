from django.http import JsonResponse
from .models import Game
from .serializers import GameSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.contrib.auth.models import User



class game_list(APIView):
    def get(self, request, format=None):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class game_detail(APIView):
    def get_object(self, id):
        try: 
            return Game.objects.get(pk=id)
        except Game.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        game = self.get_object(id)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        game = self.get_object(id)
        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        game = self.get_object(id)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# @api_view(['GET', 'POST'])
# def game_list(request, format=None):

#     if request.method == 'GET':
#         #get all the drinks
#         games = Game.objects.all()
#         #serialize them
#         serializer = GameSerializer(games, many=True)
#         #return json
#         return JsonResponse({"Games": serializer.data})

#     if request.method == 'POST':
#         serializer = GameSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def game_detail(request, id, format=None):
#     try:
#         game = Game.objects.get(pk=id)
#     except Game.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = GameSerializer(game)
#         return Response(serializer.data)
#     elif request.method == 'PUT':  
#         serializer = GameSerializer(game, data=request.data)
#         if serializer.is_valid():  
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         game.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)