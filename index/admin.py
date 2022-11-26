from django.contrib import admin
from .models import *
#from django.contrib.auth.models import User


admin.site.register(User)
admin.site.register(Choices)
admin.site.register(Questions)
admin.site.register(Answer)
admin.site.register(Form)
admin.site.register(Responses)
