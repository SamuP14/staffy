import json
from json.decoder import JSONDecodeError
from io import BytesIO
import base64
from PIL import Image, UnidentifiedImageError

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from shared.decorators import get_required, post_required
from shared import utils
from .models import Profile, Role
from .serializers import ProfileSerializer, RoleSerializer


@csrf_exempt
@get_required
def profile_list(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, request=request)
    return serializer.json_response()

@csrf_exempt
@post_required
def add_profile(request):
    try:
        data = json.loads(request.body)
    except JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    required_fields = ['username', 'first_name', 'last_name', 'id_number', 'email', 'password', 'phone', 'profession']
    
    if not utils.validate_required_fields(data, required_fields):
        return JsonResponse({'error': 'Missing required fields'}, status=400)

    username = data['username']
    first_name = data['first_name']
    last_name = data['last_name']
    id_number = data['id_number']
    email = data['email']
    password = data['password']
    phone = data['phone']
    profession = data['profession']

    user = User.objects.create(
        username=username, 
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )
    user.set_password(password)
    user.save()

    profile = Profile.objects.create(
        user=user,
        id_number=id_number,
        phone=phone,
        profession=profession,
    )

    if 'avatar' in data:
        profile.avatar = data['avatar']
        
    if 'role' in data:
        profile.role.set(data['role'])

    return JsonResponse({'id': user.pk}, status=201)


@get_required
def profile_detail(request, username):
    try:
        profile = Profile.objects.select_related('user').get(user__username=username)
    except Profile.DoesNotExist:
        return JsonResponse({'error': 'Profile not found'}, status=404)

    serializer = ProfileSerializer(profile, request=request)
    return serializer.json_response()

@csrf_exempt
@post_required
def edit_profile(request, username):
    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
    except (User.DoesNotExist, Profile.DoesNotExist):
        return JsonResponse({'error': 'User or profile not found'}, status=404)

    try:
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    for field in ['first_name', 'last_name']:
        if field in data:
            setattr(user, field, data[field])
    user.save()

    for field in ['experience', 'profession', 'phone', 'id_number']:
        if field in data:
            setattr(profile, field, data[field])

    avatar_base64 = data.get('avatar')
    if avatar_base64:
        try:
            if avatar_base64.startswith('data:image'):
                avatar_base64 = avatar_base64.split(';base64,')[1]

            decoded_img = base64.b64decode(avatar_base64)
            image = Image.open(BytesIO(decoded_img))
            image.verify()

            profile.avatar.save(f"{username}_avatar.png", BytesIO(decoded_img), save=False)
        except (base64.binascii.Error, UnidentifiedImageError, ValueError):
            return JsonResponse({'error': 'Invalid image data'}, status=400)

    profile.save()
    return JsonResponse({'message': 'Profile updated successfully'})


@csrf_exempt
@post_required
def delete_profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    user.delete()

    return JsonResponse({'message': 'User and profile deleted successfully'}, status=200)

@csrf_exempt
@post_required
def profile_add_role(request, username):
    try:
        data = json.loads(request.body)
        role_codes = data.get('role_codes', [])
        if not isinstance(role_codes, list) or not role_codes:
            return JsonResponse({'error': 'role_codes must be a non-empty list'}, status=400)
    except JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    try:
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
    except (User.DoesNotExist, Profile.DoesNotExist):
        return JsonResponse({'error': 'User or Profile not found'}, status=404)

    added_roles = []
    for code in role_codes:
        try:
            role = Role.objects.get(code=code)
            profile.role.add(role)
            added_roles.append(code)
        except Role.DoesNotExist:
            continue

    return JsonResponse({'message': f'Roles added to {username}', 'added_roles': added_roles}, status=200)


@csrf_exempt
@post_required
def profile_delete_role(request, username, role_code):
    profile = get_object_or_404(Profile, user__username=username)

    role_exists = profile.role.filter(code=role_code).exists()

    if role_exists:
        profile.role.remove(profile.role.get(code=role_code))
        profile.save()
        return JsonResponse({'message': 'Role removed successfully.'}, status=200)
    
    return JsonResponse({'error': 'Role not found in profile.'}, status=400)


@csrf_exempt
@get_required
def role_list(request):
    roles = Role.objects.all()
    serializer = RoleSerializer(roles, request=request)
    return serializer.json_response()

@csrf_exempt
@post_required
def add_role(request):
    try:
        data = json.loads(request.body)
    except JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    required_fields = ['code', 'name']
    if not utils.validate_required_fields(data, required_fields):
        return JsonResponse({'error': 'Missing required fields'}, status=400)

    role = Role.objects.create(
        code=data['code'],
        name=data['name'],
    )

    return JsonResponse({'id': role.pk}, status=201)

@csrf_exempt
@post_required
def delete_role(request, role_code):
    try:
        role = Role.objects.get(code=role_code)
    except (Role.DoesNotExist):
        return JsonResponse({'error': 'Role not found'}, status=404)

    role.delete()
    return JsonResponse({'message': 'Role deleted'})

@csrf_exempt
@post_required
def login_view(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return JsonResponse({'success': False, 'error': 'Missing credentials'}, status=400)

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

        try:
            avatar_url = request.build_absolute_uri(user.profile.avatar.url)
            print(avatar_url)
        except Exception as e:
            print('No avatar found:', e)
            avatar_url = request.build_absolute_uri('/media/avatars/noavatar.png')

        return JsonResponse({
            'success': True,
            'username': user.username,
            'user_id': user.pk,
            'avatar': avatar_url
        })
    else:
        return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=401)

@csrf_exempt
@post_required
def logout_view(request):
    logout(request)
    return JsonResponse({'success': True})