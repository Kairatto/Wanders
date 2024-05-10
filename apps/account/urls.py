from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.account.views import (
    RegistrationView,
    EmailActivationView,
    ChangePasswordView,
    SetRestoredPasswordView,
    RestorePasswordView,
    DeleteAccountView,
    UserRetrieveView, LogoutAPIView, UserInfoView,
)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('activate/<str:activation_code>/', EmailActivationView.as_view(), name='activation'),

    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('restore-password/', RestorePasswordView.as_view(), name='restore_password'),
    path('set-restored-password/', SetRestoredPasswordView.as_view(), name='set_restored_password'),
    path('delete-account/', DeleteAccountView.as_view(), name='delete account'),

    path('user-retrieve/<int:id>/', UserRetrieveView.as_view(), name='get-user'),
    path('user-info/', UserInfoView.as_view(), name='user-info'),

]
