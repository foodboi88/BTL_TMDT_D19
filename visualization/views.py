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


def get_data(request):
    data = {
        'name': 'John',
        'age': 30,
        'is_student': True
    }
    return JsonResponse(data, status=200)


@csrf_exempt
def get_data2(request):
    if request.method == 'POST':
        # Xử lý dữ liệu POST ở đây
        data = {'message': 'Dữ liệu đã được xử lý thành công!'}
        return JsonResponse(data, status=200)
    else:
        # Xử lý trường hợp không phải POST (ví dụ: GET)
        data = {'message': 'Phương thức không được hỗ trợ'}
        return JsonResponse(data, status=405)


class MyView(APIView):
    def get(self, request):
        data = {
            'name': 'John',
            'age': 30,
            'is_student': True
        }
        return Response(data, status=status.HTTP_200_OK)


class MyView2(APIView):
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
                'start_date': 1111111111,
                'end_date': 11111111111
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Missing start_date or end_date parameter'}, status=status.HTTP_400_BAD_REQUEST)


'''
def get_data1():  # request
    # start_date = request.GET.get('start_date')
    # end_date = request.GET.get('end_date')
    # data = Data.objects.filter(date__range=[start_date, end_date])
    results = []
    data = "imageeeeeeeeeee"
    for i in range(10):
        results.append({
            data
        })
    # json_data = json.dumps(results)
    json_data = serializers.serialize('json', data)
    return JsonResponse(json_data, safe=False)
'''
