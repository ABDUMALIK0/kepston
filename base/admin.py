from django.contrib import admin

# Register your models here.
from .models import PredictResult

admin.site.register(PredictResult)