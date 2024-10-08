''' user_details Views URL'''
from django.urls import path
from .views import  CreateUser,GenerateOtp,VerifyOtp,LoginUser,Health,getApiHealth
# VerifyOtpView

urlpatterns = [
    path('verifyotp/', VerifyOtp.as_view(), name='verify_otp'),
    path('create/', CreateUser.as_view(), name='signup'),
    path('login/',LoginUser.as_view(), name='login'),
    path('generateotp/',GenerateOtp.as_view(), name='generate_otp'),
    path('test/',Health.as_view(), name='test'),
    path('health/', getApiHealth),
]