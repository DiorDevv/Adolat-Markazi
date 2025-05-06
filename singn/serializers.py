from rest_framework import serializers

# OTP yuborish uchun serializer
class SendOTPSerializer(serializers.Serializer):
    chat_id = serializers.CharField(max_length=100)

# OTP tasdiqlash uchun serializer
class VerifyOTPSerializer(serializers.Serializer):
    chat_id = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=6)
