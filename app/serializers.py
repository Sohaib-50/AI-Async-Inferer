from rest_framework import serializers

class PredictSerializer(serializers.Serializer):
    model_input = serializers.CharField()
    async_mode = serializers.BooleanField()

class PredictionResultSerializer(serializers.Serializer):
    prediction_id = serializers.CharField()