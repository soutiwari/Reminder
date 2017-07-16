from rest_framework import serializers
from task.models import Task
from django.contrib.auth.models import User
from django.utils import six


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    timezone = serializers.SerializerMethodField()

    def get_timezone(self, obj):
        return six.text_type(obj.timezone)

    class Meta:
        model = Task
        fields = ('url', 'id', 'title', 'message', 'phoneno', 'scheduleTime', 'owner', 'timezone', 'eventId')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    task = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'task')
