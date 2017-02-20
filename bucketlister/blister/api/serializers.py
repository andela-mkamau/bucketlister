from rest_framework import serializers

from ..models import Bucketlist, Tag


class BucketlistSerializer(serializers.ModelSerializer):
    """
    Bucketlist serializers
    """

    class Meta:
        model = Bucketlist
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    """
    Tag serializer
    """

    class Meta:
        model = Tag
        fields = '__all__'
