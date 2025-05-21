from shared.serializers import BaseSerializer

class RoleSerializer(BaseSerializer):
    def _init_(self, to_serialize, *, fields=[], request=None):
        super()._init_(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'code': instance.code,
            'name': instance.name,
        }


class ProfileSerializer(BaseSerializer):
    def __init__(self, to_serialize, *, fields=[], request=None):
        super().__init__(to_serialize, fields=fields, request=request)

    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'user': {
                'username': instance.user.username,
                'first_name': instance.user.first_name,
                'last_name': instance.user.last_name,
                'email': instance.user.email,
            },
            'id_number': instance.id_number,
            'phone': instance.phone,
            'profession': instance.profession,
            'experience': instance.experience,
            'avatar': self.build_url(instance.avatar.url),
            'role': [role.name for role in instance.role.all()],
        }