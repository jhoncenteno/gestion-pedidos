from django.contrib import admin
from app_blog.models import Categorias, post
class categoriasadmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')   
class postadmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')   


admin.site.register(Categorias, categoriasadmin)
admin.site.register(post, postadmin)