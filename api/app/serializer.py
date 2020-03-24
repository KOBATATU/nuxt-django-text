from rest_framework import serializers
from .models import InputText


class InputTextSerializer(serializers.Serializer):
    input_text = serializers.CharField()
    neg_pos = serializers.SerializerMethodField()

    def get_neg_pos(self,obj):
        print(obj)
        return 1