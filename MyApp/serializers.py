from rest_framework import serializers
from .models import Tours

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = '__all__'
        # fields = ['id',dia_diem','thanh_pho','khach_san','nha_hang','quan_an','giai_tri','ghi_chu']


