from rest_framework import serializers
from .models import Exam, Result

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    percentage = serializers.SerializerMethodField() # per is calcualted  at run time 

    class Meta:
        model = Result
        fields = '__all__'

    def get_percentage(self, obj):
        return (obj.marks_obtained / obj.total_marks) * 100
