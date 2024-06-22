from rest_framework import serializers
from .models import * 
from django.conf import settings

class MarcaSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only =True, required=False)
    class Meta:
        model = Marca
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        marca = super().create(validated_data)
        if image:
            marca.image_url = self.save_image(marca, image)
            marca.save()
        return marca

    def save_image(self, marca, image):
        from django.core.files.storage import default_storage
        from django.core.files.storage import ContentFile
        import os

        path = default_storage.save(os.path.join('image', str(marca.id)+ '_'+ image.name), ContentFile(image.read())) 
        return settings.MEDIA_URL + path

class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'

class ProcesadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procesador
        fields = '__all__'

class DiscoDuroSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscoDuro
        fields = '__all__'

        