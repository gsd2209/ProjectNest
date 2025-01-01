from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT Authentication
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT Token Refresh
    path('api/', include('management_app.urls')),  # Include app-specific routes
]
