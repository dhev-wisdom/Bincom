from django.contrib import admin
from .models import (AgentName, AnnouncedLgaResults, AnnouncedPuResults, AnnouncedStateResults, AnnouncedWardResults, \
Lga, Party, States, Ward, PollingUnit)

# Register your models here.

admin.site.register(AgentName)
admin.site.register(AnnouncedLgaResults)
admin.site.register(AnnouncedPuResults)
admin.site.register(AnnouncedStateResults)
admin.site.register(AnnouncedWardResults)
admin.site.register(Lga)
admin.site.register(PollingUnit)
admin.site.register(Party)
admin.site.register(States)
admin.site.register(Ward)
