# school/serializers.py
from rest_framework import serializers
from .models import School, Branch

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    school_name = serializers.ReadOnlyField(source='school.name')

    class Meta:
        model = Branch
        fields = '__all__'
