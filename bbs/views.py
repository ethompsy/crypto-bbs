from django.core.cache import cache
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.shortcuts import render

from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes

from bbs.models import Board, Post
from bbs.serializers import BoardSerializer, PostSerializer

import datetime
from django.utils import timezone
from django.utils.timezone import utc

def board(request):
    """Load the template"""
    return render(request, 'bbs/board.html')

class BoardDetailView(DetailView):
    """Board Detail View"""
    model = Board
    template_name = "bbs/board.html"
    def get_object(self, *args, **kwargs):
        pk = self.kwargs['pk']
        obj = get_board_or_make_one(pk)
        return obj

# ENDPOINT VIEWS

@api_view(['GET', 'POST',])
@renderer_classes([JSONRenderer])
def boardAPI(request, *args, **kwargs):
    """
    API endpoint for Board objects
    """
    # Currently GET requests are restricted by api_auth.
    if request.method == 'GET':
        key = kwargs.get('key')
        qs = Board.objects.all()
        if key: 
            try:
                board = qs.get(key=key)
            except Exception:
                # Make an object
                board = Board()
                board.key = key
            serializer = BoardSerializer(board, many=False)
            return Response(serializer.data)
        else:
            # If a list then we don't want to share.
            return Response("Please be more specific.")
    elif request.method == 'POST':
        return create_board(request, *args, **kwargs)
    else:
        msg = "HTTP METHOD NOT ALLOWED: " + request.method
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST',])
@renderer_classes([JSONRenderer])
def postAPI(request, *args, **kwargs):
    """
    API endpoint for saving Post objects
    """
    if request.method == 'POST':
        return create_post(request, *args, **kwargs)
    elif request.method == 'GET':
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    else:
        msg = "HTTP METHOD NOT ALLOWED: " + request.method
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)

# CREATE/UPDATE FUNCTIONS

def create_board(request, *args, **kwargs):
    # Make an object
    b = Board()
    # Set the date to now
    b.date = timezone.now()
    # Get key
    key = request.DATA.get('key', '0')
    # Check for a session_id
    if not key:
        msg = "The key is required."
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    # Assign key value
    b.key = request.DATA.get('key', '0')
    # Add object to the cache
    board_key = "board_" + str(b.key)
    cache.set(board_key, b)
    # Save the object
    b.save()
    # Return an HTTP Response
    msg = "Created board with key: " + b.key
    return HttpResponse(msg)

def create_post(request, *args, **kwargs):
    key = request.DATA.get('key', '0')
    if not key:
        msg = "The key is required."
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)
    # Get the Board referenced by key
    b = get_board_or_make_one(key)
    if not b:
        msg = "Something has gone wrong!"
        return HttpResponse(msg)
    # Make an object
    p = Post()
    # Assign to the board
    # setattr(p, 'board', b)
    p.board = b
    # Set the date to now
    p.date = timezone.now()
    # Set the post content
    p.text = request.DATA.get('text', '')
    # Save the object
    p.save()
    # Return an HTTP Response
    msg = "Created a post."
    return HttpResponse(msg)

def get_board_or_make_one(key):
    b = cache.get('board_' + str(key))
    if not b:
        try:
            b = Board.objects.get(key=key)
            cache.set('board_' + str(key), b)
        except Exception:
            b = Board()
            b.key = key
            b.date = timezone.now()
            b.save()
            cache.set('board_' + str(key), b)
    return b