from rest_framework import serializers

from django.apps import apps
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:        
        model = apps.get_model('projects.Project')        
        fields ='__all__'


# class ProjectSerializer(serializers.Serializer):
#     id= serializers.ReadOnlyField()    
#     title = serializers.CharField(max_length=200)    
#     description = serializers.CharField(max_length=None)    
#     goal = serializers.IntegerField()    
#     image = serializers.URLField()    
#     is_open = serializers.BooleanField()    
#     date_created = serializers.DateTimeField()    
#     owner = serializers.CharField(max_length=200)