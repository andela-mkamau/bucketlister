from rest_framework import serializers

from ..models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):
    """
    Bucketlist serializers
    """

    class Meta:
        model = Bucketlist
        fields = '__all__'
