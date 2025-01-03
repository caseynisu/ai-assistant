from django.contrib import admin
from .models import DemoRequest, ClientFeedback, Serivces, Events


admin.site.register(DemoRequest)
admin.site.register(ClientFeedback)
admin.site.register(Serivces)
admin.site.register(Events)

admin.site.site_title = 'Ai Solution'
admin.site.site_header = 'Ai Solution'
admin.site.index_title = 'Ai Solution'