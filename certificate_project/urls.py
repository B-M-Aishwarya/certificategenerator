from django.contrib import admin
from django.urls import path
from certificate_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.create_certificate, name='create_certificate'),
    path('verify_certificate/', views.verify_certificate, name='verify_certificate'),
    path('customize_certificate/<uuid:certificate_id>/', views.customize_certificate, name='customize_certificate'),
    path('certificate_details/<uuid:certificate_id>/', views.certificate_details, name='certificate_details')
]
