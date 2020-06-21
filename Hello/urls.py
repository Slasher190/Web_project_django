from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Slasher Admin"
admin.site.site_title = "Slasher's Admin Portal"
admin.site.index_title = "Welcome to slasher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]


# django shell
# to see all object :- Contact.objects.all()