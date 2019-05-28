from django.contrib import admin
from . import models
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(models.CropCategory,CategoryAdmin)

class CropAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('crop_name',)}
admin.site.register(models.Crop,CropAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display=['id','f_name','l_name','dob','gender','mobile','type','password','address','zip_code','state','country','email']

admin.site.register(models.UserModel,UserAdmin)

admin.site.register(models.feedback)
#admin.site.register(models.Crop)
#admin.site.register(models.CropCategory)
