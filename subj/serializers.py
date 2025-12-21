from rest_framework import serializers 
from .models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    

    class_name=serializers.ReadOnlyField(source='class_obj.name') 
    branch_name=serializers.ReadOnlyField(source='branch.name')
    branch_name=serializers.ReadOnlyField(source='branch.name')
    

    class Meta:
        model=Subject 
        fields='__all__'