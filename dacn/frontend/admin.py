from django.contrib import admin
from .models import Discount, Categories, Website
# Register your models here.

admin.site.register(Discount)
admin.site.register(Categories)
admin.site.register(Website)