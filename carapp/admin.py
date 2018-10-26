from django.contrib import admin
from .models import Make,Model,Location,Profile,Image,Comment,Likes

admin.site.register(Make)
admin.site.register(Model)
admin.site.register(Location)
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Likes)