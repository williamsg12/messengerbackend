from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model =Profile 
        fields = ('username', 'name', 'age', 'account_owner','gender')
