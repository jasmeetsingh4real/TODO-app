from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from django.utils import translation
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import taskSerializer
# Create your views here.
from .models import Task

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List':'/task-list/',
        'Detail View': 'task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk/',
        'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = taskSerializer(tasks,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request,pk):
    task = Task.objects.get(id=pk)
    serializer = taskSerializer(task,many=False)
    return Response(serializer.data)



@api_view(['POST'])
def taskCreate(request):
    serializer = taskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request,pk):
    task=Task.objects.get(id=pk)
    serializer = taskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return response('updated!')


@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('done!')




# pk = primary key