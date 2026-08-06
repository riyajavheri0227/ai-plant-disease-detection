from django.contrib import admin
from .models import Plant, MyPlant, DiseaseInfo, ScanHistory
from .models import Contact


admin.site.register(Plant)
admin.site.register(MyPlant)
admin.site.register(DiseaseInfo)
admin.site.register(ScanHistory)
admin.site.register(Contact)

# Register your models here.
