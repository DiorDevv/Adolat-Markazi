from django.urls import path
from .views import SendOTPView, VerifyOTPView

urlpatterns = [
    path('api/otp/send/', SendOTPView.as_view(), name='send_otp'),
    path('api/otp/verify/', VerifyOTPView.as_view(), name='verify_otp'),
]
