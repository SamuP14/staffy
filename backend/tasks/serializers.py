from shared.serializers import BaseSerializer
from accounts.serializers import ProfileSerializer

class TaskSerializer(BaseSerializer):
    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'title': instance.title,
            'description': instance.description,
            'due_date': instance.due_date.isoformat(),
            'status': instance.get_status_display(),
            'priority': instance.get_priority_display(),
            'employees': ProfileSerializer(instance.employees.all(), request=self.request).serialize(),
            'created_at': instance.created_at.isoformat(),
            'updated_at': instance.updated_at.isoformat(),
        }
