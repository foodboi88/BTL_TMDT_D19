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

from .models import *


# from .models import Data


class MyView_Funtion1(APIView):
    def get(self, request):
        data = {
            'start_date': "2022-01-01",
            'end_date': "2023-01-04"
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        start_date = str(request.data.get('start_date'))
        end_date = str(request.data.get('end_date'))
        if start_date and end_date:
            filename, days, count = funtion1(start_date, end_date)
            # Xử lý dữ liệu
            data = {
                'url_image': filename,
                'days': days,
                "count": count
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing start_date or end_date parameter'}, status=status.HTTP_400_BAD_REQUEST)


class MyView_Funtion2(APIView):
    def get(self, request):
        data = {
            'year': 2022,
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        year = str(request.data.get('year'))
        if year:
            filename, my_dict = funtion2(year)
            # Xử lý dữ liệu
            data = {
                'url_image': filename,
                'my_dict': my_dict,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing start_date or end_date parameter'}, status=status.HTTP_400_BAD_REQUEST)


class MyView_Funtion3(APIView):
    def get(self, request):
        data = {
            'start_year': 2010,
            'end_year': 2023
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        start_year = str(request.data.get('start_year'))
        end_year = str(request.data.get('end_year'))
        if start_year and end_year:
            filename, my_dict = funtion3(start_year, end_year)
            # Xử lý dữ liệu
            data = {
                'url_image': filename,
                'my_dict': my_dict,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing start_date or end_date parameter'}, status=status.HTTP_400_BAD_REQUEST)


class MyView_Funtion4(APIView):
    def get(self, request):
        data = {
            'start_date': "2022-01-01",
            'end_date': "2022-01-04"
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        start_date = str(request.data.get('start_date'))
        end_date = str(request.data.get('end_date'))
        if start_date and end_date:
            filename, days, count = funtion4(start_date, end_date)
            # Xử lý dữ liệu
            data = {
                'url_image': filename,
                'days': days,
                "count": count
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing start_date or end_date parameter'}, status=status.HTTP_400_BAD_REQUEST)


class MyView_Funtion5(APIView):
    def get(self, request):
        data = {
            'year': 2022,
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        year = str(request.data.get('year'))
        if year:
            filename, my_dict = funtion5(year)
            # Xử lý dữ liệu
            data = {
                'url_image': filename,
                'my_dict': my_dict,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing start_date or end_date parameter'}, status=status.HTTP_400_BAD_REQUEST)


class MyView_Funtion6(APIView):
    def get(self, request):
        data = {
            'start_year': 2010,
            'end_year': 2023
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        start_year = str(request.data.get('start_year'))
        end_year = str(request.data.get('end_year'))
        if start_year and end_year:
            filename, my_dict = funtion6(start_year, end_year)
            # Xử lý dữ liệu
            data = {
                'url_image': filename,
                'my_dict': my_dict,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing start_date or end_date parameter'}, status=status.HTTP_400_BAD_REQUEST)


class MyView_Funtion7(APIView):
    def get(self, request):
        data = {
            'year': 2022,
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        year = str(request.data.get('year'))
        if year:
            filename, my_dict_0, my_dict_1 = funtion7(year)
            # Xử lý dữ liệu
            data = {
                'url_image': filename,
                'my_dict_0': my_dict_0,
                'my_dict_1': my_dict_1,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing start_date or end_date parameter'}, status=status.HTTP_400_BAD_REQUEST)


class MyView_Funtion8(APIView):
    def get(self, request):
        data = {
            'year': 2022,
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        year = str(request.data.get('year'))
        if year:
            filename, my_dict_0, my_dict_1 = funtion8(year)
            # Xử lý dữ liệu
            data = {
                'url_image': filename,
                'my_dict_0': my_dict_0,
                'my_dict_1': my_dict_1,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing start_date or end_date parameter'}, status=status.HTTP_400_BAD_REQUEST)


class MyView_Funtion9(APIView):
    def get(self, request):
        data = {
            'year': 2022,
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        year = str(request.data.get('year'))
        if year:
            filename, my_dict = funtion9(year)
            # Xử lý dữ liệu
            data = {
                'url_image': filename,
                'my_dict': my_dict,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing start_date or end_date parameter'}, status=status.HTTP_400_BAD_REQUEST)


class MyView_Funtion10(APIView):
    def get(self, request):
        data = {
            'year': 2022,
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        year = str(request.data.get('year'))
        if year:
            filename, my_dict = funtion10(year)
            # Xử lý dữ liệu
            data = {
                'url_image': filename,
                'my_dict': my_dict,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing start_date or end_date parameter'}, status=status.HTTP_400_BAD_REQUEST)


class MyView_Funtion11(APIView):
    def get(self, request):
        data = {
            'year': 2022,
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        year = str(request.data.get('year'))
        if year:
            filename, my_dict = funtion11(year)
            # Xử lý dữ liệu
            data = {
                'url_image': filename,
                'my_dict': my_dict,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing start_date or end_date parameter'}, status=status.HTTP_400_BAD_REQUEST)


class MyView_Funtion12(APIView):
    def get(self, request):
        data = {
            'year': 2022,
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        year = str(request.data.get('year'))
        if year:
            filename, my_dict = funtion12(year)
            # Xử lý dữ liệu
            data = {
                'url_image': filename,
                'my_dict': my_dict,
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing start_date or end_date parameter'}, status=status.HTTP_400_BAD_REQUEST)
