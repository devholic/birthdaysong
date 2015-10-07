from django.contrib import admin
from timeline_web.models import Rankdata
# Register your models here.

class RankdataAdmin(admin.ModelAdmin):
    list_display = ('year', 'week', 'title','artist','album','youtube')

admin.site.register(Rankdata, RankdataAdmin)
