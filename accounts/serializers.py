from rest_framework import serializers 
from.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=['id','username','first_name','last_name','email','role','password']
        extra_kwargs={'password':{'write_only':True}} # secure the password

    def create(self,validate_data):
        user=User(
            username=validate_data['username'],
            email=validate_data['email'],
            first_name=validate_data.get('first_name',''),
            last_name=validate_data.get('last_name',''),
            role=validate_data['role']

        )
        user.set_password(validate_data['password'])
        user.save()
        return user

