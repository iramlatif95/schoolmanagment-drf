from rest_framework import serializers

from branch.models import Branch, School 


class Schoolserializer(serializers.ModelSerializer):
    class Meta:
        model=School 
        fields='__all__'


class Branchserializer(serializers.ModelSerializer):
    class Meta:
        model=Branch 
        fields='__all__'

