from models import Script,ScriptArgs
from rest_framework import serializers
class ScriptSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Script
        fields = ('id', 'name', 'info',
                )

class ScriptArgsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ScriptArgs
        fields= ('id','args_name','args_value')
