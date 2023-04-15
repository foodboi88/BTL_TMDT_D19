from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

from django.shortcuts import render
import json
# Create your views here.
from django.http import JsonResponse
from django.core import serializers


from django.views.decorators.csrf import csrf_exempt


# from .models import Data


class MyView(APIView):
    def get(self, request):
        # start_date = request.GET.get('start_date')
        # end_date = request.GET.get('end_date')
        start_date = 1
        end_date = 2
        if start_date and end_date:
            # Xử lý dữ liệu
            data = {
                'start_date': start_date,
                'end_date': end_date
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing start_date or end_date parameter'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        if start_date and end_date:
            # Xử lý dữ liệu
            data = {
                'url_image': "thumbnail.png",
                'aray': 11111111111,
                "res": [1, 2]
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing start_date or end_date parameter'}, status=status.HTTP_400_BAD_REQUEST)
