from rest_framework import serializers 
from . models import Class, Section  

from accounts.models import User

class ClassSerializer(serializers.ModelSerializer):
    teacher_name=serializers.ReadOnlyField(source='user.username')
    branch_name=serializers.ReadOnlyField(source='branch.name')
    class Meta:
        model=Class     
        fields='__all__'

class SectionSerializer(serializers.ModelSerializer):
    class_name=serializers.ReadOnlyField(source='class_obj.name')
    students_name=serializers.SlugRelatedField(many=True,read_only=True,slug_field='username',source='students')

    class Meta:
        model=Section   
        fields='__all__'



        
            
        
            