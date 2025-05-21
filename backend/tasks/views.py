from django.shortcuts import render
import json
from json.decoder import JSONDecodeError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from accounts.models import Profile
from .models import Task
from .serializers import TaskSerializer
from shared.decorators import get_required, post_required
from shared import utils

@csrf_exempt
@get_required
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, request=request)
    return serializer.json_response()

@get_required
def task_detail(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

    serializer = TaskSerializer(task)
    return serializer.json_response()

@csrf_exempt
@post_required
def add_task(request):
    try:
        data = json.loads(request.body)
    except JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    required_fields = ['title', 'description', 'due_date', 'status', 'priority', 'employees']
    if not utils.validate_required_fields(data, required_fields):
        return JsonResponse({'error': 'Missing required fields'}, status=400)

    task = Task.objects.create(
        title=data['title'],
        description=data['description'],
        due_date=data['due_date'],
        status=data['status'],
        priority=data['priority'],
    )
    profiles = Profile.objects.filter(user__username__in=data['employees'])
    task.employees.set(profiles)
    task.save()

    return JsonResponse({'id': task.pk}, status=201)

@csrf_exempt
@post_required
def edit_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

    try:
        data = json.loads(request.body)
    except JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    for field in ['title', 'description', 'due_date', 'status', 'priority']:
        if field in data:
            setattr(task, field, data[field])

    if 'employees' in data:
        profiles = Profile.objects.filter(user__username__in=data['employees'])
        task.employees.set(profiles)

    task.save()
    return JsonResponse({'message': 'Task updated successfully'})

@csrf_exempt
@post_required
def delete_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

    task.delete()
    return JsonResponse({'message': 'Task deleted'})
