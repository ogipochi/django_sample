from django.contrib import admin
from .models import MusicInstrument



# Register your models here.

class MusicInstrumentAdmin(admin.ModelAdmin):
    model = MusicInstrument
    fieldsets= [
    (None,{'fields':['MusicInstrument']})
    ]

admin.site.register(MusicInstrument,MusicInstrumentAdmin)



