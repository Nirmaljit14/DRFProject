from rest_framework import serializers

from django.apps import apps

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model('projects.Pledge')
        fields = '__all__'
class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:        
        model = apps.get_model('projects.Project')        
        fields ='__all__'

class ProjectDetailSerializer (PledgeSerializer):
    pledges = PledgeSerializer (many=True, read_only=True)
# class ProjectSerializer(serializers.Serializer):
#     id= serializers.ReadOnlyField()    
#     title = serializers.CharField(max_length=200)    
#     description = serializers.CharField(max_length=None)    
#     goal = serializers.IntegerField()    
#     image = serializers.URLField()    
#     is_open = serializers.BooleanField()    
#     date_created = serializers.DateTimeField()    
#     owner = serializers.CharField(max_length=200)
