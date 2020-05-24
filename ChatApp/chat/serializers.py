# Serializers allow complex data such as querysets and model instances to be converted to native 
# Python datatypes that can then be easily rendered into JSON, XML or other content types.



from django.contrib.auth.models import User
from chat.models import Message
from rest_framework import serializers


# User Serializer
class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True)
     #For Serializing User
    
    class Meta:
        model = User
        fileds = ['username', 'password']
        
        
class MessageSerializers(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many = False, slug_field= 'username', queryset = User.objects.all()) #slug is used since we used foreign key.
    receiver = serializers.SlugRelatedField(many = False, slug_field= 'username', queryset = User.objects.all())
    """The sender and receiver of Message is serialized as SlugRelatedField to represent the target of the relationship 
    using a field on the target. The field is specified as slug_field. It also takes a 'many' argument which identifies 
    the relation is many-to-many or not. We gave it false, since a message can only contain a single sender and receiver.
    The 'queryset' argument takes the list of objects from which the related object is to be chosen."""
    
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']
        

    