from rest_framework import serializers
from todo.models import todo

class Todoserializer(serializers.ModelSerializer):
    class metal:
        model = todo
        fields = '___all__'
        read_only_fields = ('id',)

class todofewserilizers(serializers.ModelSerializer):
    class Meta: 
        model = todo
        fields = ("id", "school_info","closing_remarks")
        read_only_fields= ('id')

class todocreateserializers(serializers.ModelSerializer):
     class Meta:
         model= todo
         fields = ('id''name_ofstaff','gender_choice',)
         read_onlyfields=('id')
        