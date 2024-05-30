from rest_framework import serializers
from core.models import Pet

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'name', 'age', 'breed', 'description', 'location', 'is_adopted', 'adopted_by', 'img']  
        read_only_fields = ['is_adopted', 'adopted_by']
        


class PetDetailSerializer(PetSerializer):
    """Serializer for pet detail view"""
    
    class Meta(PetSerializer.Meta):
        fields = PetSerializer.Meta.fields + ['description']