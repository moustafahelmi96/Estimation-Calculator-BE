import json
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from EstimationCalculatorBE.forms import UserForm
from EstimationCalculatorBE.models import User
from rest_framework.decorators import api_view
from django.http import JsonResponse
import logging

from EstimationCalculatorBE.serializers import UserSerializer

# Get an instance of a logger
logger = logging.getLogger(__name__)


@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data=request.data)

    logging.error(serializer.is_valid())
    if serializer.is_valid():
        logging.error('INSIDE HERE!')
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
